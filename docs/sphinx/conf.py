# HAND-WRITTEN: not modified by `make generate`. Edit directly.
import logging
import os
import re
import sys

# Point Sphinx directly at the generated SDK so autodoc can read the code
sys.path.insert(0, os.path.abspath("../../src"))

project = "Kentik API - Python SDK"
copyright = "2026, Kentik"
author = "Alex DeAraujo"


# Explicitly tell Sphinx to accept both .md and .rst files
source_suffix = [".rst", ".md"]

# Explicitly tell Sphinx the homepage is named "index" (so it stops looking for index.rst)
root_doc = "index"

# Exclude GitHub-browsable README files (not Sphinx pages) and build artifacts.
# "**/README.md" does not match a README at the source root, so list it too.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.md", "**/README.md"]

# Deliberately empty. Broken links surface as myst.xref_missing and orphaned
# pages as toc.not_included, so suppressing either would let `-W` pass on the
# exact defects it exists to catch. Link to files outside this tree by GitHub
# URL instead.
suppress_warnings: list[str] = []

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinxcontrib.autodoc_pydantic",  # Formats Pydantic v2 models beautifully
    "sphinxcontrib.mermaid",  # Renders Mermaid diagrams (replaces PlantUML)
]

# Tell MyST we want to use the {include} and {eval-rst} directives
myst_enable_extensions = [
    "alert",
    "colon_fence",
]

# Route plain ```mermaid fenced blocks through the mermaid directive, so the
# same fence renders natively on GitHub and via sphinxcontrib.mermaid here.
myst_fence_as_directive = ["mermaid"]

html_theme = "sphinx_book_theme"

# Skip copying every source page into build/html/_sources/. Those copies are
# byte-identical to docs/sphinx/**, and this repo already tracks the
# rendered HTML in git, so the copies were pure duplication.
html_copy_source = False
html_show_sourcelink = False

# The theme's "download source" button links to _sources/ regardless of
# html_show_sourcelink, so it needs its own opt-out too.
html_theme_options = {
    "use_download_button": False,
}

# Clean up Pydantic model rendering
autodoc_pydantic_model_show_json = True
autodoc_pydantic_settings_show_json = False
autodoc_pydantic_model_show_config_summary = False


class SuppressDocutilsFilter(logging.Filter):
    """Filter out pedantic docstring formatting warnings from generated code."""

    def filter(self, record):
        msg = record.getMessage()
        return not (
            "Block quote ends without a blank line" in msg
            or "unexpected unindent" in msg
        )


_RST_INLINE_MARKUP = re.compile(r"([\\*`|_])")


def setup(app):
    """Sphinx hook to inject our custom logger filter."""
    from sphinx.util.logging import getLogger
    from sphinxcontrib.autodoc_pydantic.directives.autodocumenters import (
        PydanticFieldDocumenter,
    )

    class SchemaTextFieldDocumenter(PydanticFieldDocumenter):
        def _get_field_description(self) -> str:
            # Field descriptions are schema prose: `c_` or `*.` is not RST markup.
            text = super()._get_field_description() or ""
            return _RST_INLINE_MARKUP.sub(r"\\\1", text)

    app.add_autodocumenter(SchemaTextFieldDocumenter, override=True)
    logger = getLogger("sphinx")
    # Dig into the underlying standard python logger to add the filter
    logger.logger.addFilter(SuppressDocutilsFilter())

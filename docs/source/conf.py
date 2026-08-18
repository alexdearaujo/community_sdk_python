import logging
import os
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

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinxcontrib.autodoc_pydantic",  # Formats Pydantic v2 models beautifully
    "sphinxcontrib.mermaid",  # Renders Mermaid diagrams (replaces PlantUML)
]

# Tell MyST we want to use the {include} and {eval-rst} directives
myst_enable_extensions = [
    "colon_fence",
]

# Route plain ```mermaid fenced blocks through the mermaid directive, so the
# same fence renders natively on GitHub and via sphinxcontrib.mermaid here.
myst_fence_as_directive = ["mermaid"]

html_theme = "sphinx_book_theme"

# Skip copying every source page into build/html/_sources/. Those copies are
# byte-identical to docs/source/**, and this repo already tracks the
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
        if (
            "Block quote ends without a blank line" in msg
            or "unexpected unindent" in msg
        ):
            return False
        return True


def setup(app):
    """Sphinx hook to inject our custom logger filter."""
    from sphinx.util.logging import getLogger

    logger = getLogger("sphinx")
    # Dig into the underlying standard python logger to add the filter
    logger.logger.addFilter(SuppressDocutilsFilter())

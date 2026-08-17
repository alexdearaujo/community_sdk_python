# Kentik Community Python SDK

An automated Python SDK for the Kentik API, generated from OpenAPI schemas and powered by `uv`, `Pydantic v2`, and `HTTPX`.

## Overview

This SDK is not maintained manually. Instead, it is **generated and patched** automatically from the [Kentik API Public Schema](https://github.com/kentik/api-schema-public). Our generation pipeline fixes common OpenAPI generator bugs, scrubs versioning from class names for a cleaner developer experience, and automatically generates architecture diagrams.

## Prerequisites

* **Python 3.12+**
* **[uv](https://github.com/astral-sh/uv)**: The lightning-fast Python package manager.
* **Java (JRE)**: Required to render PlantUML diagrams.
* **Graphviz**: Required by PlantUML for graph layouts.

    ```bash
    # macOS
    brew install openjdk graphviz
    echo 'export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"' >> ~/.zshrc
    source ~/.zshrc

    # Ubuntu/Debian
    sudo apt install default-jre graphviz
    ```

## Development Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/kentik/community_sdk_python.git
    cd community_sdk_python
    ```

2. Sync the environment:

    ```bash
    make install
    ```

## Authentication via .env

The SDK can load credentials automatically from a `.env` file at your project root.

Create `.env` in the repository root:

```bash
KENTIK_EMAIL=you@example.com
KENTIK_API_TOKEN=your_api_token
```

When `KentikAPI(...)` is created without `email` and `api_token`, it will:

1. Load the nearest `.env` file from the current working directory.
2. Read `KENTIK_EMAIL` and `KENTIK_API_TOKEN`.

You can still pass `email` and `api_token` explicitly, and explicit values take precedence.

## Generating the SDK

The SDK generation script performs the following tasks:

1. Clones/Updates the Kentik API schemas.
2. Scrubs version prefixes (e.g., v2023...) from model names.
3. Fixes generator bugs (Ghost variables, Pydantic v2 compatibility, Path sanitization).
4. Generates PlantUML architecture diagrams.
5. Formats the output with Ruff.

**To generate from the remote GitHub repo:**

```bash
make generate
```

**To generate from a local schema folder (for testing):**

```bash
make generate local
```

**To generate from a custom local schema path:**

```bash
make generate LOCAL_REPO=/path/to/api-schema-public
```

**To run the full pipeline (services + docs + tests):**

```bash
make
```

**To run stages independently:**

```bash
make services
make docs
make tests
```

## Documentation

Documentation is built using **Sphinx** and **MyST (Markdown)**. It includes automatically generated service diagrams and code references.

1. **Generate the SDK and Docs Source:**
Running the `generate_sdk.py` script automatically prepares the documentation source.

2. **Build the HTML site:**

    ```bash
    make docs
    ```

3. **View the Docs:**
Open `docs/build/html/index.html` in your browser.

## Testing

We use `pytest` for testing. Ensure you run the generator before running tests to ensure the latest models are present.

```bash
make tests
```

## Code Quality

We use Ruff for linting and formatting. The generation script runs this automatically, but you can run it manually at any time:

```bash
make lint
```

## Generation Pipeline Logic (Internal)

If you are modifying `scripts/generate_sdk.py`, keep in mind the following custom patches currently applied:

* **Flattened Structure**: Subdirectories for versions are removed; only the latest version of each service is kept.
* **Wildcard Patching**: from `.models import *` is replaced with explicit re-exports (`import X as X`) to satisfy Pylance/Ruff.
* **Ghost Data Fix**: Removes `json=data.dict()` calls in functions where the generator failed to provide a payload argument.
* **Pydantic v2**: Injects `.model_construct()` for empty API responses to prevent validation crashes.

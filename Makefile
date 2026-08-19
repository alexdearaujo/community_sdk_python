.PHONY: all help install generate services local docs tests test test-generated test-runtime test-smoke test-generator test-e2e lint clean deep-clean

.DEFAULT_GOAL := all

# Variables
PYTHON := uv run python
PYTEST := uv run pytest -vv -s -rA
RUFF   := uv run ruff
SPHINX := uv run sphinx-build
DEFAULT_LOCAL_REPO := ../api-schema-public/

# Supports either:
# - make generate local
# - make generate LOCAL_REPO=/path/to/api-schema-public
ifneq ($(filter local,$(MAKECMDGOALS)),)
LOCAL_REPO := $(DEFAULT_LOCAL_REPO)
endif

GENERATE_ARGS := $(if $(LOCAL_REPO),--local-repo $(LOCAL_REPO),)

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

all: services tests ## Generate services and run tests (docs is opt-in: run `make docs`)

install: ## Install dependencies and sync environment
	uv sync

generate: ## Generate the SDK and Architecture Diagrams
	$(PYTHON) scripts/generate_sdk.py $(GENERATE_ARGS)

services: generate ## Generate SDK services/models and architecture diagrams

local: ## Marker target for `make generate local`
	@if [ "$(MAKECMDGOALS)" = "local" ]; then \
		echo "'local' is a marker target and does not generate by itself."; \
		echo "Use: make generate local"; \
		echo "Or override: make generate LOCAL_REPO=/path/to/api-schema-public"; \
	fi

docs: ## Build the HTML documentation
	$(SPHINX) -b html docs/source docs/build/html

tests: test ## Run the full test suite (alias)

test: ## Run the test suite
	$(PYTEST) tests/

test-generated: ## Run generated wrapper contract tests only
	$(PYTEST) tests/generated/

test-runtime: ## Run shared runtime tests only
	$(PYTEST) tests/runtime/

test-smoke: ## Run smoke tests only
	$(PYTEST) tests/smoke/

test-generator: ## Run generator (scripts/generation/) unit tests only
	$(PYTEST) tests/generator/

test-e2e: ## Run end-to-end tests against the REAL Kentik API (opt-in, needs .env)
	$(PYTEST) -m e2e tests/e2e/

lint: ## Run linter and formatter (Ruff)
	$(RUFF) check --fix .
	$(RUFF) format .

clean: ## Remove generated SDK and build artifacts
	# Keep project-local customization code (do not remove):
	# - scripts/openapi_templates/
	# - src/kentik_api/core/
	# - docs/source/local_generation_workflow.md
	rm -rf src/kentik_api/gen/
	rm -rf docs/build/
	find docs/source/services -maxdepth 1 -type f -name '*.md' ! -name 'README.md' -delete
# 	rm -rf bin/				# commented out only for testing (to speed up tests)
	find . -type d -name "__pycache__" -exec rm -rf {} +

deep-clean: clean ## Remove virtual environment and lock files
	rm -rf .venv
	rm -f uv.lock
	rm -rf .pytest_cache/
	rm -rf .ruff_cache/

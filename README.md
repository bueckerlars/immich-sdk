# immich-sdk

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/badge/ruff-enabled-0080ff.svg)](https://github.com/astral-sh/ruff)

Python SDK for the [Immich](https://immich.app/) API. Type-safe client generated from the official OpenAPI specification, with support for albums, assets, authentication, libraries, and all other Immich API endpoints.

- **Official API documentation:** [Immich API](https://immich.app/docs/api)
- **OpenAPI / developer docs:** [Immich OpenAPI](https://immich.app/docs/developer/open-api)

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Install uv](#install-uv)
    - [Linux](#linux)
    - [macOS](#macos)
    - [Windows](#windows)
  - [Install the SDK](#install-the-sdk)
  - [Pre-commit (development)](#pre-commit-development)
- [Quick Start](#quick-start)

## Prerequisites

- **Python 3.13 or later.** The SDK requires Python 3.13+.
- **[uv](https://docs.astral.sh/uv/)** for dependency management and virtual environments. uv is a fast, drop-in replacement for pip and pip-tools.

## Installation

### Install uv

Install uv using one of the methods below for your platform. See [Installation - uv](https://docs.astral.sh/uv/getting-started/installation/) for more options.

#### Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Add `~/.local/bin` to your `PATH` if it is not already there (the installer will print instructions).

#### macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On macOS you can also install via Homebrew:

```bash
brew install uv
```

#### Windows

Using PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installation, restart your terminal. The installer adds uv to your user `PATH`.

### Install the SDK

Clone the repository and sync dependencies with uv:

```bash
git clone https://github.com/bueckerlars/immich-sdk.git
cd immich-sdk
uv sync
```

This creates a virtual environment (e.g. `.venv`) and installs the package and its dependencies. To install with development dependencies (testing, linting, pre-commit):

```bash
uv sync --extra dev
```

### Pre-commit (development)

For contributors: install the pre-commit hooks so that formatting and linting run automatically before each commit.

After cloning and running `uv sync --extra dev`:

```bash
pre-commit install
```

Pre-commit will then run hooks (e.g. Ruff, Black, pyupgrade, toml-sort) on staged files. To run manually:

```bash
pre-commit run --all-files
```

## Quick Start

```python
from immich_sdk import ImmichClient

client = ImmichClient(
    base_url="https://immich.example.com",
    api_key="your-api-key",
)

# Use sub-clients for each API area
albums = client.albums.get_all()
assets = client.assets.get_all()
```

Authentication uses the `x-api-key` header. Create an API key in Immich under Settings > API Keys. For more endpoints and request/response formats, see the [official Immich API documentation](https://immich.app/docs/api).

# [WIP]

## how to use
required [poetry](https://python-poetry.org/).

If you don't use poetry, install the libraries listed in `pyproject.toml` file.

```bash
poetry install
poetry run inv download-salt-and-overthrust-models
poetry run python src/box-TV-constrained-FWI.py
```
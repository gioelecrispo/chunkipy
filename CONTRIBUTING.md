# Contributing to Chunkipy

Contributions to **Chunkipy** are welcome!  
Whether you want to fix a bug, improve documentation, or propose a new feature — your help is appreciated 💪

If you find a bug or have a feature request, please [open an issue](https://github.com/gioelecrispo/chunkipy/issues).  
To contribute code, fork the repository, create a new branch, make your changes, and open a pull request.

Please make sure to:

- Include **tests** for your changes  
- Follow the official Python style guide ([PEP 8](https://www.python.org/dev/peps/pep-0008/))  
- Keep your code clean, readable, and documented  

---

## 🧑‍💻 Development Setup

You can set up your development environment using **Poetry**, **uv**, or **pip**.  
We recommend **uv** for the fastest dependency management.

### 1. Clone the repository

```bash
git clone https://github.com/gioelecrispo/chunkipy.git
cd chunkipy
```

### 2. Create a virtual environment

You can use any of the following:

```bash
# Using Python built-in venv
python -m venv .venv && source .venv/bin/activate

# Or using uv
uv venv && source .venv/bin/activate
```

### 3. Install development dependencies

#### With Poetry

```bash
pip install poetry
poetry install               # Core
poetry install --all-extras  # With all optional dependencies
```

#### With uv

```bash
pip install uv
uv sync                      # Core
uv sync --all-extras         # With all optional dependencies
```

#### With pip

```bash
pip install -e .[dev,all]    # Editable install with all extras
```

## 🧹 Linting & Formatting

We use ruff and black to ensure consistent code style.

Before committing or pushing, please run:

```bash
ruff check chunkipy
black chunkipy
```

If you have pre-commit installed, you can automate this:

```bash
pip install pre-commit
pre-commit install
```

This will automatically lint and format your code before each commit.

## 🧪 Testing

We use pytest as the main testing framework.

### Run tests with Poetry

```bash
poetry install --with test
pytest --cov=chunkipy --cov-report=term-missing
```

### Run tests with uv

```bash
uv run pytest --cov=chunkipy
```

### Run tests with pip

```bash
pytest --cov=chunkipy
```

## 📚 Documentation

Chunkipy uses Sphinx for documentation, with:

- `sphinx-autosummary` for automatic API docs
- `sphinx-multiversion` for versioned documentation

To build the docs locally:

```bash
poetry install --only docs
sphinx-multiversion docs/source docs/build/html
```

Then open:

`docs/build/html/index.html`

## ✅ Submitting Your PR

Before opening a pull request, please ensure:

- [ ] All tests pass locally (pytest)

- [ ] Code is linted (ruff + black)

- [ ] Documentation builds without warnings (sphinx-multiversion)

- [ ] Commits are clear and descriptive

Once everything looks good, open a PR and link any related issues.
Thank you for contributing to Chunkipy 🎉
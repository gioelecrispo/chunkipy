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

You can set up your development environment using **uv** (recommended) or **pip**.

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

#### With uv (recommended)

```bash
pip install uv
uv sync --all-extras --group test --group docs
```

#### With pip

```bash
pip install -e .[dev,all]    # Editable install with docs+test+all extras
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

### Test doubles policy (no monkey patch)

To keep tests deterministic and resilient, prefer **fake subclasses** and
dependency injection over monkey patching.

- Use helper names like `Fake...`, `Stub...`, `Dummy...` (avoid `Test...` for helper classes)
- Keep fakes minimal: override only what is needed
- Avoid runtime patching of import paths unless strictly necessary
- Keep fake behavior deterministic and explicit
- Validate edge cases through public APIs

### Run tests with uv

```bash
uv run pytest --cov=chunkipy --cov-report=term-missing
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
uv sync --group docs
uv run sphinx-multiversion docs/source docs/build/html
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

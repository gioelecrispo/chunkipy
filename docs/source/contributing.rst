Contributing
==================
Contributions to ``chunkipy`` are welcome!  
Whether you want to fix a bug, improve documentation, or propose a new feature, your help is appreciated.

If you find a bug or have a feature request, please open an issue on `GitHub <https://github.com/gioelecrispo/chunkipy/issues>`_.  
To contribute code, fork the repository, create a feature branch, make your changes, and submit a pull request.  
Please make sure to include appropriate **tests** and follow the official Python `style guide (PEP 8) <https://www.python.org/dev/peps/pep-0008/>`_.


Development setup
------------------
You can set up your development environment using **uv** (recommended) or **pip**.

**1. Clone the repository**

.. code-block:: bash

    git clone https://github.com/gioelecrispo/chunkipy.git
    cd chunkipy

**2. Create a virtual environment**

You can use any of the following:

.. code-block:: bash

    # Using Python built-in venv
    python -m venv .venv && source .venv/bin/activate

    # Or using uv
    uv venv && source .venv/bin/activate

**3. Install development dependencies**

.. tab:: uv

    .. code-block:: bash

        pip install uv
        uv sync --all-extras --group test --group docs

.. tab:: pip

    .. code-block:: bash

        pip install -e .[dev,all]    # Editable install with docs+test+all extras


Linting & formatting
--------------------
We use ``ruff`` and ``black`` to keep the codebase consistent.  
Run the following before submitting a PR:

.. code-block:: bash

    ruff check chunkipy
    black chunkipy


Testing
------------------
We use ``pytest`` as the main testing framework.

.. code-block:: bash

    uv run pytest --cov=chunkipy --cov-report=term-missing


Documentation
------------------
``chunkipy`` uses ``sphinx`` to build the documentation, leveraging ``autosummary`` for code reference
and ``sphinx-multiversion`` to provide versioned docs.

To build docs locally:

.. code-block:: bash

    uv sync --group docs
    uv run sphinx-multiversion docs/source docs/build/html

Then open ``docs/build/html/index.html`` in your browser.


Submitting your PR
------------------
Before submitting your pull request, please ensure that:
- All tests pass locally (`pytest` ✅)
- Code is linted (`ruff` + `black` ✅)
- Documentation builds without warnings (`sphinx-multiversion` ✅)
- Commit messages are clear and descriptive

Once ready, open a pull request and link any related issue.  
Thank you for helping improve ``chunkipy`` 🎉

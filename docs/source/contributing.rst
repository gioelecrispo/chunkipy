Contributing
==================
If you find a bug or have a feature request, please open an issue on [GitHub](https://github.com/gioelecrispo/chunkipy/issues).
Contributions are welcome! Just fork the repository, create a new branch with your changes, and submit a pull request. Please make sure to write tests for your changes and to follow the [code style](https://www.python.org/dev/peps/pep-0008/).


Development 
------------------
To start developing chunkipy, it is recommended to: 

1. Create a virtual environment (e.g. ``python -m venv .venv``) and activate it
2. Install poetry via ``pip install poetry``
3. Install the development dependencies via one of these commands:

.. code-block:: bash

    poetry install  # no extra dependencies
    poetry install --extra spacy-splitter
    poetry install --extra openai-splitter,openai-estimator  # multiple extras dependencies
    poetry install --all-extras  # all the extras dependencies



Documentation
------------------
``chunkipy`` relies on python docstrings and ``sphinx`` for its documentation.
``sphinx-autosummary`` is used to automatically generate documentation from code.

``sphinx-multiversion`` is used to provide multiversion support, i.e. you can navigation documention for past version too.

This is handled via Github Action, but you can reproduce it by installing the needed dependencies:

.. code-block:: bash

    poetry install --only docs

and then by running the following command:

.. code-block:: bash

    sphinx-multiversion docs/source docs/build/html



Testing
------------------
We use ``pytest`` as main testing framework. 
You can install al the testing dependencies by running: 

.. code-block:: bash

    poetry install --with test

Once done, you can run all the unit test (and check the coverage) with this command from the project folder:

.. code-block:: bash
    
    pytest --cov=chunkipy --cov-report=term



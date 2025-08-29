Installation
==================

You can install ``chunkipy`` in different ways depending on your needs and preferences. Below are the methods for installing Chunkipy using pip or poetry.

``chunkipy`` has a bunch of optional dependencies that you can install based on your requirements. 
The aim is to keep the core library lightweight while allowing users to choose additional features as needed.
Note that you can install multiple optional dependencies at once.

List of optional dependencies
--------------------------------

- ``stanza``: for using ``stanza`` as a text splitter
- ``spacy``: for using ``spaCy`` as a text splitter
- ``langdetect``: for using ``langdetect`` for language detection
- ``tiktoken``: for using ``tiktoken`` to count tokens using OpenAI's tokenizer


Install using pip
----------------------------

You can install Chunkipy using pip by running the following command:

.. tab:: Core installation

    This will install the core library without optional dependencies. 

    .. code-block:: bash

        pip install chunkipy 

.. tab:: Single extra dependency

    This will install the core library along with the ``stanza`` library to use Stanza as a text splitter.

    .. code-block:: bash

        pip install chunkipy[stanza]  

.. tab:: Multiple extra dependencies

    This will install the core library along with the ``stanza``, ``spacy`` and ``langdetect`` libraries.
    Stanza and spaCy will be used as text splitters, while langdetect will be used for language detection.

    .. code-block:: bash

        pip install chunkipy[stanza, spacy, langdetect]  

.. tab:: All extra dependencies

    This will install the core library along with all optional dependencies.

    .. code-block:: bash

        pip install chunkipy[all]  



Install using poetry
----------------------------

If you want to use poetry instead, you can run the following command:


.. tab:: Core installation

    This will install the core library without optional dependencies. 

    .. code-block:: bash

        poetry add chunkipy # basic installation


.. tab:: Single extra dependency

    This will install the core library along with the ``stanza`` library to use Stanza as a text splitter.

    .. code-block:: bash

        poetry add chunkipy[stanza] 

.. tab:: Multiple extra dependencies

    This will install the core library along with the ``stanza``, ``spacy`` and ``langdetect`` libraries.
    Stanza and spaCy will be used as text splitters, while langdetect will be used for language detection.

    .. code-block:: bash

        poetry add chunkipy[stanza, spacy, langdetect]  

.. tab:: All extra dependencies

    This will install the core library along with all optional dependencies.

    .. code-block:: bash

        poetry add chunkipy[all]  






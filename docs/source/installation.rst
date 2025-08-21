Installation
==================

You can install ``chunkipy`` in different ways depending on your needs and preferences. Below are the methods for installing Chunkipy using pip or poetry.

``chunkipy`` has a bunch of optional dependencies that you can install based on your requirements. 
The aim is to keep the core library lightweight while allowing users to choose additional features as needed.

List of optional dependencies
----------------------------
- ``stanza``: for using ``stanza`` as a text splitter
- ``spacy``: for using ``spaCy`` as a text splitter
- ``langdetect``: for using ``langdetect`` for language detection
- ``tiktoken``: for using ``tiktoken`` to count tokens using OpenAI's tokenizer


Install using pip
----------------------------

You can install Chunkipy using pip by running the following command:

.. code-block:: bash

    pip install chunkipy

This will install the core library without optional dependencies. 
This is sufficient for basic usage and to give flexibility for the user to choose which optional dependencies to install based on their needs or restrictions.

If you want you can install it with optional dependencies:

.. code-block:: bash

    pip install chunkipy[stanza]  # with stanza libraries to use Stanza as text splitter

    pip install chunkipy[spacy]  # with spacy libraries to use SpaCy as text splitter

    pip install chunkipy[langdetect]  # with langdetect libraries to use LangDetect for language detection

    pip install chunkipy[tiktoken]  # with tiktoken library to count tokens using OpenAI's tokenizer

    # you can combine them, e.g. spacy to split and tiktoken (openai) to count the tokens
    pip install chunkipy[spacy, langdetect, tiktoken]

You can also install it with **all** the optional dependencies:

.. code-block:: bash

    pip install chunkipy[all]

Install using poetry
----------------------------

If you want to use poetry instead, you can run the following command:

.. code-block:: bash

    poetry add chunkipy # basic installation

If you want to install it with optional dependencies, you can run:

.. code-block:: bash

    poetry add chunkipy[spacy, langdetect]

    poetry add chunkipy[stanza, spacy, langdetect, tiktoken]



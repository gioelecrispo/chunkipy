Installation Guide
==================

You can install Chunkipy using pip:

.. code-block:: bash

    pip install chunkipy

If you want you can install it with optional dependencies:

.. code-block:: bash

    pip install chunkipy[stanza-splitter]  # with langdetect and stanza libraries to use Stanza as text splitter

    pip install chunkipy[spacy-splitter]  # with langdetect and spacy libraries to use SpaCy as text splitter

    pip install chunkipy[openai-estimator]  # with tiktoken library to count tokens using OpenAI's tokenizer

    # you can combine them, e.g. spacy to split and tiktoken (openai) to count the tokens
    pip install chunkipy[spacy-splitter, openai-estimator]

You can also install it with all the optional dependencies:

.. code-block:: bash

    pip install chunkipy[all]


If you want to use poetry instead, you can run the following command:

.. code-block:: bash

    poetry add chunkipy[stanza-splitter, spacy-splitter, openai-estimator]


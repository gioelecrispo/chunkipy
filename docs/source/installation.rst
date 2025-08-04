Installation Guide
==================

You can install Chunkipy using pip:

.. code-block:: bash

    pip install chunkipy

If you want you can install it with optional dependencies:

.. code-block:: bash

    pip install chunkipy[stanza-splitter]
    
    pip install chunkipy[spacy-splitter]

    # you can combine them, e.g. spacy to split and tiktoken (openai) to count the tokens
    pip install chunkipy[openai-splitter, openai-estimator]

You can also install it with all the optional dependencies:

.. code-block:: bash

    pip install chunkipy[all]



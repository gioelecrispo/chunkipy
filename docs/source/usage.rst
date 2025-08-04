Using Chunkipy
==============

To use Chunkipy, you first need to install it. You can do this using pip, as described in the installation guide. 
Once installed, you can start using it to chunk text.

Basic Usage
--------------

Here is an example to help you use Chunkipy to split text into chunks, with char or token counting.
tokens = False by default, so it will count characters. If you want to count tokens, set it to True.
You can also specify the chunk size in characters or tokens.

.. code-block:: python

    from chunkipy import TextChunker

    # Create a TextChunker instance with a specified chunk size
    text_chunker = TextChunker(chunk_size=512, tokens=False)  # Set tokens=True to count tokens instead of characters
    
    # Chunk your text
    chunks = text_chunker.chunk("Your long text here...")

    # Print each chunk
    for chunk in chunks:
        print(chunk)


Advanced Usage
-----------------

You can also use Chunkipy with different splitters and estimators. 
For example, you can use the Stanza or SpaCy splitters to handle more complex text structures.
Remember to install the optional dependencies, i.e. `pip install chunkipy[stanza-splitter]`, if you want to use these features.

.. code-block:: python

    from chunkipy import TextChunker, StanzaSplitter

    # Create a TextChunker instance with a Stanza splitter
    text_chunker = TextChunker(chunk_size=512, splitter=StanzaSplitter(), tokens=False)
    
    # Chunk your text
    chunks = text_chunker.chunk("Your long text here...")

    # Print each chunk
    for chunk in chunks:
        print(chunk)


You can also use the OpenAI tokenizer to estimate the number of tokens in your text, which is useful for applications that require token-based processing.

.. code-block:: python

    from chunkipy import TextChunker, OpenAITokenizer

    # Create a TextChunker instance with an OpenAI tokenizer
    text_chunker = TextChunker(chunk_size=512, tokenizer=OpenAITokenizer(), tokens=True)
    
    # Chunk your text
    chunks = text_chunker.chunk("Your long text here...")

    # Print each chunk
    for chunk in chunks:
        print(chunk)


Examples
-----------------
You can find more examples in the `examples` directory of the Chunkipy repository.


Using Chunkipy
==============

Here is an example to help you use Chunkipy to split text into chunks:

.. code-block:: python

    from chunkipy import TextChunker

    text_chunker = TextChunker(chunk_size=512, tokens=True)
    chunks = text_chunker.chunk("Your long text here...")

    for chunk in chunks:
        print(chunk)

Quickstart
==============

This page shows the main patterns to get productive quickly with the currently implemented API.


Basic chunking
-----------------------------

Use ``FixedSizeTextChunker`` when you want predictable chunk sizes.

.. code-block:: python

    from chunkipy import FixedSizeTextChunker

    text = "Chunkipy makes text processing modular, flexible, and powerful!"

    chunker = FixedSizeTextChunker(chunk_size=20)
    chunks = chunker.chunk(text)

    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}: {chunk}")


Overlapping
--------------------------

Set ``overlap_ratio`` (from ``0.0`` to ``1.0``) to preserve context between adjacent chunks.

.. code-block:: python

    from chunkipy import FixedSizeTextChunker

    text = "This is a long text used to demonstrate overlap behavior in Chunkipy."

    chunker = FixedSizeTextChunker(chunk_size=20, overlap_ratio=0.3)
    chunks = chunker.chunk(text)

    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}: {chunk}")


Choose a size estimator
--------------------------

Use a custom estimator when chunk size should be measured with domain-specific logic.

.. code-block:: python

    from chunkipy import FixedSizeTextChunker
    from chunkipy.size_estimators.base_size_estimator import BaseSizeEstimator

    class CommaSizeEstimator(BaseSizeEstimator):
        def estimate_size(self, text):
            return len(text.split(","))

        def segment(self, text):
            return text.split(",")

    estimator = CommaSizeEstimator()
    chunker = FixedSizeTextChunker(chunk_size=3, size_estimator=estimator)
    text = "alpha,beta,gamma,delta"
    chunks = chunker.chunk(text)


Recursive chunking with splitters
----------------------------------

Use ``RecursiveTextChunker`` with one or more splitters to preserve natural boundaries.

.. code-block:: python

    from chunkipy import RecursiveTextChunker
    from chunkipy.text_splitters import FullStopTextSplitter

    splitter = FullStopTextSplitter()
    chunker = RecursiveTextChunker(chunk_size=120, overlap_ratio=0.2, text_splitters=[splitter])

    text = "First sentence. Second sentence. Third sentence."
    chunks = chunker.chunk(text)


Semantic sentence splitters (spaCy / Stanza)
-----------------------------------------------

For sentence-aware splitting, use semantic splitters with ``RecursiveTextChunker``.

Install extras:

.. code-block:: bash

    pip install "chunkipy[spacy]"
    pip install "chunkipy[stanza]"

Example:

.. code-block:: python

    from chunkipy import RecursiveTextChunker
    from chunkipy.text_splitters.semantic.sentences import StanzaSentenceTextSplitter

    splitter = StanzaSentenceTextSplitter()
    chunker = RecursiveTextChunker(chunk_size=200, overlap_ratio=0.25, text_splitters=[splitter])

    text = "This is a sample text. It will be split into sentences and then chunked."
    chunks = chunker.chunk(text)


Examples
-----------------

See runnable scripts in ``examples/chunkers``:

- ``fixed_size/custom_size_estimator.py``
- ``recursive/overlapping.py``
- ``recursive/custom_text_splitter.py``
- ``recursive/prebuilt_spacy_text_splitter.py``
- ``recursive/prebuilt_stanza_text_splitter.py``


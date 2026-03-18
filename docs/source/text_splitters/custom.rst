Custom text splitters
======================

Create a custom splitter when built-in separator/sentence splitters are not enough for your domain.

Base class
----------

Extend :class:`BaseTextSplitter <chunkipy.text_splitters.BaseTextSplitter>` and implement ``_split(self, text: str) -> list[str]``.

Minimal example
----------------

.. code-block:: python

    from chunkipy import RecursiveTextChunker
    from chunkipy.text_splitters.base_text_splitter import BaseTextSplitter

    class ArrowTextSplitter(BaseTextSplitter):
        def _split(self, text: str) -> list[str]:
            return [part.strip() for part in text.split("->") if part.strip()]

    splitter = ArrowTextSplitter()
    chunker = RecursiveTextChunker(chunk_size=50, text_splitters=[splitter])

    text = "part one -> part two -> part three"
    chunks = chunker.chunk(text)


Guidelines
-----------

- Return meaningful segments, not single characters, unless explicitly needed.
- Keep splitter output deterministic.
- Validate edge separators in unit tests for your domain texts.


See also
---------

- :doc:`overview`
- :doc:`../quickstart`

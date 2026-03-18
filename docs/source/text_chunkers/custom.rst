Custom text chunkers
====================

Create a custom chunker when built-in strategies are not enough for your domain.

Base class
----------

Extend :class:`BaseTextChunker <chunkipy.text_chunker.BaseTextChunker>` and implement
``chunk(self, text: str) -> Chunks``.

If your chunker is still based on split-then-build flow, you can instead extend
:class:`BaseOverlapTextChunker <chunkipy.text_chunker.BaseOverlapTextChunker>`
and keep ``split_text`` as a thin delegate to your splitter.

Minimal example
---------------

.. code-block:: python

    from typing import Generator

    from chunkipy.text_chunker import BaseOverlapTextChunker
    from chunkipy.text_chunker.data_models import TextPart, Chunks
    from chunkipy.text_splitters import WordTextSplitter


    class WordWindowChunker(BaseOverlapTextChunker):
        def __init__(self, chunk_size: int = 50, overlap_ratio: float = 0.0):
            super().__init__(chunk_size=chunk_size, overlap_ratio=overlap_ratio)
            self._splitter = WordTextSplitter()

        def chunk(self, text: str) -> Chunks:
            # Focus of customization: chunking policy.
            # Here we normalize and then use the shared split/build flow.
            normalized_text = " ".join(text.split())
            return super().chunk(normalized_text)

        def split_text(self, text: str) -> Generator[TextPart, None, None]:
            # Keep splitting simple: just delegate to a splitter.
            for part in self._splitter.split(text):
                yield TextPart(
                    text=part,
                    size=self.size_estimator.estimate_size(part),
                )


    chunker = WordWindowChunker(chunk_size=6, overlap_ratio=0.2)
    chunks = chunker.chunk("Custom chunk policy with simple splitting delegation.")

Guidelines
----------

- Put custom policy in ``chunk`` when your roadmap strategy changes chunking logic.
- Keep ``split_text`` minimal and deterministic when using split-then-build chunkers.
- Reuse configured ``size_estimator`` and overlap behavior from base classes.

See also
--------

- :doc:`overview`
- :doc:`../quickstart`

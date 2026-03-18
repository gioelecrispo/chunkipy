Custom size estimators
=======================

Create a custom estimator when chunk size must follow domain-specific logic.

Base class
----------

Extend :class:`BaseSizeEstimator <chunkipy.size_estimators.BaseSizeEstimator>` and implement:

- ``estimate_size(self, text: str) -> int``
- ``segment(self, text: str) -> Generator[str, None, None]``

The ``segment`` method is especially important for
:class:`FixedSizeTextChunker <chunkipy.text_chunker.FixedSizeTextChunker>`.
Instead of depending on a separate splitter implementation, the chunker uses
``segment`` as its atomic splitting strategy. This keeps sizing and splitting
logic in one place and avoids duplicating domain rules across estimator and
splitter components. Different size estimator and splitter combinations would
not make sense for ``FixedSizeTextChunker``.

Minimal example
----------------

.. code-block:: python

    from chunkipy import FixedSizeTextChunker
    from chunkipy.size_estimators.base_size_estimator import BaseSizeEstimator

    class CommaSizeEstimator(BaseSizeEstimator):
        def estimate_size(self, text: str) -> int:
            return len(text.split(","))

        def segment(self, text: str):
            for part in text.split(","):
                yield part

    estimator = CommaSizeEstimator()
    chunker = FixedSizeTextChunker(chunk_size=3, size_estimator=estimator)

    text = "alpha,beta,gamma,delta"
    chunks = chunker.chunk(text)


Guidelines
-----------

- Keep ``estimate_size`` and ``segment`` logically consistent.
- For ``FixedSizeTextChunker``, implement ``segment`` carefully because it controls atomic parts and replaces the need for a dedicated splitter.
- Use tests with representative long and short texts.


See also
---------

- :doc:`overview`
- :doc:`../quickstart`

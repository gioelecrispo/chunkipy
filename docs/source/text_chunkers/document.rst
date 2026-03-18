Document-based chunking (Roadmap)
=================================

.. important::

   This chunker is planned and not available in the current public API.

Goal
-----

Document-based chunking is intended for structured sources (for example markdown sections, HTML blocks, or paragraph groups), where boundaries should follow document semantics.

Planned behavior
----------------

- Prioritize structural separators such as headings and paragraph breaks.
- Preserve section-level context before applying size constraints.
- Keep compatibility with existing splitters and size estimators.

Current status
--------------

- No importable ``DocumentBasedTextChunker`` class is available yet.
- Use :class:`RecursiveTextChunker <chunkipy.text_chunker.RecursiveTextChunker>` for production workflows today.

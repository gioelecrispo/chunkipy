Semantic chunking (Roadmap)
============================

.. important::

   This chunker is planned and not available in the current public API.

Goal
-----

Semantic chunking is intended to group adjacent text by meaning, improving coherence for retrieval and embedding pipelines.

Planned behavior
----------------

- Build chunks around semantically related spans.
- Integrate with sentence-level splitters and optional language-aware components.
- Balance semantic cohesion with target chunk size constraints.

Current status
--------------

- No importable ``SemanticTextChunker`` class is available yet.
- For now, combine :class:`RecursiveTextChunker <chunkipy.text_chunker.RecursiveTextChunker>` with semantic sentence splitters from ``chunkipy.text_splitters.semantic.sentences``.

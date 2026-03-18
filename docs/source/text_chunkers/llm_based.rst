LLM-based chunking (Roadmap)
=============================

.. important::

   This chunker is planned and not available in the current public API.

Goal
-----

LLM-based chunking is intended for advanced segmentation where chunk boundaries depend on instruction-following or task-specific semantic interpretation.

Planned behavior
----------------

- Use model-guided boundary proposals.
- Support strategy prompts for domain-specific chunking.
- Provide deterministic fallbacks when model access is unavailable.

Current status
--------------

- No importable ``LLMBasedChunker`` class is available yet.
- Use :class:`FixedSizeTextChunker <chunkipy.text_chunker.FixedSizeTextChunker>` or :class:`RecursiveTextChunker <chunkipy.text_chunker.RecursiveTextChunker>` in production today.

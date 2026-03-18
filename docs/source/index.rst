Welcome to Chunkipy's documentation!
====================================

**GitHub Repository**: https://github.com/gioelecrispo/chunkipy

.. image:: https://img.shields.io/badge/python-3.10%2C%203.11%2C%203.12%2C%203.13-blue.svg
   :alt: Python 3.10, 3.11, 3.12, 3.13
   :target: #

.. image:: https://badge.fury.io/py/chunkipy.svg
   :alt: PyPI version
   :target: https://badge.fury.io/py/chunkipy

.. image:: https://codecov.io/gh/gioelecrispo/chunkipy/graph/badge.svg?token=2A7KQ87Q62
   :alt: Codecov
   :target: https://codecov.io/gh/gioelecrispo/chunkipy




``chunkipy`` is a **modular and extensible text chunking library** for Python — built to help you split large texts into smaller, meaningful segments for NLP, LLMs, and text processing pipelines.

It provides both **ready-to-use chunkers** and **plug-and-play components**, enabling developers to use it out of the box or fully customize its behavior according to their own needs.


Why Chunkipy?
-------------

Traditional text-splitting libraries often limit flexibility to simple fixed-size splitting or token-based segmentation, ignoring linguistic or semantic structure.
``chunkipy`` bridges that gap with a **flexible, language-aware architecture** that adapts to your use case.

- ✅ **Lightweight core** — install only what you need
- ✅ **Configurable overlapping** via ``overlap_ratio`` to preserve context across chunks
- ✅ **Plug-and-play defaults** for immediate use without configuration
- ✅ **Optional language detection** for multilingual text processing
- ✅ **Highly modular design** — every component (chunker, splitter, estimator, detector) can be replaced or extended

The result is a library that's both **pragmatic for production** and **powerful for research**, enabling data scientists and developers to easily find the best chunking strategy for a given use case.


Available Chunkers
-------------------

``chunkipy`` provides several built-in chunking strategies, each designed for different use cases.
All of them implement a common interface, so you can easily switch between them or even define your own custom chunker.

They are flexible: you can combine them with custom text splitters, size estimators, or language detectors.


FixedSizeTextChunker
^^^^^^^^^^^^^^^^^^^^^^

✅ **Available now** — ``pip install chunkipy``

Splits text into fixed-size chunks based on the number of words or characters.
This is the simplest and most predictable method, suitable when you just need evenly sized chunks for processing.

.. image:: img/gifs/fixed_size.gif
   :width: 500
   :alt: Fixed-size chunking
   :target: text_chunkers/fixed_size.html

RecursiveTextChunker
^^^^^^^^^^^^^^^^^^^^^^

✅ **Available now** — ``pip install chunkipy``

Uses a hierarchy of rules to split text at logical boundaries (e.g., paragraphs, sentences) while respecting the desired chunk size and overlap.

.. image:: img/gifs/recursive.gif
   :width: 500
   :alt: Recursive chunking
   :target: text_chunkers/recursive.html

DocumentBasedTextChunker
^^^^^^^^^^^^^^^^^^^^^^^^^^

🗺️ **Roadmap** — not yet implemented

Splits text based on document structure, such as paragraphs or sections. For example, it can split at double newlines or specific headings, depending on the document's type (markdown, HTML, etc.).

.. image:: img/gifs/document_based.gif
   :width: 500
   :alt: Document-based chunking
   :target: text_chunkers/document.html

SemanticTextChunker
^^^^^^^^^^^^^^^^^^^^^^

🗺️ **Roadmap** — not yet implemented

Splits text based on semantic similarity between consecutive sentences or paragraphs.
This method ensures that each chunk preserves contextual coherence — ideal for embeddings, RAG pipelines, and LLM-driven applications.

.. image:: img/gifs/semantic.gif
   :width: 500
   :alt: Semantic chunking
   :target: text_chunkers/semantic.html

LLMBasedChunker
^^^^^^^^^^^^^^^^

🗺️ **Roadmap** — not yet implemented

Uses a large language model (LLM) to intelligently segment text based on its meaning and context.
This approach is highly flexible and can adapt to various text types and structures, making it suitable for
complex chunking tasks.

.. image:: img/gifs/llm_based.gif
   :width: 500
   :alt: LLM-based chunking
   :target: text_chunkers/llm_based.html

CustomTextChunker
^^^^^^^^^^^^^^^^^^^^^^

You can create your own chunker by extending the base :class:`BaseTextChunker <chunkipy.text_chunker.BaseTextChunker>` class and implementing the ``chunk`` method.

.. list-table::
   :header-rows: 1
   :widths: 30 15 12 23

   * - Type
     - Status
     - Overlap
     - Language-Aware
   * - **FixedSizeTextChunker**
     - ✅ Available
     - ✅
     - ❌
   * - **RecursiveTextChunker**
     - ✅ Available
     - ✅
     - ✅ (depends on the splitter)
   * - **DocumentBasedTextChunker**
     - 🗺️ Roadmap
     - ✅
     - ❌
   * - **SemanticTextChunker**
     - 🗺️ Roadmap
     - ✅
     - ✅
   * - **LLMBasedTextChunker**
     - 🗺️ Roadmap
     - ❌
     - ✅
   * - **CustomTextChunker**
     - ✅ Available
     - ✅/❌
     - ✅/❌


**Configurable Overlapping**
   Preserve context across chunks with configurable overlap ratios via ``overlap_ratio`` (0.0–1.0).
   Overlapping is supported for all chunkers except the LLM-based one:
   :class:`FixedSizeTextChunker <chunkipy.text_chunker.FixedSizeTextChunker>` and
   :class:`RecursiveTextChunker <chunkipy.text_chunker.RecursiveTextChunker>` support it today.

**Pre-built and Customizable Splitters**
   Ready-to-use text splitters (e.g. :class:`SpacySentenceTextSplitter <chunkipy.text_splitters.semantic.sentences.SpacySentenceTextSplitter>`) are available,
   but you can easily implement your own custom splitter by extending :class:`BaseTextSplitter <chunkipy.text_splitters.base_text_splitter.BaseTextSplitter>`.

**Language Detection (Optional)**
   ``chunkipy`` includes **plug-and-play language detectors** for cases where splitting logic depends on language (e.g. spaCy or Stanza models).
   It is completely optional — you can use built-in detectors or implement your own by extending :class:`BaseLanguageDetector <chunkipy.language_detectors.BaseLanguageDetector>`.

**Highly Modular Architecture**
   Every component of the pipeline is replaceable and independently configurable:

   - **Chunkers** define how chunks are formed.
   - **Splitters** define how text is divided into linguistic units.
   - **Size estimators** define how chunk size is measured (characters, words, tokens).
   - **Detectors** identify the language for language-dependent splitters.

   This modularity allows users to combine, extend, or replace any part of the system without touching the rest of the library.


Quick Summary
--------------

- 🧩 **2 built-in chunkers** available now — 3 more on the roadmap.
- 🔁 **Overlapping support** — configurable context preservation via ``overlap_ratio``.
- 🧠 **Smart splitters** — pre-built (spaCy, Stanza) and fully customizable.
- 🌍 **Optional language detection** — lightweight and extendable.
- ⚙️ **Highly modular architecture** — all components are replaceable.
- 🚀 **Ready-to-use defaults** — works out of the box, no configuration required.


.. toctree::
   :maxdepth: 1
   :caption: Getting Started
   :hidden:

   installation
   quickstart
   api
   contributing

.. toctree::
   :maxdepth: 1
   :caption: Text Chunkers
   :hidden:

   text_chunkers/overview
   text_chunkers/custom
   text_chunkers/fixed_size
   text_chunkers/recursive
   text_chunkers/document
   text_chunkers/semantic
   text_chunkers/llm_based

.. toctree::
   :maxdepth: 1
   :caption: Text Splitters
   :hidden:

   text_splitters/overview
   text_splitters/custom
   text_splitters/spacy
   text_splitters/stanza

.. toctree::
   :maxdepth: 1
   :caption: Language Detection
   :hidden:

   language_detectors/overview
   language_detectors/custom
   language_detectors/langdetect
   language_detectors/fasttext

.. toctree::
   :maxdepth: 1
   :caption: Size Estimators
   :hidden:

   size_estimators/overview
   size_estimators/custom
   size_estimators/char
   size_estimators/word
   size_estimators/openai

# Chunkipy

[![Python 3.10–3.13](https://img.shields.io/badge/python-3.10%20|%203.11%20|%203.12%20|%203.13-blue.svg)](#)
[![PyPI version](https://badge.fury.io/py/chunkipy.svg)](https://badge.fury.io/py/chunkipy)
[![codecov](https://codecov.io/gh/gioelecrispo/chunkipy/graph/badge.svg?token=2A7KQ87Q62)](https://codecov.io/gh/gioelecrispo/chunkipy)
[![Docs](https://img.shields.io/badge/docs-online-success)](https://gioelecrispo.github.io/chunkipy/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

`chunkipy` is a **modular and extensible text chunking library** for Python — built to help you split large texts into smaller, meaningful segments for NLP, LLMs, and text processing pipelines.  

It provides both **ready-to-use chunkers** and **plug-and-play components**, enabling developers to use it out of the box or fully customize its behavior according to their own needs.  

---

## Why Chunkipy?

Traditional text-splitting libraries often limit flexibility to simple fixed-size splitting or token-based segmentation, ignoring linguistic or semantic structure.  
`chunkipy` bridges that gap with a **flexible, language-aware architecture** that adapts to your use case.

- ✅ **Lightweight core** — install only what you need  
- ✅ **Five chunking strategies** (fixed, recursive, document-based, semantic, LLM-based)  
- ✅ **Configurable overlapping** to preserve context across chunks.
- ✅ **Plug-and-play defaults** for immediate use without configuration.  
- ✅ **Optional language detection** for multilingual text processing, used seamlessly by semantic or linguistic splitters.  
- ✅ **Highly modular design** — every component (chunker, splitter, size estimator, detector) can be replaced or extended.  

The result is a library that’s both **pragmatic for production** and **powerful for research**, enabling data scientists and developers to easily find the best chunking strategy for a given use case.

---

## Quick Example

```python
from chunkipy import FixedSizeChunker

text = "Chunkipy makes text processing modular, flexible, and powerful!"

chunker = FixedSizeChunker(chunk_size=20, overlap_percentage=0.2)
chunks = chunker.chunk(text)

for i, c in enumerate(chunks):
    print(f"Chunk {i+1}: {c}")
```

**Output:**

```bash
Chunk 1: Chunkipy makes text
Chunk 2: text processing modular,
Chunk 3: modular, flexible, and
Chunk 4: and powerful!
```

> ✨ Works out-of-the-box — no setup required.
> For semantic or language-specific chunking, install the appropriate splitter extras.

## Available Chunkers

`chunkipy` provides several built-in chunking strategies, each designed for different use cases.
All of them implement a common interface, so you can easily switch between them or even define your own custom splitter.

Also, they are flexible: you can combine them with custom text splitters, size estimators, or language detectors.

### FixedSizeTextChunker

Splits text into fixed-size chunks based on the number of tokens or characters.
This is the simplest and most predictable method, suitable when you just need evenly sized chunks for processing.

![fixed_size](docs/source/img/gifs/fixed_size.gif)

### RecursiveTextChunker

It uses a hierarchy of rules to split text at logical boundaries (e.g., paragraphs, sentences) while respecting the desired chunk size and overlap.

![recursive](docs/source/img/gifs/recursive.gif)

### DocumentBasedTextChunker

Splits text based on document structure, such as paragraphs or sections. For example, it can split at double newlines or specific headings, depending on the document's type (markdown, HTML, etc.).

![document_based](docs/source/img/gifs/document_based.gif)

### SemanticTextChunker

Splits text based on semantic similarity between consecutive sentences or paragraphs.
This method ensures that each chunk preserves contextual coherence — ideal for embeddings, RAG pipelines, and LLM-driven applications.

![semantic](docs/source/img/gifs/semantic.gif)

### LLMBasedChunker

Uses a large language model (LLM) to intelligently segment text based on its meaning and context.
This approach is highly flexible and can adapt to various text types and structures, making it suitable for
complex chunking tasks.

![llm_based](docs/source/img/gifs/llm_based.gif)

### CustomTextChunker

You can create your own chunker by extending the base `TextChunker` class and implementing the `chunk` method.

| Type                      | Description                                                     | Overlap | Language-Aware               |
| ------------------------- | --------------------------------------------------------------- | ------- | ---------------------------- |
| **FixedSizeTextChunker**      | Split by fixed size (characters or tokens)                      | ✅       | ❌                           |
| **RecursiveTextChunker**      | Recursively split text using multiple rules                     | ✅       | ✅ (Depends on the splitter) |
| **DocumentBasedTextChunker**  | Split by document structure (paragraphs, sections)              | ✅       | ❌                           |
| **SemanticTextChunker**       | Split by meaning using linguistic models (spaCy, stanza, etc.)  | ✅       | ✅                           |
| **LLMBasedTextChunker**       | Use an LLM API (OpenAI, Gemini, etc.) for semantic segmentation | ❌       | ✅                           |
| **CustomTextChunker**         | Build your own chunker by extending the base class              | ✅/❌    | ✅/❌                         |

## Installation

Install only the core library:

```bash
pip install chunkipy
```

Or include optional components:

```bash
# For semantic splitting via spaCy or Stanza
pip install "chunkipy[spacy,stanza]"

# For language detection
pip install "chunkipy[langdetect]"

# Everything included
pip install "chunkipy[all]"
```

Supports `pip`, `poetry`, and `uv` package managers.

## Documentation

Full installation guide, API reference, and usage examples are available here:
👉 [https://gioelecrispo.github.io/chunkipy](https://gioelecrispo.github.io/chunkipy)

You can also explore real examples in the [examples directory](https://github.com/gioelecrispo/chunkipy/tree/main/examples).

## Contributing

Found a bug or have an idea for improvement?
Open an issue or a pull request on [GitHub](https://github.com/gioelecrispo/chunkipy/issues).

Development setup (with Poetry):

```bash
git clone https://github.com/gioelecrispo/chunkipy.git
cd chunkipy
poetry install --all-extras
```

See `CONTRIBUTING.md` for full guidelines.

## License

`chunkipy` is released under the [MIT License](https://opensource.org/license/MIT).
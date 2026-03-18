# Chunkipy

[![Python 3.10–3.13](https://img.shields.io/badge/python-3.10%20|%203.11%20|%203.12%20|%203.13-blue.svg)](#)
[![PyPI version](https://badge.fury.io/py/chunkipy.svg)](https://badge.fury.io/py/chunkipy)
[![codecov](https://codecov.io/gh/gioelecrispo/chunkipy/graph/badge.svg?token=2A7KQ87Q62)](https://codecov.io/gh/gioelecrispo/chunkipy)
[![Docs](https://img.shields.io/badge/docs-online-success)](https://gioelecrispo.github.io/chunkipy/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

`chunkipy` is a modular and extensible text chunking library for Python, built for NLP and LLM pipelines.

## Why Chunkipy?

- ✅ Lightweight core with optional extras
- ✅ Configurable overlap support via `overlap_ratio`
- ✅ Composable architecture (chunkers + splitters + size estimators + language detectors)
- ✅ Practical defaults with customizable behavior

## Quick Example

```python
from chunkipy import FixedSizeTextChunker

text = "Chunkipy makes text processing modular, flexible, and powerful!"
chunker = FixedSizeTextChunker(chunk_size=20, overlap_ratio=0.2)
chunks = chunker.chunk(text)

for i, c in enumerate(chunks):
    print(f"Chunk {i + 1}: {c}")
```

## Implemented vs Roadmap

| Status | Strategy |
| --- | --- |
| ✅ Implemented | `FixedSizeTextChunker` |
| ✅ Implemented | `RecursiveTextChunker` |
| 🚧 Roadmap | Document-based chunking |
| 🚧 Roadmap | Semantic chunker |
| 🚧 Roadmap | LLM-based chunker |

> Semantic sentence splitters and language detectors are already available and can be used today.

## Installation

Install core package:

```bash
pip install chunkipy
```

Install optional feature groups:

```bash
pip install "chunkipy[language-detection]"  # Language detection (langdetect + fasttext)
pip install "chunkipy[nlp]"                  # NLP backends (spacy + stanza)
pip install "chunkipy[ai]"                   # LLM integration (openai + tiktoken)
pip install "chunkipy[all]"                  # All optional dependencies
```

Or install individual packages:

```bash
pip install "chunkipy[spacy]"
pip install "chunkipy[stanza]"
pip install "chunkipy[langdetect]"
pip install "chunkipy[fasttext]"
pip install "chunkipy[openai]"
pip install "chunkipy[tiktoken]"
```

## Documentation

Full guides and API reference:
👉 <https://gioelecrispo.github.io/chunkipy>

Examples:
👉 <https://github.com/gioelecrispo/chunkipy/tree/main/examples>

## Contributing

Issues and pull requests are welcome:
👉 <https://github.com/gioelecrispo/chunkipy/issues>

For local setup, see `CONTRIBUTING.md`.

## License

`chunkipy` is released under the [MIT License](https://opensource.org/license/MIT).

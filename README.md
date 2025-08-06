# Chunkipy

![Python 3.8, 3.9, 3.10, 3.11, 3.12, 3.13](https://img.shields.io/badge/python-3.8%2C%203.9%2C%203.10%2C%203.11%2C%203.12%2C%203.13-blue.svg)
[![PyPI version](https://badge.fury.io/py/chunkipy.svg)](https://badge.fury.io/py/chunkipy)
[![codecov](https://codecov.io/gh/gioelecrispo/chunkipy/graph/badge.svg?token=2A7KQ87Q62)](https://codecov.io/gh/gioelecrispo/chunkipy)


`chunkipy` is an extremely useful tool for segmenting long texts into smaller chunks, based on either a character or token count. With customizable chunk sizes and splitting strategies, `chunkipy` provides flexibility and control
for various text processing tasks.

## Motivation and Features
`chunkipy` was created to address the need within the field of Natural Language Processing (NLP) to chunk text so that it does not exceed the input size of **neural networks** such as BERT, but it could be used for several other use cases.

The library offers some useful features:
- **Size estimation**: unlike other text chunking libraries, `chunkipy` offers the possibility of providing a size estimator function, in order to build the chunks taking into account the  counting function (e.g. tokenizer) that will use those chunks.
- **Split text into meaningful sentences**: in its default configuration, `chunkipy`,
  in creating the chunks, avoids cutting sentences, and always tries to have a complete and syntactically correct sentence.
  This is achieved through the use of the `stanza` library, which utilizes semantic models to cut text
  into meaningful sentences.
- **Smart Overlapping**: `chunkipy` offers the possibility to define an `overlap_percentage` and create overlapping chunks to
  preserve the context along chunks. 
- **Flexibility in choosing split strategies**: Additionally, `chunkipy` offers complete flexibility in choosing how to split, allowing users to define their own text splitting function or choose from a list of pre-defined text spliters.

## Documentation
For **Installation**, **Usage**, and **API documentation**, please refer to the [documentation](https://chunkipy.gioelecrispo.github.io).

You can also check the [examples](https://chunkipy.gioelecrispo.github.io/examples) directory for more usage scenarios.


## Usage
The main class in `chunkipy` is `TextChunker`, which takes a text and splits it into chunks of a given size.
You can use the default settings or specify custom parameters for the **chunk size**,
whether to split by **characters or tokens**, the **tokenizer function** to use (if `tokens` is set to True`), and the list of **split strategies** to apply.

Here's an example of using it to chunk text that has a number of tokens
greater than the input size of BERT:

```python
from chunkipy import TextChunker

text_chunker = TextChunker(50, tokens=True, overlap_percent=0.3)


# Generate chunks with overlapping
chunks = text_chunker.chunk(text)

# Print the resulting chunks
for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1}: {chunk}")
```

As you can see, `chunkipy` created chunks smaller than the given input size,
`512`, counted the tokens using BERT's tokenizer, and didn't cut sentences in half,
producing syntactically correct chunks of text.

You can also use `TextChunker`'s `split_text()` method to split a text into smaller parts without actually creating the chunks.
This can be useful, for example, when you want to apply further processing to
the text parts before creating the final chunks.

### Overlapping
`TextChunker` provides you with the *overlap* functionality.
The system aims to ensure that the last text parts of each segment do not exceed the maximum token limit defined for overlap. 
For example, if the `chunk_size` is set to 100 and the `overlap_percentage` is 0.1, the maximum number of overlapping tokens is 10. 
Consequently, if there are sentences or text parts that fit within this token limit, they are added at the beginning of the next segment. 
If not, they are skipped to maintain a good ratio between overlap and content. 

```python
from chunkipy import TextChunker

text_chunker = TextChunker(50, tokens=True, overlap_percent=0.3)

# Generate chunks with overlapping
chunks = text_chunker.chunk(text)

# Print the resulting chunks
for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1}: {chunk}")
```


### Provide a custom text split strategy
If you don't want to use `stanza` or you need to use your custom text splitting logic,
you can provide it in the constructor, as shown in this example:

```python
from chunkipy import TextChunker


def split_by_arrow(text):
    return [t for t in text.split("->") if t != '' and ' ']


text = "This is a tokenized text -> with custom split strategy."


# Create a TextChunker object with custom split strategy
text_chunker = TextChunker(chunk_size=8, tokens=True,
                           split_strategies=[split_by_arrow])
chunks = text_chunker.chunk(text)

# Print the resulting chunks
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}")
```

This would output:

```
Chunk 1: This is a tokenized text
Chunk 2: with custom split strategy.
```

## Contributing
If you find a bug or have a feature request, please open an issue on [GitHub](https://github.com/gioelecrispo/chunkipy/issues).
Contributions are welcome! Just fork the repository, create a new branch with your changes, and submit a pull request. Please make sure to write tests for your changes and to follow the [code style](https://www.python.org/dev/peps/pep-0008/).


### Development 
To start developing chunkipy, it is recommended to: 

1. Create a virtual environment (e.g. `python -m venv .venv`) and activate it
2. Install poetry via `pip install poetry`
3. Install the development dependencies via one of these commands:

```bash
poetry install  # no extra dependencies
poetry install --extra  spacy-splitter
poetry install --extra  openai-splitter,openai-estimator  # multiple extras dependencies
poetry install --all-extras  # all the extras dependencies
```


### Documentation
`chunkipy` relies on python docstrings and `sphinx` for its documentation.
`sphinx-autosummary` is used to automatically generate documentation from code.

`sphinx-multiversion` is used to provide multiversion support, i.e. you can navigation documention for past version too.

This is handled via Github Action, but you can reproduce it by installing the needed dependencies:

```bash
poetry install --only docs
```

and then by running the following command:
```bash
sphinx-multiversion docs/source docs/build/html
```


### Testing
We use `pytest` as main testing framework. 
You can install al the testing dependencies by running: 

```bash
poetry install --with test
```

Once done, you can run all the unit test (and check the coverage) with this command from the project folder:

```bash
pytest --cov=chunkipy --cov-report=term
```


## License
`chunkipy` is licensed under the [MIT License](https://opensource.org/licenses/MIT).

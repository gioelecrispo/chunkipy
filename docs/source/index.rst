.. Chunkipy documentation master file

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

``chunkipy`` is an extremely useful tool for segmenting long texts into smaller chunks, based on either a character or token count. With customizable chunk sizes and splitting strategies, ``chunkipy`` provides flexibility and control
for various text processing tasks.

Motivation and Features
-----------------------

`chunkipy` was created to address the need within the field of Natural Language Processing (NLP) to chunk text so that it does not exceed the input size of **neural networks** such as BERT, but it could be used for several other use cases.

The library offers some useful features:

- **Size estimation**: unlike other text chunking libraries, ``chunkipy`` offers the possibility of providing a size estimator function, in order to build the chunks taking into account the  counting function (e.g. tokenizer) that will use those chunks.
- **Split text into meaningful sentences**: as an optional configuration, ``chunkipy``, in creating the chunks, avoids cutting sentences, and always tries to have a complete and syntactically correct sentence. This is achieved through the use of the sentence segmenter libraries, that utilize semantic models to cut text into meaningful sentences.
- **Smart Overlapping**: ``chunkipy`` offers the possibility to define an ``overlap_percentage`` and create overlapping chunks to preserve the context along chunks. 
- **Flexibility for text splitters**: Additionally, ``chunkipy`` offers complete flexibility in choosing how to split, allowing users to define their own text splitting function or choose from a list of pre-defined text spliters.


.. toctree::
   :maxdepth: 2
   :caption: Contents

   installation
   usage
   api
   contributing


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
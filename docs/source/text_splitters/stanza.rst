StanzaSentenceTextSplitter
===========================

Description
-----------

``StanzaSentenceTextSplitter`` detects the input language and tokenizes the text
into sentences via Stanza pipelines. It is useful when you need robust sentence
segmentation for multilingual texts and want to plug sentence-level splits into
``RecursiveTextChunker``.

.. note::

   Install the optional dependency first:

   .. code-block:: bash

      pip install "chunkipy[stanza]"

API / Documentation
-------------------

.. autoclass:: chunkipy.text_splitters.semantic.sentences.StanzaSentenceTextSplitter
   :members:
   :no-index:

Example
-------

This example is included in ``examples/chunkers/recursive/prebuilt_stanza_text_splitter.py``.

.. literalinclude:: ../../../examples/chunkers/recursive/prebuilt_stanza_text_splitter.py
   :language: python
   :linenos:

More examples are available under ``examples/chunkers/recursive/``.


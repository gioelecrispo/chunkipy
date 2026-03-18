Spacy Sentence Text Splitter
=============================

Description
-----------

``SpacySentenceTextSplitter`` detects the text language, selects the configured
spaCy model, and splits content into sentence units for recursive chunking
pipelines. It is a semantic splitter suited for multilingual workflows where
sentence boundaries are more meaningful than punctuation-only splitting.

.. note::

   You need to install the `spacy` library and download at least one model (e.g. the English one) before using this splitter:

   .. code:: bash
   
      pip install chunkipy[spacy]
      python -m spacy download en_core_web_sm

API / Documentation
-------------------

.. autoclass:: chunkipy.text_splitters.semantic.sentences.SpacySentenceTextSplitter
   :members:
   :no-index:

Example

This example is included in ``examples/chunkers/recursive/prebuilt_spacy_text_splitter.py``.

.. literalinclude:: ../../../examples/chunkers/recursive/prebuilt_spacy_text_splitter.py
   :language: python
   :linenos:

More examples are available under ``examples/chunkers/recursive/``.
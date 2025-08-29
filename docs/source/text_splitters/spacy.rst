Spacy Sentence Text Splitter
=============================

.. note::

   You need to install the `spacy` library and download at least one model (e.g. the English one) before using this splitter:

   .. code:: bash
   
      pip install chunkipy[spacy]
      python -m spacy download en_core_web_sm


This splitter uses the spaCy library to split text into sentences. 


Documentation
-----------------

.. autoclass:: chunkipy.text_splitters.semantic.sentences.SpacySentenceTextSplitter
   :members:
   :no-index:

Example
---------

.. literalinclude:: ../../../examples/chunkers/recursive/prebuilt_spacy_text_splitter.py
   :language: python
   :linenos:
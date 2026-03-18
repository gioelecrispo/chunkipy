FixedSizeTextChunker
=======================

Description
-----------

``FixedSizeTextChunker`` splits text into deterministic chunks based on the
configured size estimator strategy. It is the most predictable chunker when you
need stable chunk boundaries and straightforward overlap behavior. By default,
it uses the word estimator and works with no optional dependencies.

API / Documentation
-------------------

.. autoclass:: chunkipy.text_chunker.FixedSizeTextChunker
   :members:
   :no-index:

Example
-------

This example is included in ``examples/chunkers/fixed_size/prebuilt_text_splitter.py``.

.. literalinclude:: ../../../examples/chunkers/fixed_size/prebuilt_text_splitter.py
   :language: python
   :linenos:

More examples are available under ``examples/chunkers/fixed_size/``.
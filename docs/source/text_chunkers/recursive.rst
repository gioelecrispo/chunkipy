RecursiveTextChunker
=======================

Description
-----------

``RecursiveTextChunker`` progressively applies text splitters from coarse to
fine granularity until each piece satisfies ``chunk_size``. It is useful when
you want chunk boundaries to follow natural separators (phrases, clauses, words)
instead of fixed windows while still preserving overlap support.

API / Documentation
-------------------

.. autoclass:: chunkipy.text_chunker.RecursiveTextChunker
   :members:
   :no-index:

Example
-------

This example is included in ``examples/chunkers/recursive/custom_text_splitter.py``.

.. literalinclude:: ../../../examples/chunkers/recursive/custom_text_splitter.py
   :language: python
   :linenos:

More examples are available under ``examples/chunkers/recursive/``.


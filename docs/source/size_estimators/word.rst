WordSizeEstimator
==================

Description
-----------

``WordSizeEstimator`` measures size by counting words and segments text at word
boundaries. It is the default estimator for chunkers and is a practical choice
for most NLP pipelines where word units are more meaningful than raw characters.
It requires no optional dependency.

API / Documentation
-------------------

.. autoclass:: chunkipy.size_estimators.WordSizeEstimator
   :members:
   :no-index:

Example
-------

This example is included in ``examples/size_estimators/word_size_estimator.py``.

.. literalinclude:: ../../../examples/size_estimators/word_size_estimator.py
   :language: python
   :linenos:


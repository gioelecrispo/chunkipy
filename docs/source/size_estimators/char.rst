CharSizeEstimator
==================

Description
-----------

``CharSizeEstimator`` measures text size using character count. It is the
simplest estimator when you want deterministic sizing independent of language
tokenization rules. It also provides character-level segmentation that works
without any external dependency.

API / Documentation
-------------------

.. autoclass:: chunkipy.size_estimators.CharSizeEstimator
   :members:
   :no-index:

Example
-------

This example is included in ``examples/size_estimators/char_size_estimator.py``.

.. literalinclude:: ../../../examples/size_estimators/char_size_estimator.py
   :language: python
   :linenos:


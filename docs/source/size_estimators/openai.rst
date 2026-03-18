OpenAI Size Estimator
=======================

Description
-----------

``OpenAISizeEstimator`` measures text size with ``tiktoken`` encodings, making
chunk boundaries closer to LLM token budgets than plain words or characters.
Use it when your downstream model has token limits and you need a more realistic
size metric for prompt construction.

.. note::

   Install the optional dependency first:

   .. code-block:: bash

      pip install "chunkipy[tiktoken]"

API / Documentation
-------------------

.. autoclass:: chunkipy.size_estimators.OpenAISizeEstimator
   :members:
   :no-index:

Example
-------

This example is included in ``examples/size_estimators/openai_size_estimator.py``.

.. literalinclude:: ../../../examples/size_estimators/openai_size_estimator.py
   :language: python
   :linenos:

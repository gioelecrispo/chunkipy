Langdetect Language Detector
================================

Description
-----------

``LangdetectLanguageDetector`` detects a language code from raw text using the
``langdetect`` package. It is a lightweight default detector for semantic
splitters and can be replaced with custom detector objects implementing the same
interface.

.. note::

   Install the optional dependency first:

   .. code-block:: bash

      pip install "chunkipy[langdetect]"

API / Documentation
-------------------

.. autoclass:: chunkipy.language_detectors.LangdetectLanguageDetector
   :members:
   :show-inheritance:
   :no-index:

Example:

This example is included in ``examples/language_detectors/langdetect_detector.py``.

.. literalinclude:: ../../../examples/language_detectors/langdetect_detector.py
   :language: python
   :linenos:

Common use cases
-----------------

- Detect the language of a text before routing it to a language-aware splitter.
- Reuse the same detector instance across multiple semantic processing steps.



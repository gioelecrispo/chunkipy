FastText Language Detector
================================

Description
-----------

``FastTextLanguageDetector`` detects language codes using a local FastText
language identification model. It is useful when you need reproducible
predictions from a specific model file and full control over model lifecycle in
production environments.

.. note::

   Install the optional dependency first:

   .. code-block:: bash

      pip install "chunkipy[fasttext]"

API / Documentation
-------------------

.. autoclass:: chunkipy.language_detectors.FastTextLanguageDetector
   :members:
   :show-inheritance:
   :no-index:

Example
-------

This example is included in ``examples/language_detectors/fasttext_detector.py``.

.. literalinclude:: ../../../examples/language_detectors/fasttext_detector.py
   :language: python
   :linenos:

Common use cases
-----------------

- Load a local FastText language ID model once and reuse it across requests.
- Use a model-based detector when you want reproducible predictions from a specific model file.

Notes
-----------------

- FastText detectors require a model file available on disk.
- The returned language code is normalized by stripping the standard ``__label__`` prefix.

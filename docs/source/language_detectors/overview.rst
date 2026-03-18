Overview
===============

.. sidebar:: Language detector classes

   - :class:`BaseLanguageDetector <chunkipy.language_detectors.BaseLanguageDetector>`
   - :class:`LangdetectLanguageDetector <chunkipy.language_detectors.LangdetectLanguageDetector>`
   - :class:`FastTextLanguageDetector <chunkipy.language_detectors.FastTextLanguageDetector>`


Chunkipy provides optional language detectors for multilingual pipelines.

These detectors are especially useful when sentence splitters or downstream
processing need to choose models based on the detected language.

All detectors follow the same base contract, so you can swap implementations
without changing splitter or chunker APIs.


Available detectors
-------------------

- ``LangdetectLanguageDetector``: lightweight detector powered by the ``langdetect`` package.
- ``FastTextLanguageDetector``: detector backed by a FastText language ID model loaded from disk.

Both implement the same base interface and can be passed into semantic
sentence splitters or used independently in your pipeline.

Custom detectors
----------------

When built-in detectors are not enough, you can create your own detector by
extending :class:`BaseLanguageDetector <chunkipy.language_detectors.BaseLanguageDetector>`
and then pass that object into language-aware splitters.

See :doc:`custom` for a minimal custom detector template.
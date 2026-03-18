Custom language detectors
=========================

Create a custom detector when built-in language detection strategies are not
enough for your pipeline or compliance constraints.

Base class
----------

Extend :class:`BaseLanguageDetector <chunkipy.language_detectors.BaseLanguageDetector>`
and implement ``detect(self, text: str) -> str``.

Minimal example
---------------

.. code-block:: python

    from chunkipy.language_detectors import BaseLanguageDetector
    from chunkipy.text_splitters.semantic.sentences import SpacySentenceTextSplitter


    class PrefixLanguageDetector(BaseLanguageDetector):
        def detect(self, text: str) -> str:
            self._validate_text(text)
            return "it" if text.strip().startswith("IT:") else "en"


    detector = PrefixLanguageDetector()
    splitter = SpacySentenceTextSplitter(language_detector=detector)

Guidelines
----------

- Return a normalized language code expected by downstream splitters.
- Validate empty input before detection.
- Keep behavior deterministic and test language edge cases explicitly.

See also
--------

- :doc:`overview`
- :doc:`../text_splitters/overview`

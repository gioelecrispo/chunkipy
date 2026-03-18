import unittest

from chunkipy.language_detectors import BaseLanguageDetector


class TestBaseLanguageDetector(unittest.TestCase):
    def test_abstract_detector_cannot_be_instantiated(self):
        class DummyLanguageDetector(BaseLanguageDetector):
            pass

        with self.assertRaises(TypeError):
            DummyLanguageDetector()

    def test_validate_text_rejects_none_and_non_string(self):
        class ConcreteDetector(BaseLanguageDetector):
            def detect(self, text: str) -> str:
                self._validate_text(text)
                return "en"

        detector = ConcreteDetector()
        with self.assertRaises(TypeError):
            detector.detect(None)
        with self.assertRaises(TypeError):
            detector.detect(123)

    def test_detect_not_implemented_branch_is_raised_when_super_called(self):
        class SuperCallingDetector(BaseLanguageDetector):
            def detect(self, text: str) -> str:
                return super().detect(text)

        with self.assertRaises(NotImplementedError):
            SuperCallingDetector().detect("text")

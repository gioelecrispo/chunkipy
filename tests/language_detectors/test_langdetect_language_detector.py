import unittest
from unittest.mock import MagicMock

from chunkipy.language_detectors import LangdetectLanguageDetector


class FakeLangdetectLanguageDetector(LangdetectLanguageDetector):
    def __init__(self, langdetect_module):
        self._test_langdetect_module = langdetect_module

    def _get_langdetect_module(self):
        return self._test_langdetect_module


class TestLangdetectLanguageDetector(unittest.TestCase):
    def test_detect_uses_injected_module(self):
        mock_langdetect = MagicMock()
        mock_langdetect.detect.return_value = "it"
        detector = FakeLangdetectLanguageDetector(langdetect_module=mock_langdetect)

        result = detector.detect("Questo testo e scritto in italiano.")

        self.assertEqual(result, "it")
        mock_langdetect.detect.assert_called_once_with("Questo testo e scritto in italiano.")

    def test_detect_rejects_empty_text(self):
        detector = FakeLangdetectLanguageDetector(langdetect_module=MagicMock())

        with self.assertRaises(ValueError):
            detector.detect("   ")

import unittest
from unittest.mock import MagicMock

from chunkipy.language_detectors import FastTextLanguageDetector


class FakeFastTextLanguageDetector(FastTextLanguageDetector):
    def __init__(self, *args, fasttext_module, **kwargs):
        self._test_fasttext_module = fasttext_module
        super().__init__(*args, **kwargs)

    def _get_fasttext_module(self):
        return self._test_fasttext_module


class TestFastTextLanguageDetector(unittest.TestCase):
    def test_init_loads_model_from_module(self):
        mock_fasttext = MagicMock()
        mock_model = MagicMock()
        mock_fasttext.load_model.return_value = mock_model

        detector = FakeFastTextLanguageDetector(
            model_path="/tmp/lid.176.bin",
            fasttext_module=mock_fasttext,
        )

        self.assertIs(detector.model, mock_model)
        mock_fasttext.load_model.assert_called_once_with("/tmp/lid.176.bin")

    def test_detect_normalizes_fasttext_label(self):
        mock_fasttext = MagicMock()
        mock_model = MagicMock()
        mock_model.predict.return_value = (["__label__en"], [0.99])
        mock_fasttext.load_model.return_value = mock_model
        detector = FakeFastTextLanguageDetector(
            model_path="/tmp/lid.176.bin",
            fasttext_module=mock_fasttext,
        )

        result = detector.detect("This text is written in English.")

        self.assertEqual(result, "en")
        mock_model.predict.assert_called_once_with("This text is written in English.", k=1)

    def test_detect_raises_when_no_labels_are_returned(self):
        mock_fasttext = MagicMock()
        mock_model = MagicMock()
        mock_model.predict.return_value = ([], [])
        mock_fasttext.load_model.return_value = mock_model
        detector = FakeFastTextLanguageDetector(
            model_path="/tmp/lid.176.bin",
            fasttext_module=mock_fasttext,
        )

        with self.assertRaises(ValueError):
            detector.detect("text")

    def test_init_rejects_invalid_model_path(self):
        with self.assertRaises(ValueError):
            FastTextLanguageDetector(model_path="")

    def test_init_rejects_invalid_label_prefix_type(self):
        with self.assertRaises(ValueError):
            FastTextLanguageDetector(model_path="/tmp/lid.176.bin", label_prefix=123)

    def test_detect_returns_label_when_prefix_does_not_match(self):
        mock_fasttext = MagicMock()
        mock_model = MagicMock()
        mock_model.predict.return_value = (["lang_en"], [0.88])
        mock_fasttext.load_model.return_value = mock_model
        detector = FakeFastTextLanguageDetector(
            model_path="/tmp/lid.176.bin",
            fasttext_module=mock_fasttext,
        )

        result = detector.detect("text")
        self.assertEqual(result, "lang_en")

import unittest
from unittest.mock import MagicMock
from chunkipy.utils import MissingDependencyError

from chunkipy.text_splitters.semantic.sentences.spacy_sentence_text_splitter import (
    SpacySentenceTextSplitter, SPACY_INSTRUCTIONS
)


class FakeSpacySentenceTextSplitter(SpacySentenceTextSplitter):
    def __init__(self, *args, spacy_dependency=None, **kwargs):
        self._spacy_dependency = spacy_dependency
        super().__init__(*args, **kwargs)

    def _get_spacy_module(self):
        return self._spacy_dependency


class TestSpacySentenceTextSplitter(unittest.TestCase):

    def setUp(self):
        self.example_text = "This is the first sentence. Here is another one!"

        # Shared fakes injected via constructor — no monkey patching needed
        self.mock_langdetect = MagicMock()
        self.mock_spacy = MagicMock()
        self.mock_model = MagicMock()
        self.mock_spacy.load.return_value = self.mock_model
        self.mock_model.select_pipes.return_value.__enter__.return_value = None
        self.mock_model.select_pipes.return_value.__exit__.return_value = None

        self.splitter = FakeSpacySentenceTextSplitter(
            language_detector=self.mock_langdetect,
            spacy_dependency=self.mock_spacy,
        )

    def test_split_calls_langdetect_and_load_model(self):
        self.mock_langdetect.detect.return_value = "en"
        self.mock_model.return_value.sents = [
            MagicMock(text="This is the first sentence."),
            MagicMock(text="Here is another one!"),
        ]

        result = self.splitter._split(self.example_text)
        self.assertEqual(result, ["This is the first sentence. ", "Here is another one! "])

    def test_load_model_unsupported_language(self):
        with self.assertLogs(level="WARNING") as caplog:
            model = self.splitter._load_model("fr")
        self.assertIn("Defaulting to 'en'", "".join(caplog.output))
        self.assertEqual(model, self.mock_model)

    def test_load_model_missing_spacy_model(self):
        self.mock_spacy.load.side_effect = OSError("Model not found")
        with self.assertRaises(MissingDependencyError) as excinfo:
            self.splitter._load_model("en")
        self.assertIn("python -m spacy download en_core_web_sm", str(excinfo.exception))

    def test_split_with_custom_models_map(self):
        models_map = {"it": "it_core_news_sm"}
        splitter = FakeSpacySentenceTextSplitter(
            models_map=models_map,
            language_detector=self.mock_langdetect,
            spacy_dependency=self.mock_spacy,
        )
        self.mock_langdetect.detect.return_value = "it"
        self.mock_model.return_value.sents = [MagicMock(text="Ciao mondo.")]

        result = splitter._split("Ciao mondo.")
        self.assertEqual(result, ["Ciao mondo. "])

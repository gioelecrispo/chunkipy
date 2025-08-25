import unittest
import pytest
from unittest.mock import patch, MagicMock
from chunkipy.utils import MissingDependencyError

from chunkipy.text_splitters.semantic.sentences.spacy_sentence_text_splitter import (
    SpacySentenceTextSplitter, SPACY_INSTRUCTIONS
)


class TestSpacySentenceTextSplitter(unittest.TestCase):

    def setUp(self):
        self.example_text = "This is the first sentence. Here is another one!"
        self.splitter = SpacySentenceTextSplitter()
        
        # Shared Mocks
        self.mock_langdetect = MagicMock()
        self.mock_spacy = MagicMock()
        self.mock_model = MagicMock()
        self.mock_spacy.load.return_value = self.mock_model
        self.mock_model.select_pipes.return_value.__enter__.return_value = None
        self.mock_model.select_pipes.return_value.__exit__.return_value = None

        # Side effect for import_dependencies
        self.import_deps_side_effect = lambda *args, **kwargs: (
            self.mock_langdetect if kwargs.get("package_name") == "langdetect"
            else self.mock_spacy
        )

    def test_split_calls_langdetect_and_load_model(self):
        with patch("chunkipy.text_splitters.semantic.sentences.spacy_sentences_text_splitter.import_dependencies") as import_deps:
            import_deps.side_effect = self.import_deps_side_effect
            
            self.mock_model.return_value.sents = [
                MagicMock(text="This is the first sentence."),
                MagicMock(text="Here is another one!")
            ]
           
        
            result = self.splitter._split(self.example_text)
            self.assertEqual(result, ["This is the first sentence. ", "Here is another one! "])

    def test_load_model_unsupported_language(self):
        with patch("chunkipy.text_splitters.semantic.sentences.spacy_sentences_text_splitter.import_dependencies") as import_deps, \
             self.assertLogs(level="WARNING") as caplog:
            import_deps.side_effect = self.import_deps_side_effect

            model = self.splitter._load_model("fr")
            self.assertIn("Defaulting to 'en'", "".join(caplog.output))
            self.assertEqual(model, self.mock_model)

    def test_load_model_missing_spacy_model(self):
        with patch("chunkipy.text_splitters.semantic.sentences.spacy_sentences_text_splitter.import_dependencies") as import_deps:
            import_deps.side_effect = self.import_deps_side_effect

            self.mock_spacy.load.side_effect = OSError("Model not found")

            with self.assertRaises(MissingDependencyError) as excinfo:
                self.splitter._load_model("en")
            self.assertIn("python -m spacy download en_core_web_sm", str(excinfo.exception))

    def test_split_with_custom_models_map(self):
        models_map = {"it": "it_core_news_sm"}
        splitter = SpacySentenceTextSplitter(models_map=models_map)
        with patch("chunkipy.text_splitters.semantic.sentences.spacy_sentences_text_splitter.import_dependencies") as import_deps:
            import_deps.side_effect = self.import_deps_side_effect
    
            self.mock_langdetect.detect.return_value = "it"
            self.mock_model.return_value.sents = [MagicMock(text="Ciao mondo.")]

            result = splitter._split("Ciao mondo.")
            self.assertEqual(result, ["Ciao mondo. "])

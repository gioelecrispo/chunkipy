from typing import Dict, List
from chunkipy.text_splitters.semantic.base_semantic_text_splitter import BaseTextSemanticSplitter
import langdetect

from chunkipy.utils import MissingDependencyError, import_dependencies

SPACY_INSTRUCTIONS = """
It seems you do not have the model installed.
Generally, it is sufficient to run

    python -m spacy download {model_name}

Check https://spacy.io/usage to see all the models available.
"""



class SpacyTextSentenceSplitter(BaseTextSemanticSplitter):
    """Sentence splitter using spaCy for semantic text splitting.
    This class uses spaCy to split text into sentences based on the language detected in the text.
    It supports multiple languages by loading different spaCy models based on the detected language.
    If the language is not supported, it defaults to English.
    
    Attributes:
        models (Dict[str, str]): A dictionary mapping language codes to spaCy model names.
        models_map (Dict[str, str]): A dictionary mapping language codes to spaCy model names.
        text_limit (int): The maximum length of text to process at once. If None, DEFAULT_LIMIT from base class is applied.    
    """
    
    DEFAULT_LANG = "en"

    def __init__(self, models_map: Dict [str, str], text_limit: int = None):
        super()._init__(text_limit)
        self.models_map = models_map
        self.models = dict()

    def _load_model(self, lang: str):
        spacy = import_dependencies(
            extra="spacy-sentence", 
            package_name="spacy"
        )

        if lang not in self.models_map:
            lang = self.DEFAULT_LANG
        if lang not in self.models:
            try:
                self.models [lang] = spacy.load(self.models_map[lang])
            except OSError as e:
                raise MissingDependencyError (SPACY_INSTRUCTIONS.format(model_name=self.models_map[lang])) from e
        return self.models [lang]


    def _split(self, text: str) -> List[str]:
        lang = langdetect.detect(text)
        sentence_tokenizer = self._load_model(lang)
        with sentence_tokenizer.select_pipes(enable=["tok2vec", "parser", "senter"]):
            doc = sentence_tokenizer(text)
        return [s.text + " " for s in doc.sents]
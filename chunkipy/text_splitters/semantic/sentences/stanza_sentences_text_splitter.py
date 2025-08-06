from typing import List
import langdetect
from chunkipy.text_splitters.semantic.base_semantic_text_splitter import BaseSemanticTextSplitter
from chunkipy.utils import import_dependencies


class StanzaSentenceTextSplitter(BaseSemanticTextSplitter):
    """Sentence splitter using Stanza for semantic text splitting.
    This class uses Stanza to split text into sentences based on the language detected in the text.
    It supports multiple languages by loading different Stanza models based on the detected language.
    
    Attributes:
        text_limit (int): The maximum length of text to process at once. If None, DEFAULT_LIMIT from base class is applied.
        
    """

    def _split(self, text: str) -> List[str]:
        _, DownloadMethod, Pipeline = import_dependencies(
            extra="sentence",
            package_name="stanza",
            attribute_names=["DownloadMethod", "Pipeline"]
        )
        lang = langdetect.detect(text)
        sentence_tokenizer = Pipeline(
            lang=lang, processors="tokenize", download_method=DownloadMethod.REUSE_RESOURCES 
        )
        return [s.text + " " for s in sentence_tokenizer(text).sentences]

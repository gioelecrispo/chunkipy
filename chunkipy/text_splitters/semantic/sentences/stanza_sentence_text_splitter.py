from typing import List
from chunkipy.text_splitters.semantic.base_semantic_text_splitter import BaseSemanticTextSplitter
from chunkipy.utils import import_dependencies


class StanzaSentenceTextSplitter(BaseSemanticTextSplitter):
    """Sentence splitter using Stanza for semantic text splitting.
    This class uses Stanza to split text into sentences based on the language detected in the text.
    It supports multiple languages by loading different Stanza models based on the detected language.
    
    Attributes:
        text_limit (int): The maximum length of text to process at once. If None, DEFAULT_LIMIT from base class is applied.
        
    """


    # Mapping from langdetect language codes to Stanza language codes
    # Note: Some languages are not supported by Stanza, so they are set to None
    # Here, the list of languages supported by langdetect (see https://pypi.org/project/langdetect/):   langdetect_languages = ['af','ar','bg','bn','ca','cs','cy','da','de','el','en','es','et','fa','fi','fr','gu','he','hi','hr','hu','id','it','ja','kn','ko','lt','lv','mk','ml','mr','ne','nl','no','pa','pl','pt','ro','ru','sk','sl','so','sq','sv','sw','ta','te','th','tl','tr','uk','ur','vi','zh-cn','zh-tw']
    # Here, the list of languages supported by stanza (invoke stanza.resources.common.list_available_languages()):       stanza_languages = ['af','ar','be','bg','bxr','ca','cop','cs','cu','da','de','el','en','es','et','eu','fa','fi','fr','fro','ga','gd','gl','got','grc','he','hi','hr','hsb','hu','hy','id','it','ja', 'kk','kmr','ko','la','lt','lv','lzh','mr','mt','nl','nn','no','olo','orv','pl','pt','ro','ru','sk','sl','sme','sr','sv','swl','ta','te','tr','ug','uk','ur','vi','wo','zh-hans','zh-hant']
    langdetect_stanza_mapping = {
        'af': 'af',         # Afrikaans
        'ar': 'ar',         # Arabic
        'bg': 'bg',         # Bulgarian
        'bn': None,         # Bengali - not supported in stanza
        'ca': 'ca',         # Catalan
        'cs': 'cs',         # Czech
        'cy': None,         # Welsh - not supported in stanza
        'da': 'da',         # Danish
        'de': 'de',         # German
        'el': 'el',         # Greek
        'en': 'en',         # English
        'es': 'es',         # Spanish
        'et': 'et',         # Estonian
        'fa': 'fa',         # Persian
        'fi': 'fi',         # Finnish
        'fr': 'fr',         # French
        'gu': None,         # Gujarati - not supported in stanza
        'he': 'he',         # Hebrew
        'hi': 'hi',         # Hindi
        'hr': 'hr',         # Croatian
        'hu': 'hu',         # Hungarian
        'id': 'id',         # Indonesian
        'it': 'it',         # Italian
        'ja': 'ja',         # Japanese
        'kn': None,         # Kannada - not supported in stanza
        'ko': 'ko',         # Korean
        'lt': 'lt',         # Lithuanian
        'lv': 'lv',         # Latvian
        'mk': None,         # Macedonian - not supported in stanza
        'ml': None,         # Malayalam - not supported in stanza
        'mr': 'mr',         # Marathi
        'ne': None,         # Nepali - not supported in stanza
        'nl': 'nl',         # Dutch
        'no': 'no',         # Norwegian (Bokmål/Nynorsk combined in langdetect)
        'pa': None,         # Punjabi - not supported in stanza
        'pl': 'pl',         # Polish
        'pt': 'pt',         # Portuguese
        'ro': 'ro',         # Romanian
        'ru': 'ru',         # Russian
        'sk': 'sk',         # Slovak
        'sl': 'sl',         # Slovenian
        'so': None,         # Somali - not supported in stanza
        'sq': None,         # Albanian - not supported in stanza
        'sv': 'sv',         # Swedish
        'sw': None,         # Swahili - not supported in stanza
        'ta': 'ta',         # Tamil
        'te': 'te',         # Telugu
        'th': None,         # Thai - not supported in stanza
        'tl': None,         # Tagalog - not supported in stanza
        'tr': 'tr',         # Turkish
        'uk': 'uk',         # Ukrainian
        'ur': 'ur',         # Urdu
        'vi': 'vi',         # Vietnamese
        'zh-cn': 'zh-hans', # Chinese (Simplified)
        'zh-tw': 'zh-hant'  # Chinese (Traditional)
    }


    def _split(self, text: str) -> List[str]:
        langdetect = import_dependencies(
            extra="langdetect", 
            package_name="langdetect"
        )
        _, DownloadMethod, Pipeline = import_dependencies(
            extra="sentence",
            package_name="stanza",
            attribute_names=["DownloadMethod", "Pipeline"]
        )
        lang = langdetect.detect(text)
        
        stanza_lang = self.langdetect_stanza_mapping.get(lang, None)
        if stanza_lang is None:
            raise ValueError(f"Language '{lang}' is not supported by Stanza for sentence splitting.")
        
        sentence_tokenizer = Pipeline(
            lang=stanza_lang, processors="tokenize", download_method=DownloadMethod.REUSE_RESOURCES
        )
        return [s.text + " " for s in sentence_tokenizer(text).sentences]

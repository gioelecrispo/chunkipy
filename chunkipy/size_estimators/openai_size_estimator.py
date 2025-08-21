from chunkipy.size_estimators.base_size_estimator import BaseSizeEstimator
from chunkipy.utils import import_dependencies


class OpenAISizeEstimator(BaseSizeEstimator):
    """
    Size estimator that uses OpenAI's tokenization to estimate the size of the text.
    """
    def __init__(self, encoding: str = "cl100k_base"):
        super().__init__()
        tiktoken = import_dependencies(extra="tiktoken", package_name="tiktoken")
        self.tokenizer = tiktoken.get_encoding(encoding)

    def estimate_size(self, text: str) -> int:
        """
        Estimate the size of the given text using OpenAI's tokenization.

        Args:
            text (str): The text to estimate the size of.

        Returns:
            int: The estimated size of the text in tokens.
        """
        return len(self.tokenizer.encode(text))
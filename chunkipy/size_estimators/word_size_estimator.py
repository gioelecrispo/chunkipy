import re
from typing import Generator
from chunkipy.size_estimators.base_size_estimator import BaseSizeEstimator


WORD_REGEX = r'\S+\s*'


class WordSizeEstimator(BaseSizeEstimator):
    """
    Size estimator that counts the number of words in the text.
    """

    def estimate_size(self, text: str) -> int:
        """
        Estimate the size of the given text by counting the number of words.

        Args:
            text (str): The text to estimate the size of.

        Returns:
            int: The estimated size of the text in words.
        """
        return sum(1 for _ in re.finditer(WORD_REGEX, text)) 
    
    def segment(self, text: str) -> Generator[str, None, None]:
        """
        Generate words from the given text using a regular expression.

        Args:
            text (str): The text to analyze.

        Yields:
            str: A segment, representing of a word for estimation.
        """
        for match in re.finditer(WORD_REGEX, text):
            yield match.group()


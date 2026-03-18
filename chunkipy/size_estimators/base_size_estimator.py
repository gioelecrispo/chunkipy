from abc import ABC, abstractmethod
from typing import Generator


class BaseSizeEstimator(ABC):
    """Base class for strategies that measure and segment text size."""

    @abstractmethod
    def estimate_size(self, text: str) -> int:
        """
        Estimate the size of the given text.

        Args:
            text (str): The text to estimate the size of.

        Returns:
            int: Estimated size in units defined by the concrete estimator.
        """
        raise NotImplementedError("Subclasses must implement the estimate_size method.")
    
    def segment(self, text: str) -> Generator[str, None, None]:
        """
        Segment the text into smaller parts for size estimation.
        This method allows dividing the text into manageable segments, which can be processed individually for size estimation purposes by downstream methods.

        Args:
            text (str): The text to be divided into smaller parts.

        Yields:
            str: A segment of the text for estimation.

        Raises:
            NotImplementedError: If a subclass does not implement this method.
        """
        raise NotImplementedError(
            "Subclasses must implement the segment method."
        )
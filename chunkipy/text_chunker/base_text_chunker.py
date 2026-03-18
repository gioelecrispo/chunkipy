from abc import ABC, abstractmethod
from chunkipy.text_chunker.data_models import Chunks
from chunkipy.size_estimators import BaseSizeEstimator, WordSizeEstimator


DEFAULT_CHUNK_SIZE = 1000  


class BaseTextChunker(ABC):
    """Base class for all chunker implementations.

    Args:
        chunk_size: Maximum size allowed for a single chunk in the units defined
            by ``size_estimator``.
        size_estimator: Strategy used to measure text size. Defaults to
            :class:`WordSizeEstimator`.
    """

    def __init__(self, chunk_size: int = None,
                size_estimator: BaseSizeEstimator = None):

        if chunk_size is not None and (not isinstance(chunk_size, int) or chunk_size <= 0):
            raise ValueError(f"chunk_size must be a positive integer. Current value: {chunk_size}")

        self.chunk_size = chunk_size if chunk_size is not None else DEFAULT_CHUNK_SIZE
        self.size_estimator = size_estimator

        if size_estimator is None:
            self.size_estimator = WordSizeEstimator()
        

    @abstractmethod
    def chunk(self, text: str) -> Chunks:
        """Chunk the provided text into ``Chunks`` objects."""
        raise NotImplementedError("Subclasses must implement chunk method.")
    
    def _validate_text(self, text: str):
        """Validate user-provided text before chunking."""
        if text is None or not isinstance(text, str):
            raise TypeError(f"Text must be a non-empty string. Text type: {type(text)}")
        if not text.strip():
            raise ValueError("Text cannot be empty or whitespace only.")

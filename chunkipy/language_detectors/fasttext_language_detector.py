from chunkipy.language_detectors.base_language_detector import BaseLanguageDetector
from chunkipy.utils import import_dependencies


class FastTextLanguageDetector(BaseLanguageDetector):
    """Detect language codes using a FastText language identification model.

    The detector expects a path to a model compatible with the FastText Python
    bindings, such as Facebook's ``lid.176.bin``.
    """

    def __init__(
        self,
        model_path: str,
        label_prefix: str = "__label__",
    ):
        """Initialize the detector and load the FastText model.

        Args:
            model_path: Path to the FastText model file.
            label_prefix: Prefix removed from FastText labels.
        """
        if not model_path or not isinstance(model_path, str):
            raise ValueError("model_path must be a valid non-empty string.")
        if not isinstance(label_prefix, str):
            raise ValueError("label_prefix must be a string.")

        self.model_path = model_path
        self.label_prefix = label_prefix
        self.model = self._get_fasttext_module().load_model(model_path)

    def _get_fasttext_module(self):
        """Return the fasttext dependency module.

        This method can be overridden by subclasses for advanced integrations.
        """
        return import_dependencies(
            extra="fasttext",
            package_name="fasttext",
        )

    def detect(self, text: str) -> str:
        """Return the top predicted FastText language code for ``text``."""
        self._validate_text(text)
        labels, _scores = self.model.predict(text, k=1)
        if not labels:
            raise ValueError("FastText did not return any language labels.")

        label = labels[0]
        if self.label_prefix and label.startswith(self.label_prefix):
            return label[len(self.label_prefix):]
        return label
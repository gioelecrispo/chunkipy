Installation
==================

You can install ``chunkipy`` in several ways, depending on your preferred environment or package manager.  
The library is lightweight at its core, with optional dependencies for specific functionalities such as language detection or advanced text splitting.

The goal is to let you install only what you really need — while still providing an easy way to install everything at once.

.. note::
   You can install optional dependencies as feature groups or individually. 
   Feature groups (e.g. ``language-detection``, ``nlp``, ``ai``) are recommended for convenience.

-------------------------------
Optional dependencies overview
-------------------------------

**Feature groups** (recommended for convenience):

- ``language-detection`` – enables both ``LangdetectLanguageDetector`` and ``FastTextLanguageDetector`` (langdetect + fasttext).
- ``nlp`` – enables semantic sentence splitters with Stanza and spaCy backends (stanza + spacy).
- ``ai`` – enables LLM integration with OpenAI and token-based size estimation (openai + tiktoken).
- ``all`` – installs all optional dependencies.

**Individual packages** (for granular control):

- ``stanza`` – enables the **StanzaSentenceTextSplitter** for sentence-level splitting using the Stanza NLP library.
- ``spacy`` – enables the **SpacySentenceTextSplitter** for sentence-level splitting using spaCy models.
- ``langdetect`` – enables the built-in ``LangdetectLanguageDetector`` (used by default in semantic splitters).
- ``fasttext`` – enables the ``FastTextLanguageDetector`` for FastText model-based language identification.
- ``openai`` – enables the **OpenAISizeEstimator** for OpenAI-compatible token counting.
- ``tiktoken`` – enables **token-based size estimation** using OpenAI’s tokenizer.  

--------------------------------
Install using pip
--------------------------------

You can install ``chunkipy`` directly from PyPI using pip.

.. tab:: Core installation

    Installs only the core library (no optional dependencies).

    .. code-block:: bash

        pip install chunkipy

.. tab:: Feature groups (recommended)

    Install feature groups for common use cases.

    .. code-block:: bash

        pip install "chunkipy[language-detection]"  # Language detection
        pip install "chunkipy[nlp]"                  # NLP backends
        pip install "chunkipy[ai]"                   # LLM integration
        pip install "chunkipy[all]"                  # Everything

.. tab:: Individual packages

    Installs ``chunkipy`` with specific optional dependencies.

    .. code-block:: bash

        pip install "chunkipy[spacy,langdetect]"
        pip install "chunkipy[stanza,fasttext]"

.. tab:: Custom combinations

    Mix and match feature groups and individual packages.

    .. code-block:: bash

        pip install "chunkipy[nlp,language-detection,openai]"


--------------------------------
Install using Poetry
--------------------------------

If you use ``poetry`` for dependency management, you can add ``chunkipy`` with extras directly to your project.

.. tab:: Core installation

    .. code-block:: bash

        poetry add chunkipy

.. tab:: Feature groups (recommended)

    .. code-block:: bash

        poetry add chunkipy[language-detection]
        poetry add chunkipy[nlp]
        poetry add chunkipy[ai]
        poetry add chunkipy[all]

.. tab:: Individual packages

    .. code-block:: bash

        poetry add chunkipy[spacy,langdetect]

.. tab:: Custom combinations

    .. code-block:: bash

        poetry add "chunkipy[nlp,language-detection]"


--------------------------------
Install using uv
--------------------------------

``uv`` is a fast Python package manager designed for modern workflows.  
It fully supports PEP 621-style extras and can dramatically speed up installations.

.. tab:: Core installation

    .. code-block:: bash

        uv add chunkipy

.. tab:: Feature groups (recommended)

    .. code-block:: bash

        uv add chunkipy[language-detection]
        uv add chunkipy[nlp]
        uv add chunkipy[ai]

.. tab:: All extras

    .. code-block:: bash

        uv add chunkipy[all]


-----------------------------------------------
Install using pipx (for CLI or isolated usage)
-----------------------------------------------

If you want to experiment with ``chunkipy`` in isolation, or use it in a CLI-style environment without polluting your main environment:

.. code-block:: bash

    pipx install "chunkipy[spacy,stanza,langdetect,fasttext,openai,tiktoken]"

This installs ``chunkipy`` in a virtual environment managed by ``pipx`` — great for trying it out quickly or keeping your global environment clean.


--------------------------------
Verification
--------------------------------

Once installed, you can verify imports:

.. code-block:: python

    import chunkipy
    from chunkipy import FixedSizeTextChunker, RecursiveTextChunker

    print("Chunkipy import OK")


--------------------------------
Next steps
--------------------------------

- 📘 Continue to the :doc:`quickstart` section to see how to start chunking text.  
- ⚙️ Check the :doc:`api` reference for all available classes and configuration options.  
- 🤝 Explore the :doc:`contributing` guide to learn how to contribute to the project.
- 🔍 Explore :doc:`size_estimators/overview` to learn about different size estimation methods.
- 🧩 Explore :doc:`text_chunkers/overview` to learn about the different chunking strategies.
- ✂️ Explore :doc:`text_splitters/overview` to learn about the different text splitting options.  
- 🌍 Explore :doc:`language_detectors/overview` to learn about the available language detector APIs.
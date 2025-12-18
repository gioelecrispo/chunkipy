Installation
==================

You can install ``chunkipy`` in several ways, depending on your preferred environment or package manager.  
The library is lightweight at its core, with optional dependencies for specific functionalities such as language detection or advanced text splitting.

The goal is to let you install only what you really need — while still providing an easy way to install everything at once.

.. note::
   You can install multiple optional dependencies together by separating them with commas, e.g. ``chunkipy[spacy,langdetect]``.

--------------------------------
List of optional dependencies
--------------------------------

- ``stanza`` – enables the **StanzaSplitter** for sentence-level splitting using the *Stanza* NLP library.  
- ``spacy`` – enables the **SpacySplitter** for sentence-level splitting using *spaCy* models.  
- ``langdetect`` – adds a **language detector** useful for language-dependent splitters.  
- ``tiktoken`` – enables **token-based size estimation** using OpenAI’s tokenizer.  

--------------------------------
Install using pip
--------------------------------

You can install ``chunkipy`` directly from PyPI using pip.

.. tab:: Core installation

    Installs only the core library (no optional dependencies).

    .. code-block:: bash

        pip install chunkipy

.. tab:: Single extra dependency

    Installs the core library with an additional dependency (e.g. Stanza for text splitting).

    .. code-block:: bash

        pip install chunkipy[stanza]

.. tab:: Multiple extra dependencies

    Installs ``chunkipy`` with multiple optional components.

    .. code-block:: bash

        pip install chunkipy[spacy,langdetect,tiktoken]

.. tab:: All optional dependencies

    Installs everything — suitable for full NLP setups or development environments.

    .. code-block:: bash

        pip install chunkipy[all]


--------------------------------
Install using Poetry
--------------------------------

If you use ``poetry`` for dependency management, you can add ``chunkipy`` with extras directly to your project.

.. tab:: Core installation

    .. code-block:: bash

        poetry add chunkipy

.. tab:: Single extra dependency

    .. code-block:: bash

        poetry add chunkipy[stanza]

.. tab:: Multiple extra dependencies

    .. code-block:: bash

        poetry add chunkipy[spacy,langdetect,tiktoken]

.. tab:: All optional dependencies

    .. code-block:: bash

        poetry add chunkipy[all]


--------------------------------
Install using uv
--------------------------------

``uv`` is a fast Python package manager designed for modern workflows.  
It fully supports PEP 621-style extras and can dramatically speed up installations.

.. tab:: Core installation

    .. code-block:: bash

        uv add chunkipy

.. tab:: With optional extras

    .. code-block:: bash

        uv add chunkipy[spacy,langdetect]

.. tab:: All extras

    .. code-block:: bash

        uv add chunkipy[all]


--------------------------------
Install using pipx (for CLI or isolated usage)
--------------------------------

If you want to experiment with ``chunkipy`` in isolation, or use it in a CLI-style environment without polluting your main environment:

.. code-block:: bash

    pipx install "chunkipy[all]"

This installs ``chunkipy`` in a virtual environment managed by ``pipx`` — great for trying it out quickly or keeping your global environment clean.


--------------------------------
Verification
--------------------------------

Once installed, you can verify the installation and version:

.. code-block:: bash

    python -m chunkipy --version

Or, if you’re in a Python shell:

.. code-block:: python

    import chunkipy
    print(chunkipy.__version__)


--------------------------------
Next steps
--------------------------------

- 📘 Continue to the :doc:`quickstart` section to see how to start chunking text.  
- ⚙️ Check the :doc:`api` reference for all available classes and configuration options.  
- 🤝 Explore the :doc:`contributing` guide to learn how to contribute to the project.
- 🔍 Explore :doc:`size_estimators/overview` to learn about different size estimation methods.
- 🧩 Explore :doc:`text_chunkers/overview` to learn about the different chunking strategies.
- ✂️ Explore :doc:`text_splitters/overview` to learn about the different text splitting options.  
- 🌍 Explore :doc:`language/overview` to learn about language detection options.
import os
import sys
import importlib.metadata

# -- Project information --
project = "Chunkipy"
package_name = "chunkipy"
source_folder = "chunkipy"
copyright = "2023, Gioele Crispo"
author = "Gioele Crispo"
release = version = importlib.metadata.version(package_name)  # Dynamically use the version
version = release.split(".")[0] # Use major version if desired

# Add project directory to sys.path for autodoc
sys.path.insert(0, os.path.abspath(f"../../{source_folder}"))

# Sphinx configuration
extensions = [
    "sphinx.ext.autodoc",  # For auto-generating documentation from docstrings
    "sphinx.ext.napoleon",  # For Google/NumPy docstring support
    "sphinx_autodoc_typehints",  # Automatic type hinting
    "sphinx.ext.viewcode",  # Add links to source code
    "sphinx_multiversion",  # Enable versioning
    "sphinx.ext.autosummary",  # Auto-generate summary tables for modules/classes
    "sphinx.ext.intersphinx",  # Cross reference library documentation
]

templates_path = ["_templates"]
exclude_patterns = []

#-- HTML Theme Settings --
html_theme = "sphinx_rtd_theme"  # Use Read the Docs Theme
html_theme_options = {
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'flyout_display': 'hidden',
    'version_selector': True,
    'language_selector': True,
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

html_static_path = ["_static"]
html_css_files = [
    "css/style.css",
]

# -- Autodoc Settings --
autodoc_typehints = "description"  # Render type hints in docstrings

autodoc_default_options = {
    "members": True,  # Include class/module members
    "undoc-members": True,  # Include undocumented members
    "show-inheritance": True,  # Show class inheritance
}

autosummary_generate = True  # Enable autosummary generation

#-- Cross reference Documentation Settings
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "stanza": ("https://stanfordnlp.github.io/stanza", None),
    "spacy": ("https://spacy.io/", None),
}

#-- Multiversion Settings
smv_tag_whitelist = (
    r"^v\d+\.\d+\.\d+" # Include only tags like v1.0.0, v2.1.3
)
#smv_branch_whitelist = r"^main$" # Include only the main branch
#smv_remote_whitelist = r"^origin$" # Use the origin repository by default
smv_released_pattern = r"^refs/tags/.*$" # r"^refs/tags/v\d+\.\d+.\d+$"
smv_outputdir_format = "{ref.name}"


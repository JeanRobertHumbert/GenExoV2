# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))  # Adapte selon l’arborescence de ton projet

project = 'GenExoV2'
copyright = '2025, Jean-Robert Humbert'
author = 'Jean-Robert Humbert'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',       # Génération automatique à partir des docstrings
    'sphinx.ext.napoleon',      # Support du style Google / NumPy pour les docstrings
    'sphinx.ext.viewcode',      # Ajoute des liens vers le code source
    'sphinx.ext.todo',          # Gestion des TODOs
    
]

# -- Options for autodoc -----------------------------------------------------

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'special-members': '__add__,__sub__,__mul__,__truediv__,__eq__,__neg__,__repr__,__str__',
    'show-inheritance': True
}
autodoc_mock_imports = [
    'matplotlib',
    'mpl_toolkits.mplot3d',
    'sklearn',
    'numpy',
]
autodoc_typehints = 'description'
pygments_style = "friendly"
# Napoleon settings (pour un rendu propre des docstrings Google/Numpy)
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_param = True
napoleon_use_rtype = True


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

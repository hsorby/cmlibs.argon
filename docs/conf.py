# Configuration file for the Sphinx documentation builder.
import os
import sys

here = os.path.dirname(__file__)

# -- Project information

project = 'CMLibs Argon'
copyright = '2022, University of Auckland'
author = 'University of Auckland'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'nature'

# -- Options for EPUB output
epub_show_urls = 'footnote'


sys.path.append(os.path.join(here, 'mock'))
sys.path.append(os.path.join(here, '..', 'src'))

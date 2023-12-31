# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.append(os.path.abspath("../../"))
# sys.path.append(os.path.abspath("../../deepdrr"))


# -- Project information -----------------------------------------------------

project = "DeepDRR函数调用文档"
copyright = "自用"
author = "无"

# The full version, including alpha/beta/rc tags
release = "1.1.0a3"

# -- General configuration ---------------------------------------------------
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    'sphinx.ext.viewcode',
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "sphinxcontrib.httpdomain",
    "sphinxcontrib.autohttp.flask",
    "sphinxcontrib.autohttp.flaskqref",
    "recommonmark",
    "sphinx_copybutton",
    'rst2pdf.pdfbuilder'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

pdf_documents = [
  ('index', u'deepdrr', u'deepdrr', u'deepdrr'),
]
pdf_stylesheets = ['aA','zh_CN']
pdf_font_path = ['C:\\Windows\\Fonts']
pdf_language = "zh_CN"

pdf_fit_mode = "shrink"
pdf_use_index = False
pdf_use_toc = False
pdf_toc_depth = 1
pdf_use_numbered_links = False
pdf_fit_background_mode = 'scale'
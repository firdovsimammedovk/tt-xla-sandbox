# SPDX-FileCopyrightText: © 2026 Tenstorrent AI ULC
#
# SPDX-License-Identifier: Apache-2.0

# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import subprocess
import sys

sys.path.insert(0, os.path.abspath("."))

# -- Project information -----------------------------------------------------

project = "TT-XLA"
copyright = "Tenstorrent"
author = "Tenstorrent"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.email",
    "sphinx_sitemap",
    "myst_parser",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

myst_heading_anchors = 3

# Napoleon settings (NumPy-style)
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_attr_annotations = True

email_automode = True

intersphinx_mapping = {
    "tt-metalium": ("https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/", None),
    "ttnn": ("https://docs.tenstorrent.com/tt-metal/latest/ttnn/", None),
}

templates_path = ["_templates"]
exclude_patterns = []

# -- Versioning --------------------------------------------------------------

def _git_tags():
    try:
        out = subprocess.check_output(
            ["git", "tag", "-l", "v*", "--sort=-version:refname"],
            stderr=subprocess.DEVNULL,
        ).decode().strip()
        return [t for t in out.split("\n") if t]
    except Exception:
        return []

_XLA_BASE = "https://firdovsimammedovk.github.io/tt-xla-sandbox/"
_current_version = os.environ.get("DOCS_VERSION", "latest")
_all_versions = ["latest"] + [t for t in _git_tags() if t != "latest"]
_version_urls = [(v, f"{_XLA_BASE}{v}/") for v in _all_versions]

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": True,
    "titles_only": True,
    "navigation_depth": 2,
}
html_logo = "_static/tt_logo.svg"
html_favicon = "_static/favicon.png"
html_static_path = ["_static"]
html_css_files = ["https://firdovsimammedovk.github.io/tenstorrent-sandbox/_static/tt_theme.css"]
html_baseurl = f"{_XLA_BASE}{_current_version}/"
html_last_updated_fmt = "%b %d, %Y"

sitemap_locales = [None]
sitemap_url_scheme = "{link}"

html_context = {
    "versions": _version_urls,
    "current_version": _current_version,
    "logo_link_url": "https://firdovsimammedovk.github.io/tenstorrent-sandbox/",
    "search_site_base_url": _XLA_BASE,
}

version = _current_version

"""Sphinx configuration for the PyChord documentation."""

import sys
import tomllib
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

try:
    release = version("pychord")
except PackageNotFoundError:
    with (ROOT / "pyproject.toml").open("rb") as f:
        release = tomllib.load(f)["project"]["version"]

project = "PyChord"
author = "Yuma Mihira"
copyright = f"2016 - 2026, {author}"
version = ".".join(release.split(".")[:2])

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
]

language = "en"
exclude_patterns = ["_build", "html", "Thumbs.db", ".DS_Store"]

autodoc_typehints = "description"
autodoc_member_order = "bysource"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

html_theme = "sphinx_rtd_theme"

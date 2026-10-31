# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

PyChord is a pure-Python library (no runtime dependencies) for handling musical chords: parsing chord names, transposing, listing component notes, comparing chords, finding chords from notes, and managing chord progressions. Supports Python 3.11+.

## Commands

These mirror the CI workflow (`.github/workflows/build.yml`), which runs on Python 3.11–3.15. Dev tools are declared as PEP 735 dependency groups in `pyproject.toml` (requires pip >= 25.1):

```sh
# Install the package in editable mode with test + lint tools
pip install -e . --group dev

# Run all tests with coverage (line + branch coverage must stay at 100%, enforced via fail_under in pyproject.toml)
coverage run -m unittest -v
coverage report

# Run a single test module / class / method
python -m unittest test.test_chord
python -m unittest test.test_chord.TestChordCreations
python -m unittest test.test_chord.TestChordCreations.test_chord_creation

# Lint, formatting check (ruff) and strict type check (mypy strict = true)
ruff check pychord test examples
ruff format --check pychord test examples
mypy pychord

# Build sdist/wheel and validate metadata
python -m build
twine check --strict dist/*

# Build Sphinx docs (published on Read the Docs from docs/conf.py)
make -C docs html
```

Tests use the stdlib `unittest` framework (not pytest), typically with `self.subTest` for table-driven cases.

## Architecture

Public API is exported from `pychord/__init__.py`: `Chord`, `ChordProgression`, `Quality`, `QualityManager`, `find_chords_from_notes`.

- **Notes are strings, pitches are ints 0–11.** `utils.note_to_val` converts a note name (with any number of `b`/`#`) to a pitch class; `augment`/`diminish` add or remove accidentals on a name. Note spelling is preserved where possible rather than normalized.
- **Qualities are defined by interval strings**, not semitone lists. `constants/qualities.py` holds `DEFAULT_QUALITIES` as `(name, ("1", "b3", "5", ...))` tuples. `Quality.components` derives semitone offsets from these intervals (`quality._get_interval_pitch`), and `Quality.get_components(visible=True)` derives correctly-spelled note names via `scale_notes(root, "maj")`. Adding a chord type means adding an entry to `DEFAULT_QUALITIES` (multiple aliases like `"m"`, `"min"`, `"-"` are separate entries).
- **`QualityManager` is a process-wide singleton** (via `__new__`). Do not import `DEFAULT_QUALITIES` directly elsewhere; go through `QualityManager`. `get_quality` returns a deep copy (and applies inversions by rotating intervals up an octave), so mutating the manager via `set_quality` does not affect existing `Chord` instances. Tests that call `set_quality` must restore defaults (`load_default_qualities`) to avoid leaking state.
- **Parsing flow:** `Chord(name)` → `parser.parse` splits the string into root (up to two accidentals), optional inversion (`/<digit>`), quality string, and optional slash bass note (`/<note>`), then looks up the quality in `QualityManager`. Unknown qualities raise `ValueError`.
- **Scales:** `constants/scales.py` contains `NOTE_VALUES`, sharp/flat spelling tables (`SCALE_VAL_DICT`, used by `transpose_note` to choose spelling), and `RELATIVE_KEY_DICT` (mode → semitone offsets) used by `scale_notes` and `Chord.from_note_index`. Scale strings are `<root><mode>` with a 3-letter mode, e.g. `"Cmaj"`, `"Ebmin"`.
- **`analyzer.find_chords_from_notes`** tries every rotation of the input notes, converts each to ascending semitone positions, and asks `QualityManager.find_quality_from_components` for a match; non-root rotations become slash chords over the original bass note.
- **`ChordProgression`** is a thin list wrapper around `Chord` objects (accepts strings or `Chord`s) with transpose/append/indexing.

## Conventions

- The package ships `py.typed` and is checked with `mypy --strict`; keep full type annotations (overloads are used where return type depends on a `Literal` flag, e.g. `visible`).
- Docstrings use Sphinx reST field lists (`:param x:`) since `docs/pychord.rst` autodocs the public API.
- Releases: run the "Prepare release" workflow (`.github/workflows/prepare-release.yml`, choose patch/minor/major) to open a "Bump version to vX.Y.Z" PR. Merging it triggers `.github/workflows/release.yml`, which creates the `vX.Y.Z` tag and GitHub release (auto-generated notes) and publishes to PyPI via the reusable `.github/workflows/deploy.yml`. Manually pushing a `v*` tag still triggers `deploy.yml` directly.

![PyChord](https://github.com/yuma-m/pychord/raw/main/pychord.png)

# PyChord

[![PyPI](https://img.shields.io/pypi/v/pychord)](https://pypi.org/project/pychord/)
[![Python versions](https://img.shields.io/pypi/pyversions/pychord)](https://pypi.org/project/pychord/)
[![Build Status](https://github.com/yuma-m/pychord/actions/workflows/build.yml/badge.svg)](https://github.com/yuma-m/pychord/actions/workflows/build.yml)
[![Documentation Status](https://readthedocs.org/projects/pychord/badge/?version=latest)](https://pychord.readthedocs.io/en/latest/?badge=latest)
[![License: MIT](https://img.shields.io/pypi/l/pychord)](./LICENSE)

## Overview

PyChord is a pure-Python library for working with musical chords. It parses chord names,
lists component notes, transposes chords and progressions, and finds chords from a set of notes.

## Installation

PyChord supports Python 3.11 and above.

```sh
$ pip install pychord
```

## Basic Usage

### Create a chord

```python
>>> from pychord import Chord
>>> c = Chord("Am7")
>>> c
<Chord: Am7>
>>> c = Chord("Am7/G")
>>> c.root, str(c.quality), c.on
('A', 'm7', 'G')
```

Unknown chord names raise `ValueError`:

```python
>>> Chord("Cfoo")
Traceback (most recent call last):
  ...
ValueError: Unknown quality: foo
```

### Transpose a chord

```python
>>> c = Chord("Am7/G")
>>> c.transpose(3)
>>> c
<Chord: Cm7/Bb>
```

Pass a key as the second argument to control whether sharps or flats are used:

```python
>>> c = Chord("C")
>>> c.transpose(1)
>>> c
<Chord: Db>
>>> c = Chord("C")
>>> c.transpose(1, "D")
>>> c
<Chord: C#>
```

### Get component notes

```python
>>> c = Chord("Am7")
>>> c.components()
['A', 'C', 'E', 'G']
>>> c.components_with_pitch(root_pitch=3)
['A3', 'C4', 'E4', 'G4']
>>> c.components(visible=False)  # semitones from C
[9, 12, 16, 19]
```

### Compare chords

```python
>>> Chord("C") == Chord("D")
False
>>> Chord("C#") == Chord("Db")
True
```

### Find chords from notes

```python
>>> from pychord import find_chords_from_notes
>>> find_chords_from_notes(["C", "E", "G"])
[<Chord: C>]
>>> find_chords_from_notes(["F#", "A", "C", "D"])
[<Chord: D7/F#>]
>>> find_chords_from_notes(["F", "G", "C"])
[<Chord: Fsus2>, <Chord: Csus4/F>]
```

### Chord progressions

```python
>>> from pychord import ChordProgression
>>> cp = ChordProgression(["C", "G/B", "Am"])
>>> cp
<ChordProgression: C | G/B | Am>

>>> cp.append("Em/G")
>>> cp
<ChordProgression: C | G/B | Am | Em/G>

>>> cp.transpose(+3)
>>> cp
<ChordProgression: Eb | Bb/D | Cm | Gm/Bb>

>>> cp[1]
<Chord: Bb/D>
>>> len(cp)
4

>>> cp.insert(1, "Fm")
>>> cp.pop()
<Chord: Gm/Bb>
>>> cp + ChordProgression(["Fm", "Bb7"])
<ChordProgression: Eb | Fm | Bb/D | Cm | Fm | Bb7>
```

## Advanced Usage

### Create a chord from a scale degree

```python
>>> Chord.from_note_index(note=1, quality="", scale="Cmaj")  # I of C major
<Chord: C>
>>> Chord.from_note_index(note=3, quality="m7", scale="Fmaj")  # IIIm7 of F major
<Chord: Am7>
>>> Chord.from_note_index(note=5, quality="7", scale="Amin")  # V7 of A minor
<Chord: E7>
```

### Supported and custom chord qualities

All built-in qualities are defined in [`pychord/constants/qualities.py`](./pychord/constants/qualities.py)
and can be listed with `QualityManager().get_qualities()`.

You can add a new quality or override an existing one. The change applies process-wide
to chords created afterwards; call `load_default_qualities()` to restore the defaults.

```python
>>> from pychord import Chord, QualityManager
>>> Chord("C11").components()
['C', 'E', 'G', 'Bb', 'D', 'F']

>>> quality_manager = QualityManager()
>>> quality_manager.set_quality("11", ("1", "3", "5", "b7", "11"))
>>> Chord("C11").components()
['C', 'E', 'G', 'Bb', 'F']

>>> quality_manager.load_default_qualities()
```

### Inversions

Append `/N` to a chord name for its Nth inversion. You can also add a bass note after another slash:

```python
>>> Chord("C/1").components() # First inversion of C
['E', 'G', 'C']
>>> Chord("C/2").components() # Second inversion of C
['G', 'C', 'E']

>>> Chord("Cm7/3/F").components() # Third inversion of Cm7 over F
['F', 'Bb', 'C', 'Eb', 'G']
```

## Examples

- [pychord-midi.py](./examples/pychord-midi.py) - Create a MIDI file using PyChord and pretty_midi.

## Development

Development tools are declared as [dependency groups](https://packaging.python.org/en/latest/specifications/dependency-groups/) in `pyproject.toml` (requires pip 25.1 or later).

```sh
$ pip install -e . --group dev

# Run tests with coverage
$ coverage run -m unittest -v && coverage report

# Lint, format and type check
$ ruff check pychord test examples
$ ruff format --check pychord test examples
$ mypy pychord

# Build the documentation
$ pip install -r docs/requirements.txt
$ make -C docs html
```

## Links

- [PyPI](https://pypi.org/project/pychord/)
- [GitHub](https://github.com/yuma-m/pychord)
- [Documentation](https://pychord.readthedocs.io/en/latest/)

## Author

- [Yuma Mihira](https://yuma.cloud/)

## License

- MIT License

The logo is made from [Freepik](https://www.flaticon.com/authors/freepik).

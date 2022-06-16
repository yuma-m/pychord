![PyChord](./pychord.png)

# PyChord ![Build Status](https://github.com/yuma-m/pychord/actions/workflows/build.yml/badge.svg) [![Documentation Status](https://readthedocs.org/projects/pychord/badge/?version=latest)](http://pychord.readthedocs.io/en/latest/?badge=latest)

## Overview

Pychord is a python library to handle musical chords.

## Installation

```sh
$ pip install pychord
```

## Basic Usage

### Create a Chord

```python
>>> from pychord import Chord
>>> c = Chord("Am7")
>>> c
<Chord: Am7>
>>> c.info()
"""
Am7
root=A
quality=m7
appended=[]
on=None
"""
```

### Transpose a Chord

```python
>>> c = Chord("Am7/G")
>>> c.transpose(3)
>>> c
<Chord: Cm7/Bb>
```

### Get component notes

```python
>>> c = Chord("Am7")
>>> c.components()
['A', 'C', 'E', 'G']
>>> c.components_with_pitch(root_pitch=3)
['A3', 'C4', 'E4', 'G4']
```

### Compare Chords

```python
>>> Chord("C") == Chord("D")
False
>>> Chord("C#") == Chord("Db")
True
>>> c = Chord("C")
>>> c.transpose(2)
>>> c == Chord("D")
True
```

### Find Chords from notes

```python
>>> from pychord import find_chords_from_notes
>>> find_chords_from_notes(["C", "E", "G"])
[ <Chord: C>]
>>> find_chords_from_notes(["F#", "A", "C", "D"])
[ <Chord: D7/F#>]
>>> find_chords_from_notes(["F", "G", "C"])
[ <Chord: Fsus2>, <Chord: Csus4/F>]
```

### Create and handle chord progressions

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
```

## Advanced Usage

### Create a Chord from note index in a scale

```python
>>> Chord.from_note_index(note=1, quality="", scale="Cmaj")
<Chord: C>  # I of C major
>>> Chord.from_note_index(note=3, quality="m7", scale="Fmaj")
<Chord: Am7>  # IIIm7 of F major
>>> Chord.from_note_index(note=5, quality="7", scale="Amin")
<Chord: E7>  # V7 of A minor
```

### Overwrite the default Quality components with yours

```python
>>> from pychord import Chord, QualityManager
>>> Chord("C11").components()
['C', 'G', 'Bb', 'D', 'F']

>>> quality_manager = QualityManager()
>>> quality_manager.set_quality("11", (0, 4, 7, 10, 14, 17))
>>> Chord("C11").components()
['C', 'E', 'G', 'Bb', 'D', 'F']
```

### Inversions

Chord inversions are created with a forward slash and a number
indicating the order. This can optionally be combined with an
additional forward slash to change the bass note:

```python
>>> Chord("C/1").components() # First inversion of C
['E', 'G', 'C']
>>> Chord("C/2").components() # Second inversion of C
['G', 'C', 'E']

>>> Chord("Cm7/3/F").components() # Third inversion of Cm7 with an added F bass
['F', 'Bb', 'C', 'Eb', 'G']
```

## Examples

- [pychord-midi.py](./examples/pychord-midi.py) - Create a MIDI file using PyChord and pretty_midi.

## Supported Python Versions

- 3.6 and above

Python 2.7 and 3.5 compatibility was dropped from version 1.0.0.

## Links

- PyPI: https://pypi.python.org/pypi/pychord
- GitHub: https://github.com/yuma-m/pychord
- Documentation: http://pychord.readthedocs.io/en/latest/

## Author

- [Yuma Mihira](https://yuma.cloud/)

## License

- MIT License

Icon is made by [Freepik](https://www.flaticon.com/authors/freepik).

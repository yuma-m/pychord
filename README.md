# pychord

[![Build Status](https://travis-ci.org/yuma-m/pychord.svg?branch=master)](https://travis-ci.org/yuma-m/pychord)

## Overview

Pychord is a python library to handle musical chords.

## Installation

```sh
$ pip install pychord
```

## Usage

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
```

### Create chord progressions

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
```

## Supported Python Versions
- 2.7
- 3.3 and above

## Links
- PyPI: https://pypi.python.org/pypi/pychord
- GitHub: https://github.com/yuma-m/pychord

## License

- MIT License

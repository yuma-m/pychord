## Forthcoming

## v0.4.1
- Add qualities.
    - `sus`, `maj7`, `maj9`, `m6`, `madd9`
    - `7b5`, `7#5`, `7b9`, `7#9`
    - `9-5`, `9b5`, `9+5`, `9#5`
    - `7#9b5`, `7#9#5`, `7b9b5`, `7b9#5`, `7#11`, `7b9#9`, `7b9#11`, `7#9#11`, `7b13`
    - `7b9b13`, `9+11`, `9#11`, `13-9`, `13b9`, `13+9`, `13#9`, `13+11`, `13#11`
- Support quality alias comparison.
    - `maj7 == M7`

## v0.4.0
- Add Chord.from_note_index method.
    - Support chord creation using note index in a scale.
- Contributor: @kwadwo00

## v0.3.2
- Make `QUALITY_DICT` values immutable.

## v0.3.1
- Raise TypeError in `__eq__` methods.

## v0.3.0
- Implement `__eq__` method for Quality.
- Fix `__eq__` method of Chord to support comparison between sharped and flatted chords.

## v0.2.9
- Implement `__eq__`, `__ne__`, `__setitem__` methods for ChordProgression.
- Implement `__eq__` method for Chord.

## v0.2.7
- Handle base note in Chord.components
- Contributor: @mstuttgart

## v0.2.6
- Enable setting scale on Chord.transpose
- Contributor: @jgvictores

## v0.2.5
- Refactor some classes not to modify instance variables.
- Update docstrings.

## v0.2.3
- Support 5th(power) chord.
- Add a utility to find chords from notes.

## v0.2.2
- Implement `__repr__` function.

## v0.2.1
- Support `__add__`, `__len__` and `__getitem__` functions in ChordProgression class.

## v0.2.0
- Add a class to handle chord progressions.

## v0.1.1
- Display flat or sharp by the scale.

## v0.1.0
- Add a function to get component notes of chord.

## Forthcoming

## v1.2.2

- Add tests for "M" and "maj" qualities synonyms
- Add missing synonyms for M qualities
- Contributor: @nickurak

## v1.2.1

- Add `get_qualities` method to `QualityManager`.
- Contributor: @nickurak

## v1.2.0

- Add `chromatic` parameter for `from_note_index`.
- Add `7(b9)`, `6b5` qualities.
- Contributor: @Moustov, @hejops

## v1.1.1

- Add `m11` and `maj13` qualities.
- Fix TypeError.
- Contributor: @Moustov

## v1.1.0

- Add `no5`, `m(no5)`, `(b5)`, `sus4add2` and `sus4add9` qualities.
- Support inversions.
- Contributor: @EnigmaCurry

## v1.0.0

- Drop compatibility for Python 2.7 and 3.5.
- Refactor whole library to optimize for Python 3.x.
  - Add type hints.
  - Use f-strings.
  - Rename `note_to_chord` to `find_chords_from_notes`.
  - Use tuple instead of list for `Quality.components`.

## v0.6.3

- Add modes to `RELATIVE_KEY_DICT`.
- Add `diatonic` option for `from_note_index`.
- Contributor: @hejops

## v0.6.2

- Add `add4`, `add11` and `add13` quality variations.
- Contributor: @philipmat

## v0.6.1

- Fix `dim6` to `dim7`.
- Add `M7+11` and `m7+5` qualities.

## v0.6.0

- Add an example to create a MIDI file.
- Add `QualityManager` class to overwrite default qualities.
  - Do not import `QUALITY_DICT` from modules other than quality.
- Fix `sus` quality.

## v0.5.1

- Add `m7b9b5` quality.

## v0.5.0

- Add Chord.components_with_pitch method.

## v0.4.2

- Rename `6/9` to `69`.
- Add `m69`, `m7b5` and `-` qualities.
- Contributor: @dok

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

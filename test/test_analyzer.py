import unittest

from parameterized import parameterized

from pychord import Chord
from pychord.analyzer import (
    get_all_rotated_notes,
    find_chords_from_notes,
    notes_to_positions,
)


class TestNotesToPositions(unittest.TestCase):

    @parameterized.expand(
        [
            (["C"], "C", [0]),
            (["C", "G"], "C", [0, 7]),
            (["D", "F#", "A"], "D", [0, 4, 7]),
            (["E", "G#", "B", "D"], "E", [0, 4, 7, 10]),
            (["Ab", "C", "Eb", "Bb"], "Ab", [0, 4, 7, 14]),
            (["F", "A", "C", "Eb", "G"], "F", [0, 4, 7, 10, 14]),
            (["G", "B", "D", "F", "A", "C"], "G", [0, 4, 7, 10, 14, 17]),
            (["A", "C#", "E", "G", "B", "D", "F#"], "A", [0, 4, 7, 10, 14, 17, 21]),
        ]
    )
    def test_notes_to_positions(self, notes, root, expected_positions):
        pos = notes_to_positions(notes, root)
        self.assertEqual(expected_positions, pos)


class TestGetAllRotatedNotes(unittest.TestCase):

    @parameterized.expand(
        [
            (["C", "G"], [["C", "G"], ["G", "C"]]),
            (["C", "F", "G"], [["C", "F", "G"], ["F", "G", "C"], ["G", "C", "F"]]),
        ]
    )
    def test_get_all_rotated_notes(self, notes, expected_rotations):
        notes_list = get_all_rotated_notes(notes)
        self.assertEqual(expected_rotations, notes_list)


class TestFindChordsFromNotes(unittest.TestCase):

    @parameterized.expand(
        [
            (["C", "E", "G"], ["C"]),
            (["F#", "A", "D"], ["D/F#"]),
            (["B", "E", "G#"], ["E/B"]),
            (["Eb", "Gb", "A"], ["Ebdim"]),
            (["G", "C", "D"], ["Gsus4", "Csus2/G"]),
            (["Eb", "Gb", "A", "C"], ["Ebdim7", "Gbdim7/Eb", "Adim7/Eb", "Cdim7/Eb"]),
            (["F", "A", "Db"], ["Faug", "Aaug/F", "Dbaug/F"]),
            (["C", "E", "G", "D"], ["Cadd9"]),
            (["F#", "A", "C", "E"], ["F#m7-5", "Am6/F#", "C6b5/F#"]),
            (["C", "E", "F", "G"], ["Cadd4"]),
            (["C", "Eb", "F", "G"], ["Cmadd4"]),
        ]
    )
    def test_find_chords_from_notes(self, notes, expected_chord_strs):
        chords = find_chords_from_notes(notes)
        expected_chords = [Chord(c) for c in expected_chord_strs]
        self.assertEqual(expected_chords, chords)

    @parameterized.expand(
        [
            ("C Eb G Bb F", ["Cm7add11", "F11/C"]),
            ("C E G B F", "CM7add11"),
            ("C Eb G B F", "CmM7add11"),
            ("C E G A B D", "CM7add13"),
        ]
    )
    def test_add_extension(self, notes, expected_chords):
        self._assert_chords(notes, expected_chords)

    def test_idempotence(self):
        for _ in range(2):
            chords = find_chords_from_notes(["Eb", "Gb", "Bbb", "Dbb"])
            self.assertEqual(
                chords,
                [
                    Chord("Ebdim7"),
                    Chord("Gbdim7/Eb"),
                    Chord("Adim7/Eb"),
                    Chord("Cdim7/Eb"),
                ],
            )
            self.assertEqual(
                chords[0].components(visible=True), ["Eb", "Gb", "Bbb", "Dbb"]
            )

    def _assert_chords(self, notes, expected_chords):
        """Validates that the specified notes translated to the expected chords.

        :param notes: The notes of the chord, either as a list of strings,
          e.g. ["G", "C", "D"] or a string, e.g. "G C D"
        :param expected_chords: the chords that the notes could translate to,
            specified as a list of strings, e.g. [ "Gsus4", "Csus2/G" ],
            or a single string if only one chord expected.
        """
        if isinstance(notes, str):
            notes = notes.split()
        c0 = find_chords_from_notes(notes)
        if isinstance(expected_chords, str):
            expected_chords = [expected_chords]
        self.assertEqual([Chord(c) for c in expected_chords], c0)

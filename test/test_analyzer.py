import unittest

from pychord import Chord
from pychord.analyzer import (
    get_all_rotated_notes,
    find_chords_from_notes,
    notes_to_positions,
)


class TestNotesToPositions(unittest.TestCase):
    def test_notes_to_positions(self):
        for notes, root, expected_positions in [
            (["C"], "C", [0]),
            (["C", "G"], "C", [0, 7]),
            (["D", "F#", "A"], "D", [0, 4, 7]),
            (["E", "G#", "B", "D"], "E", [0, 4, 7, 10]),
            (["Ab", "C", "Eb", "Bb"], "Ab", [0, 4, 7, 14]),
            (["F", "A", "C", "Eb", "G"], "F", [0, 4, 7, 10, 14]),
            (["G", "B", "D", "F", "A", "C"], "G", [0, 4, 7, 10, 14, 17]),
            (["A", "C#", "E", "G", "B", "D", "F#"], "A", [0, 4, 7, 10, 14, 17, 21]),
        ]:
            with self.subTest(notes=notes, root=root):
                self.assertEqual(notes_to_positions(notes, root), expected_positions)


class TestGetAllRotatedNotes(unittest.TestCase):
    def test_get_all_rotated_notes(self):
        for notes, expected_rotations in [
            (["C", "G"], [["C", "G"], ["G", "C"]]),
            (["C", "F", "G"], [["C", "F", "G"], ["F", "G", "C"], ["G", "C", "F"]]),
        ]:
            with self.subTest(notes=notes):
                self.assertEqual(get_all_rotated_notes(notes), expected_rotations)


class TestFindChordsFromNotes(unittest.TestCase):
    def test_empty(self):
        with self.assertRaises(ValueError):
            find_chords_from_notes([])

    def test_find_chords_from_notes(self):
        """
        Validates that the specified notes translated to the expected chords.
        """
        for notes, expected_chord_strs in [
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
            (["C", "Eb", "G", "Bb", "F"], ["Cm7add11"]),
            (["C", "E", "G", "B", "F"], ["Cmaj7add11"]),
            (["C", "Eb", "G", "B", "F"], ["Cmmaj7add11"]),
            (["C", "E", "G", "B", "A"], ["Cmaj7add13", "Am9/C"]),
        ]:
            with self.subTest(notes=notes):
                chords = find_chords_from_notes(notes)
                self.assertEqual([str(c) for c in chords], expected_chord_strs)

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

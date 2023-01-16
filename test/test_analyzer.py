import unittest

from pychord import Chord
from pychord.analyzer import get_all_rotated_notes, find_chords_from_notes, notes_to_positions


class TestNotesToPositions(unittest.TestCase):

    def test_one(self):
        pos = notes_to_positions(["C"], "C")
        self.assertEqual(pos, [0])

    def test_power(self):
        pos = notes_to_positions(["C", "G"], "C")
        self.assertEqual(pos, [0, 7])

    def test_major(self):
        pos = notes_to_positions(["D", "F#", "A"], "D")
        self.assertEqual(pos, [0, 4, 7])

    def test_seventh(self):
        pos = notes_to_positions(["E", "G#", "B", "D"], "E")
        self.assertEqual(pos, [0, 4, 7, 10])

    def test_add9(self):
        pos = notes_to_positions(["Ab", "C", "Eb", "Bb"], "Ab")
        self.assertEqual(pos, [0, 4, 7, 14])

    def test_major_add_9(self):
        # major add 9 is the same as add9
        self.test_add9()

    def test_ninth(self):
        pos = notes_to_positions(["F", "A", "C", "Eb", "G"], "F")
        self.assertEqual(pos, [0, 4, 7, 10, 14])

    def test_eleventh(self):
        pos = notes_to_positions(["G", "B", "D", "F", "A", "C"], "G")
        self.assertEqual(pos, [0, 4, 7, 10, 14, 17])

    def test_thirteenth(self):
        pos = notes_to_positions(["A", "C#", "E", "G", "B", "D", "F#"], "A")
        self.assertEqual(pos, [0, 4, 7, 10, 14, 17, 21])


class TestGetAllRotatedNotes(unittest.TestCase):

    def test_two(self):
        notes_list = get_all_rotated_notes(["C", "G"])
        self.assertEqual(notes_list, [["C", "G"], ["G", "C"]])

    def test_three(self):
        notes_list = get_all_rotated_notes(["C", "F", "G"])
        self.assertEqual(notes_list, [["C", "F", "G"], ["F", "G", "C"], ["G", "C", "F"]])


class TestFindChordsFromNotes(unittest.TestCase):

    def _assert_chords(self, notes, expected_chords):
        """ Validates that the specified notes translated to the expected chords.

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
        self.assertEqual(c0, [Chord(c) for c in expected_chords])

    def test_major(self):
        chords = find_chords_from_notes(["C", "E", "G"])
        self.assertEqual(chords, [Chord("C")])

    def test_major_on_third(self):
        chords = find_chords_from_notes(["F#", "A", "D"])
        self.assertEqual(chords, [Chord("D/F#")])

    def test_major_on_fifth(self):
        chords = find_chords_from_notes(["B", "E", "G#"])
        self.assertEqual(chords, [Chord("E/B")])

    def test_dim(self):
        chords = find_chords_from_notes(["Eb", "Gb", "A"])
        self.assertEqual(chords, [Chord("Ebdim")])

    def test_sus4(self):
        chords = find_chords_from_notes(["G", "C", "D"])
        self.assertEqual(chords, [Chord("Gsus4"), Chord("Csus2/G")])

    def test_dim6(self):
        chords = find_chords_from_notes(["Eb", "Gb", "A", "C"])
        self.assertEqual(chords, [Chord("Ebdim7"), Chord("Gbdim7/Eb"), Chord("Adim7/Eb"), Chord("Cdim7/Eb")])

    def test_aug(self):
        chords = find_chords_from_notes(["F", "A", "Db"])
        self.assertEqual(chords, [Chord("Faug"), Chord("Aaug/F"), Chord("Dbaug/F")])

    def test_add9(self):
        chords = find_chords_from_notes(["C", "E", "G", "D"])
        self.assertEqual(chords, [Chord("Cadd9")])

    def test_m7b5(self):
        chords = find_chords_from_notes(["F#", "A", "C", "E"])
        self.assertEqual(chords, [Chord("F#m7-5"), Chord("Am6/F#"), Chord("C6b5/F#")])

    def test_m7dim5(self):
        chords = find_chords_from_notes(["F#", "A", "C", "E"])
        self.assertEqual(chords, [Chord("F#m7-5"), Chord("Am6/F#"), Chord("C6b5/F#")])

    def test_add4(self):
        chords = find_chords_from_notes(["C", "E", "F", "G"])
        self.assertEqual(chords, [Chord("Cadd4")])

    def test_minor_add4(self):
        chords = find_chords_from_notes(["C", "Eb", "F", "G"])
        self.assertEqual(chords, [Chord("Cmadd4")])

    def test_minor7_add11(self):
        self._assert_chords("C Eb G Bb F", ["Cm7add11", "F11/C"])

    def test_major7_add11(self):
        self._assert_chords("C E G B F", "CM7add11")

    def test_minormajor7_add11(self):
        self._assert_chords("C Eb G B F", "CmM7add11")

    def test_major7_add13(self):
        self._assert_chords("C E G A B D", "CM7add13")

    def test_idempotence(self):
        for _ in range(2):
            chords = find_chords_from_notes(["Eb", "Gb", "A", "C"])
            self.assertEqual(chords, [Chord("Ebdim7"), Chord("Gbdim7/Eb"), Chord("Adim7/Eb"), Chord("Cdim7/Eb")])
            self.assertEqual(chords[0].components(visible=True), ["Eb", "Gb", "A", "C"])

import unittest

from pychord import Chord
from pychord.analyzer import get_all_rotated_notes, note_to_chord, notes_to_positions


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


class TestNoteToChord(unittest.TestCase):

    def test_major(self):
        chords = note_to_chord(["C", "E", "G"])
        self.assertEqual(chords, [Chord("C")])

    def test_major_on_third(self):
        chords = note_to_chord(["F#", "A", "D"])
        self.assertEqual(chords, [Chord("D/F#")])

    def test_major_on_fifth(self):
        chords = note_to_chord(["B", "E", "G#"])
        self.assertEqual(chords, [Chord("E/B")])

    def test_dim(self):
        chords = note_to_chord(["Eb", "Gb", "A"])
        self.assertEqual(chords, [Chord("Ebdim")])

    def test_dim6(self):
        chords = note_to_chord(["Eb", "Gb", "A", "C"])
        self.assertEqual(chords, [Chord("Ebdim6"), Chord("Gbdim6/Eb"), Chord("Adim6/Eb"), Chord("Cdim6/Eb")])

    def test_aug(self):
        chords = note_to_chord(["F", "A", "Db"])
        self.assertEqual(chords, [Chord("Faug"), Chord("Aaug/F"), Chord("Dbaug/F")])

    def test_add9(self):
        chords = note_to_chord(["C", "E", "G", "D"])
        self.assertEqual(chords, [Chord("Cadd9")])

    def test_m7dim5(self):
        chords = note_to_chord(["F#", "A", "C", "E"])
        self.assertEqual(chords, [Chord("F#m7-5")])

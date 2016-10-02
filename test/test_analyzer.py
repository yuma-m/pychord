import unittest

from pychord.analyzer import notes_to_positions


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

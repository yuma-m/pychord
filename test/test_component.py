# -*- coding: utf-8 -*-

import unittest

from pychord import Chord


class TestChordComponent(unittest.TestCase):

    def test_normal_chord(self):
        c = Chord("C")
        com0 = c.components(visible=False)
        self.assertEqual(com0, [0, 4, 7])
        com1 = c.components(visible=True)
        self.assertEqual(com1, ["C", "E", "G"])

    def test_minor_chord(self):
        c = Chord("Am")
        com0 = c.components(visible=False)
        self.assertEqual(com0, [9, 12, 16])
        com1 = c.components(visible=True)
        self.assertEqual(com1, ["A", "C", "E"])

    def test_dim_chord(self):
        c = Chord("Ddim")
        com0 = c.components(visible=False)
        self.assertEqual(com0, [2, 5, 8])
        com1 = c.components(visible=True)
        self.assertEqual(com1, ["D", "F", "G#"])

    def test_dim7_chord(self):
        c = Chord("Cdim7")
        com0 = c.components(visible=False)
        self.assertEqual(com0, [0, 3, 6, 9])
        com1 = c.components(visible=True)
        self.assertEqual(com1, ["C", "Eb", "Gb", "A"])

    def test_aug_chord(self):
        c = Chord("Eaug")
        com0 = c.components(visible=False)
        self.assertEqual(com0, [4, 8, 12])
        com1 = c.components(visible=True)
        self.assertEqual(com1, ["E", "G#", "C"])

    def test_slash_chord(self):
        c = Chord("CM9/D")
        com0 = c.components(visible=False)
        self.assertEqual(com0, [-10, 0, 4, 7, 11])
        com1 = c.components(visible=True)
        self.assertEqual(com1, ["D", "C", "E", "G", "B"])

    def test_sus4_chord(self):
        c = Chord("Fsus4")
        com0 = c.components(visible=False)
        self.assertEqual(com0, [5, 10, 12])
        com1 = c.components(visible=True)
        self.assertEqual(com1, ["F", "Bb", "C"])

    def test_seventh_chord(self):
        c = Chord("G7")
        com0 = c.components(visible=False)
        self.assertEqual(com0, [7, 11, 14, 17])
        com1 = c.components(visible=True)
        self.assertEqual(com1, ["G", "B", "D", "F"])

    def test_sixth_chord(self):
        c = Chord("C6")
        com0 = c.components(visible=False)
        self.assertEqual(com0, [0, 4, 7, 9])
        com1 = c.components(visible=True)
        self.assertEqual(com1, ["C", "E", "G", "A"])

    def test_appended_chord(self):
        c = Chord("C#m7b9b5")
        com0 = c.components(visible=False)
        self.assertEqual(com0, [1, 4, 7, 11, 14])
        com1 = c.components(visible=True)
        self.assertEqual(com1, ["C#", "E", "G", "B", "D"])


class TestChordComponentWithPitch(unittest.TestCase):

    def test_normal_chord(self):
        c = Chord("C")
        com = c.components_with_pitch(root_pitch=1)
        self.assertEqual(com, ["C1", "E1", "G1"])

    def test_minor_chord(self):
        c = Chord("Am")
        com = c.components_with_pitch(root_pitch=2)
        self.assertEqual(com, ["A2", "C3", "E3"])

    def test_slash_chord(self):
        c = Chord("Dm7/G")
        com = c.components_with_pitch(root_pitch=3)
        self.assertEqual(com, ["G3", "D4", "F4", "A4", "C5"])

    def test_add9_chord(self):
        c = Chord("Eadd9")
        com = c.components_with_pitch(root_pitch=5)
        self.assertEqual(com, ["E5", "G#5", "B5", "F#6"])


if __name__ == '__main__':
    unittest.main()

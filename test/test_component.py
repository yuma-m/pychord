#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from pychord import Chord


class TestChordCreations(unittest.TestCase):

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

    def test_aug_chord(self):
        c = Chord("Eaug")
        com0 = c.components(visible=False)
        self.assertEqual(com0, [4, 8, 12])
        com1 = c.components(visible=True)
        self.assertEqual(com1, ["E", "G#", "C"])

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

if __name__ == '__main__':
    unittest.main()

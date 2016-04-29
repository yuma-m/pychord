#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from pychord import Chord


class TestChordCreations(unittest.TestCase):

    def test_normal_chord(self):
        c = Chord("C")
        self.assertEqual(c.root, "C")
        self.assertEqual(c.quality.quality, "")

    def test_invalid_chord(self):
        self.assertRaises(ValueError, Chord, ("H"))

    def test_minor_chord(self):
        c = Chord("Am")
        self.assertEqual(c.root, "A")
        self.assertEqual(c.quality.quality, "m")

    def test_m75_chord(self):
        c = Chord("Bm7-5")
        self.assertEqual(c.root, "B")
        self.assertEqual(c.quality.quality, "m7-5")

    def test_invalid_quality_chord(self):
        self.assertRaises(ValueError, Chord, ("Csus3"))

    def test_slash_chord(self):
        c = Chord("F/G")
        self.assertEqual(c.root, "F")
        self.assertEqual(c.quality.quality, "")
        self.assertEqual(c.on, "G")

    def test_minor_slash_chord(self):
        c = Chord("Dm/G")
        self.assertEqual(c.root, "D")
        self.assertEqual(c.quality.quality, "m")
        self.assertEqual(c.on, "G")

    def test_invalid_slash_chord(self):
        self.assertRaises(ValueError, Chord, ("C/H"))

if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-

import unittest

from pychord import Chord


class TestChordCreations(unittest.TestCase):

    def test_transpose_zero(self):
        c = Chord("Am")
        c.transpose(0)
        self.assertEqual(c.root, "A")
        self.assertEqual(c.quality.quality, "m")
        self.assertEqual(c, Chord("Am"))

    def test_transpose_positive(self):
        c = Chord("Am")
        c.transpose(3)
        self.assertEqual(c.root, "C")
        self.assertEqual(c.quality.quality, "m")
        self.assertEqual(c, Chord("Cm"))

    def test_transpose_negative(self):
        c = Chord("Am")
        c.transpose(-4)
        self.assertEqual(c.root, "F")
        self.assertEqual(c.quality.quality, "m")
        self.assertEqual(c, Chord("Fm"))

    def test_transpose_slash(self):
        c = Chord("Am7/G")
        c.transpose(3)
        self.assertEqual(c.root, "C")
        self.assertEqual(c.quality.quality, "m7")
        self.assertEqual(c.on, "Bb")
        self.assertEqual(c, Chord("Cm7/Bb"))

    def test_invalid_transpose_type(self):
        c = Chord("Am")
        self.assertRaises(TypeError, c.transpose, "A")

    def test_transpose_eq1(self):
        c = Chord("C")
        c.transpose(1)
        self.assertEqual(c, Chord("C#"))
        self.assertEqual(c, Chord("Db"))

    def test_transpose_eq2(self):
        c = Chord("C")
        c.transpose(2)
        self.assertEqual(c, Chord("D"))


if __name__ == '__main__':
    unittest.main()

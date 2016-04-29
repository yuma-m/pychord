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

if __name__ == '__main__':
    unittest.main()

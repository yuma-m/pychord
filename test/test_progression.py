#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from pychord import Chord, ChordProgression


class TestChordProgressionCreations(unittest.TestCase):

    def test_none(self):
        cp = ChordProgression()
        self.assertEqual(cp.get_chords(), [])

    def test_one_chord(self):
        c = Chord("C")
        cp = ChordProgression(c)
        self.assertEqual(cp.get_chords(), [c])

    def test_one_chord_str(self):
        c = "C"
        cp = ChordProgression(c)
        self.assertEqual(cp.get_chords(), [Chord(c)])

    def test_one_chord_list(self):
        c = Chord("C")
        cp = ChordProgression([c])
        self.assertEqual(cp.get_chords(), [c])

    def test_one_chord_list_str(self):
        c = "C"
        cp = ChordProgression([c])
        self.assertEqual(cp.get_chords(), [Chord(c)])

    def test_multiple_chords(self):
        c1 = Chord("C")
        c2 = Chord("D")
        cp = ChordProgression([c1, c2])
        self.assertEqual(cp.get_chords(), [c1, c2])

    def test_multiple_chords_str(self):
        c1 = "C"
        c2 = "D"
        cp = ChordProgression([c1, c2])
        self.assertEqual(cp.get_chords(), [Chord(c1), Chord(c2)])

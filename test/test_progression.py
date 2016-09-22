#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from pychord import Chord, ChordProgression


class TestChordProgressionCreations(unittest.TestCase):

    def test_none(self):
        cp = ChordProgression()
        self.assertEqual(cp.chords, [])

    def test_one_chord(self):
        c = Chord("C")
        cp = ChordProgression(c)
        self.assertEqual(cp.chords, [c])

    def test_one_chord_str(self):
        c = "C"
        cp = ChordProgression(c)
        self.assertEqual(cp.chords, [Chord(c)])

    def test_one_chord_list(self):
        c = Chord("C")
        cp = ChordProgression([c])
        self.assertEqual(cp.chords, [c])

    def test_one_chord_list_str(self):
        c = "C"
        cp = ChordProgression([c])
        self.assertEqual(cp.chords, [Chord(c)])

    def test_multiple_chords(self):
        c1 = Chord("C")
        c2 = Chord("D")
        cp = ChordProgression([c1, c2])
        self.assertEqual(cp.chords, [c1, c2])

    def test_multiple_chords_str(self):
        c1 = "C"
        c2 = "D"
        cp = ChordProgression([c1, c2])
        self.assertEqual(cp.chords, [Chord(c1), Chord(c2)])


class TestChordProgressionFunctions(unittest.TestCase):

    def test_append(self):
        cp = ChordProgression(["C", "D", "E"])
        cp.append("F")
        self.assertEqual(len(cp), 4)
        self.assertEqual(cp.chords[-1], Chord("F"))

    def test_insert(self):
        cp = ChordProgression(["C", "D", "E"])
        cp.insert(0, "F")
        self.assertEqual(len(cp), 4)
        self.assertEqual(cp.chords[0], Chord("F"))

    def test_pop(self):
        cp = ChordProgression(["C", "D", "E"])
        c = cp.pop()
        self.assertEqual(len(cp), 2)
        self.assertEqual(c, Chord("E"))

    def test_transpose(self):
        cp = ChordProgression(["C", "F", "G"])
        cp.transpose(3)
        self.assertEqual(cp.chords, [Chord("Eb"), Chord("Ab"), Chord("Bb")])

    def test_add(self):
        cp1 = ChordProgression(["C", "F", "G"])
        cp2 = ChordProgression(["Am", "Em"])
        cp = cp1 + cp2
        self.assertEqual(len(cp), 5)
        self.assertEqual(cp.chords, [Chord("C"), Chord("F"), Chord("G"), Chord("Am"), Chord("Em")])

    def test_self_add(self):
        cp1 = ChordProgression(["C", "F", "G"])
        cp2 = ChordProgression(["Am", "Em"])
        cp1 += cp2
        self.assertEqual(len(cp1), 5)
        self.assertEqual(cp1.chords, [Chord("C"), Chord("F"), Chord("G"), Chord("Am"), Chord("Em")])

    def test_get_item(self):
        cp = ChordProgression(["C", "F", "G"])
        self.assertEqual(cp[0], Chord("C"))
        self.assertEqual(cp[1], Chord("F"))
        self.assertEqual(cp[-1], Chord("G"))

    def test_slice(self):
        cp = ChordProgression(["C", "F", "G"])
        self.assertEqual(cp[0:1], [Chord("C")])
        self.assertEqual(cp[1:], [Chord("F"), Chord("G")])
        self.assertEqual(cp[0::2], [Chord("C"), Chord("G")])

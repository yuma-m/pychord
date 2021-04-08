# -*- coding: utf-8 -*-

import unittest

from pychord import QualityManager, Chord, note_to_chord


class TestQuality(unittest.TestCase):
    def setUp(self):
        self.quality_manager = QualityManager()

    def test_eq(self):
        q1 = self.quality_manager.get_quality("m7-5")
        q2 = self.quality_manager.get_quality("m7-5")
        self.assertEqual(q1, q2)

    def test_eq_alias_maj9(self):
        q1 = self.quality_manager.get_quality("M9")
        q2 = self.quality_manager.get_quality("maj9")
        self.assertEqual(q1, q2)

    def test_eq_alias_m7b5(self):
        q1 = self.quality_manager.get_quality("m7-5")
        q2 = self.quality_manager.get_quality("m7b5")
        self.assertEqual(q1, q2)

    def test_eq_alias_min(self):
        q1 = self.quality_manager.get_quality("m")
        q2 = self.quality_manager.get_quality("min")
        q3 = self.quality_manager.get_quality("-")
        self.assertEqual(q1, q2)
        self.assertEqual(q1, q3)

    def test_invalid_eq(self):
        q = self.quality_manager.get_quality("m7")
        with self.assertRaises(TypeError):
            print(q == 0)


class TestQualityManager(unittest.TestCase):

    def test_singleton(self):
        quality_manager = QualityManager()
        quality_manager2 = QualityManager()
        self.assertIs(quality_manager, quality_manager2)


class TestOverwriteQuality(unittest.TestCase):
    def setUp(self):
        self.quality_manager = QualityManager()

    def tearDown(self):
        self.quality_manager.load_default_qualities()

    def test_overwrite(self):
        self.quality_manager.set_quality("11", (0, 4, 7, 10, 14, 17))
        chord = Chord("C11")
        self.assertEqual(chord.components(), ['C', 'E', 'G', 'Bb', 'D', 'F'])

    def test_find_from_components(self):
        self.quality_manager.set_quality("13", (0, 4, 7, 10, 14, 17, 21))
        chords = note_to_chord(['C', 'E', 'G', 'Bb', 'D', 'F', 'A'])
        self.assertEqual(chords, [Chord("C13")])

    def test_keep_existing_chord(self):
        chord = Chord("C11")
        self.quality_manager.set_quality("11", (0, 4, 7, 10, 14, 17))
        self.assertEqual(chord.components(), ['C', 'G', 'Bb', 'D', 'F'])


if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-

import unittest

from pychord import Quality


class TestQuality(unittest.TestCase):

    def test_eq(self):
        c1 = Quality("m7-5")
        c2 = Quality("m7-5")
        self.assertEqual(c1, c2)

    def test_eq_alias_69(self):
        c1 = Quality("69")
        c2 = Quality("6.9")
        self.assertEqual(c1, c2)

    def test_eq_alias_m69(self):
        c1 = Quality("m69")
        c2 = Quality("m6.9")
        self.assertEqual(c1, c2)

    def test_eq_alias_maj9(self):
        c1 = Quality("M9")
        c2 = Quality("maj9")
        self.assertEqual(c1, c2)

    def test_eq_alias_m7b5(self):
        c1 = Quality("m7-5")
        c2 = Quality("m7b5")
        self.assertEqual(c1, c2)

    def test_eq_alias_m7b9b5(self):
        c1 = Quality("m7-9-5")
        c2 = Quality("m7b9b5")
        self.assertEqual(c1, c2)

    def test_eq_alias_7b9b5(self):
        c1 = Quality("7-9-5")
        c2 = Quality("7b9b5")
        self.assertEqual(c1, c2)

    def test_eq_alias_7b9sharp5(self):
        c1 = Quality("7-9+5")
        c2 = Quality("7b9#5")
        self.assertEqual(c1, c2)

    def test_eq_alias_7b9sharp9(self):
        c1 = Quality("7-9+9")
        c2 = Quality("7b9#9")
        self.assertEqual(c1, c2)

    def test_eq_alias_7b9sharp11(self):
        c1 = Quality("7-9+11")
        c2 = Quality("7b9#11")
        self.assertEqual(c1, c2)

    def test_eq_alias_7sharp9sharp11(self):
        c1 = Quality("7+9+11")
        c2 = Quality("7#9#11")
        self.assertEqual(c1, c2)

    def test_eq_alias_7sharp9b5(self):
        c1 = Quality("7+9-5")
        c2 = Quality("7#9b5")
        self.assertEqual(c1, c2)

    def test_eq_alias_7sharp9sharp5(self):
        c1 = Quality("7+9+5")
        c2 = Quality("7#9#5")
        self.assertEqual(c1, c2)

    def test_eq_alias_7b9b13(self):
        c1 = Quality("7-9-13")
        c2 = Quality("7b9b13")
        self.assertEqual(c1, c2)

    def test_eq_alias_min(self):
        c1 = Quality("m")
        c2 = Quality("min")
        c3 = Quality("-")
        aliases = set(['-', 'm', 'min'])
        self.assertEqual(c1, c2)
        self.assertEqual(c1, c3)
        self.assertTrue(set(c1.aliases) == aliases)
        self.assertTrue(set(c2.aliases) == aliases)
        self.assertTrue(set(c3.aliases) == aliases)

    def test_invalid_eq(self):
        c = Quality("m7")
        with self.assertRaises(TypeError):
            print(c == 0)


if __name__ == '__main__':
    unittest.main()

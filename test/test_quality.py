# -*- coding: utf-8 -*-

import unittest

from pychord import Quality


class TestQuality(unittest.TestCase):

    def test_eq(self):
        c1 = Quality("m7-5")
        c2 = Quality("m7-5")
        self.assertEqual(c1, c2)

    def test_invalid_eq(self):
        c = Quality("m7")
        with self.assertRaises(TypeError):
            print(c == 0)


if __name__ == '__main__':
    unittest.main()

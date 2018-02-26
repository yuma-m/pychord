# -*- coding: utf-8 -*-

import unittest

from pychord.constants import NOTE_VAL_DICT, VAL_NOTE_DICT


class TestConstants(unittest.TestCase):

    def test_note_and_val(self):
        for note, val in NOTE_VAL_DICT.items():
            self.assertIn(note, VAL_NOTE_DICT[val])


if __name__ == '__main__':
    unittest.main()

import unittest

from pychord.utils import note_to_val


class TestUtils(unittest.TestCase):
    def test_note_to_val(self):
        self.assertEqual(note_to_val("C"), 0)

    def test_note_to_val_invalid(self):
        with self.assertRaises(ValueError):
            note_to_val("X")

import unittest

from pychord.utils import augment, diminish, note_to_val


class TestUtils(unittest.TestCase):
    def test_augment(self):
        self.assertEqual(augment("Cb"), "C")
        self.assertEqual(augment("C"), "C#")
        self.assertEqual(augment("C#"), "C##")

    def test_diminish(self):
        self.assertEqual(diminish("Cb"), "Cbb")
        self.assertEqual(diminish("C"), "Cb")
        self.assertEqual(diminish("C#"), "C")

    def test_note_to_val(self):
        self.assertEqual(note_to_val("C"), 0)

    def test_note_to_val_invalid(self):
        with self.assertRaises(ValueError):
            note_to_val("X")

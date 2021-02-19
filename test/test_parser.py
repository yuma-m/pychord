# -*- coding: utf-8 -*-

import unittest

from pychord.parser import parse
from pychord.utils import notes_list
from pychord.quality import Quality
from pychord.constants.scales import NOTE_VAL_DICT


class TestParser(unittest.TestCase):

    def test_notes_list(self):
        valid_notes = set(["A", "B", "C", "D", "E", "F", "G",
                    "Ab", "Bb", "Cb", "Db", "Eb", "Fb", "Gb",
                    "A#", "B#", "C#", "D#", "E#", "F#", "G#"])
        self.assertTrue(valid_notes == set(NOTE_VAL_DICT.keys()))

    def _test_quality_aliases(self, quality):
        aliases = Quality(quality).aliases
        for note in notes_list():
            for alias in aliases:
                _ = parse(f"{note}{alias}")

    def test_simple_major(self):
        self._test_quality_aliases('maj')

    def test_simple_minor(self):
        self._test_quality_aliases('min')

    def test_augmented(self):
        self._test_quality_aliases('aug')

    def test_diminished(self):
        self._test_quality_aliases('dim')

    def test_sus4(self):
        self._test_quality_aliases('sus4')

    def test_sus2(self):
        self._test_quality_aliases('sus2')

    def test_sixth(self):
        self._test_quality_aliases('6')

    def test_seventh(self):
        self._test_quality_aliases('7')

    def test_7sus4(self):
        self._test_quality_aliases('7sus4')

    def test_7b5(self):
        self._test_quality_aliases('7b5')

    def test_7sharp5(self):
        self._test_quality_aliases('7#5')

    def test_m6(self):
        self._test_quality_aliases('m6')

    def test_m7(self):
        self._test_quality_aliases('m7')

    def test_m7b5(self):
        self._test_quality_aliases('m7b5')

    def test_dim6(self):
        self._test_quality_aliases('dim6')

    def test_M7(self):
        self._test_quality_aliases('M7')

    def test_M7sharp5(self):
        self._test_quality_aliases('M7#5')

    def test_mM7(self):
        self._test_quality_aliases('mM7')

    def test_add9(self):
        self._test_quality_aliases('add9')

    def test_madd9(self):
        self._test_quality_aliases('madd9')

    def test_add11(self):
        self._test_quality_aliases('add11')

    def test_69(self):
        self._test_quality_aliases('69')

    def test_m69(self):
        self._test_quality_aliases('m69')

    def test_9(self):
        self._test_quality_aliases('9')

    def test_m9(self):
        self._test_quality_aliases('m9')

    def test_M9(self):
        self._test_quality_aliases('M9')

    def test_11(self):
        self._test_quality_aliases('11')

    def test_7plus11(self):
        self._test_quality_aliases('7+11')

    def test_minus9plus11(self):
        self._test_quality_aliases('7-9+11')

    def test_plus9plus11(self):
        self._test_quality_aliases('7+9+11')

    def test_13(self):
        self._test_quality_aliases('13')

    def test_b13(self):
        self._test_quality_aliases('7b13')

    def test_7b9b13(self):
        self._test_quality_aliases('7b9b13')

    def test_13b9(self):
        self._test_quality_aliases('13b9')

    def test_13plus9(self):
        self._test_quality_aliases('13+9')


class TestParserMinusPlus(unittest.TestCase):

    def test_minus9(self):
        for note in 'C', 'Ab', 'F#':
            for more_quality in '', '-5', '+5', '+11', '-13':
                final_quality = f"-9{more_quality}"
                root, parsed_quality, append, on = parse(f"{note}{final_quality}")
                self.assertTrue(parsed_quality.quality == final_quality)

    def test_plus9(self):
        for note in 'C', 'Ab', 'F#':
            for more_quality in '', '-5', '+5', '+11':
                final_quality = f"+9{more_quality}"
                root, parsed_quality, append, on = parse(f"{note}{final_quality}")
                self.assertTrue(parsed_quality.quality == final_quality)

    def test_minus13(self):
        for note in 'C', 'Ab', 'F#':
            for more_quality in '', '-9':
                final_quality = f"-13{more_quality}"
                root, parsed_quality, append, on = parse(f"{note}{final_quality}")
                self.assertTrue(parsed_quality.quality == final_quality)


if __name__ == '__main__':
    unittest.main()

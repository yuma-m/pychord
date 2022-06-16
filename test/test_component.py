import unittest

from pychord import Chord


class TestChordComponent(unittest.TestCase):
    def _assert_components(self, chord, qualities, notes):
        """ Validates if a chord is made up of specified qualities and notes.

        :param str chord: A chord, specified as a string, e.g. "C7"
        :param qualities: The expected qualities of the chord, as a list of numbers
        :param notes: The expected notes of the chord, either as a list of strings,
          e.g. ["C", "E", "G", "Bb"] or a string, e.g. "C E G Bb"
        """
        c = Chord(chord)
        com0 = c.components(visible=False)
        self.assertEqual(com0, qualities)
        com1 = c.components(visible=True)
        if isinstance(notes, str):
            notes = notes.split()
        self.assertEqual(com1, notes)

    def test_normal_chord(self):
        self._assert_components("C", [0, 4, 7], ["C", "E", "G"])

    def test_minor_chord(self):
        self._assert_components("Am", [9, 12, 16], ["A", "C", "E"])

    def test_dim_chord(self):
        self._assert_components("Ddim", [2, 5, 8], ["D", "F", "G#"])

    def test_dim7_chord(self):
        self._assert_components("Cdim7", [0, 3, 6, 9], ["C", "Eb", "Gb", "A"])

    def test_aug_chord(self):
        self._assert_components("Eaug", [4, 8, 12], ["E", "G#", "C"])

    def test_slash_chord(self):
        self._assert_components("CM9/D", [-10, 0, 4, 7, 11], ["D", "C", "E", "G", "B"])

    def test_sus4_chord(self):
        self._assert_components("Fsus4", [5, 10, 12], ["F", "Bb", "C"])

    def test_seventh_chord(self):
        self._assert_components("G7", [7, 11, 14, 17], ["G", "B", "D", "F"])

    def test_sixth_chord(self):
        self._assert_components("C6", [0, 4, 7, 9], ["C", "E", "G", "A"])

    def test_appended_chord(self):
        self._assert_components("C#m7b9b5", [1, 4, 7, 11, 14], ["C#", "E", "G", "B", "D"])

    def test_major_add9(self):
        # major add 9 is a major chord with a Major ninth
        base = Chord("C")
        base0 = list(base.components(visible=False))
        base1 = list(base.components(visible=True))
        c = Chord("CMadd9")
        com0 = c.components(visible=False)
        self.assertEqual(com0, base0 + [14])
        com1 = c.components(visible=True)
        self.assertEqual(com1, base1 + ["D"])

    def test_5(self):
        self._assert_components("Db5", [1, 8], "Db Ab")

    def test_b5(self):
        self._assert_components("D(b5)", [2, 6, 8], "D F# G#")

    def test_no5(self):
        self._assert_components("Cno5", [0, 4], "C E")

    def test_add4(self):
        self._assert_components("Cadd4", [0, 4, 5, 7], "C E F G")

    def test_major_add4(self):
        # major add 4 is alternative notation for add4
        self._assert_components("CMadd4", [0, 4, 5, 7], "C E F G")

    def test_minor_add4(self):
        self._assert_components("Cmadd4", [0, 3, 5, 7], "C Eb F G")

    def test_sus4add9(self):
        self._assert_components("Csus4add9", [0, 5, 7, 14], "C F G D")

    def test_minor7_add11(self):
        self._assert_components('Cm7add11', [0, 3, 7, 10, 17], "C Eb G Bb F")

    def test_major7_add11(self):
        self._assert_components('CM7add11', [0, 4, 7, 11, 17], "C E G B F")

    def test_minormajor7_add11(self):
        self._assert_components('CmM7add11', [0, 3, 7, 11, 17], "C Eb G B F")

    def test_major7_add13(self):
        self._assert_components("CM7add13", [0, 4, 7, 9, 11, 14], "C E G A B D")


class TestChordComponentWithPitch(unittest.TestCase):

    def test_normal_chord(self):
        c = Chord("C")
        com = c.components_with_pitch(root_pitch=1)
        self.assertEqual(com, ["C1", "E1", "G1"])

    def test_minor_chord(self):
        c = Chord("Am")
        com = c.components_with_pitch(root_pitch=2)
        self.assertEqual(com, ["A2", "C3", "E3"])

    def test_slash_chord(self):
        c = Chord("Dm7/G")
        com = c.components_with_pitch(root_pitch=3)
        self.assertEqual(com, ["G3", "D4", "F4", "A4", "C5"])

    def test_add9_chord(self):
        c = Chord("Eadd9")
        com = c.components_with_pitch(root_pitch=5)
        self.assertEqual(com, ["E5", "G#5", "B5", "F#6"])

    def test_first_order_inversion(self):
        c = Chord("G/1")
        com = c.components_with_pitch(root_pitch=4)
        self.assertEqual(com, ["B4", "D5", "G5"])
        c2 = Chord("G13b9/1")
        com2 = c2.components_with_pitch(root_pitch=4)
        self.assertEqual(com2, ['B4', 'D5', 'F5', 'G#5', 'E6', 'G6'])

    def test_second_order_inversion(self):
        c = Chord("G/2")
        com = c.components_with_pitch(root_pitch=4)
        self.assertEqual(com, ["D5", "G5", "B5"])
        c2 = Chord("G13b9/2")
        com2 = c2.components_with_pitch(root_pitch=4)
        self.assertEqual(com2, ['D5', 'F5', 'G#5', 'E6', 'G6', 'B6'])

    def test_third_order_inversion(self):
        c = Chord("Cm7/3")
        com = c.components_with_pitch(root_pitch=4)
        self.assertEqual(com, ['Bb4', 'C5', 'Eb5', 'G5'])
        c2 = Chord("F#7/3")
        com2 = c2.components_with_pitch(root_pitch=4)
        self.assertEqual(com2, ['E5', 'F#5', 'A#5', 'C#6'])
        c3 = Chord("G13b9/3")
        com3 = c3.components_with_pitch(root_pitch=4)
        self.assertEqual(com3, ['F5', 'G#5', 'E6', 'G6', 'B6', 'D7'])

    def test_fourth_order_inversion(self):
        c = Chord("F7b9")
        com = c.components_with_pitch(root_pitch=4)
        self.assertEqual(com, ['F4', 'A4', 'C5', 'Eb5', 'Gb5'])
        c2 = Chord("G13b9/4")
        com2 = c2.components_with_pitch(root_pitch=4)
        self.assertEqual(com2, ['G#5', 'E6', 'G6', 'B6', 'D7', 'F7'])

    def test_fifth_order_inversion(self):
        c = Chord("G13b9/5")
        com = c.components_with_pitch(root_pitch=4)
        self.assertEqual(com, ['E6', 'G6', 'B6', 'D7', 'F7', 'G#7'])


if __name__ == '__main__':
    unittest.main()

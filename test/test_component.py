import unittest

from parameterized import parameterized

from pychord import Chord


class TestChordComponent(unittest.TestCase):
    @parameterized.expand(
        [
            ("C", [0, 4, 7], ["C", "E", "G"]),
            ("Gm", [7, 10, 14], ["G", "Bb", "D"]),
            ("Am", [9, 12, 16], ["A", "C", "E"]),
            ("Bdim", [11, 14, 17], ["B", "D", "F"]),
            ("Cdim", [0, 3, 6], ["C", "Eb", "Gb"]),
            ("Dbdim", [1, 4, 7], ["Db", "Fb", "Abb"]),
            ("Ddim", [2, 5, 8], ["D", "F", "Ab"]),
            ("Gbdim", [6, 9, 12], ["Gb", "Bbb", "Dbb"]),
            ("Gdim", [7, 10, 13], ["G", "Bb", "Db"]),
            ("Cdim7", [0, 3, 6, 9], ["C", "Eb", "Gb", "Bbb"]),
            ("Dbdim7", [1, 4, 7, 10], ["Db", "Fb", "Abb", "Bb"]),
            ("Dbaug", [1, 5, 9], ["Db", "F", "A"]),
            ("Eaug", [4, 8, 12], ["E", "G#", "B#"]),
            ("CM9/D", [-10, 0, 4, 7, 11], ["D", "C", "E", "G", "B"]),
            ("Fsus4", [5, 10, 12], ["F", "Bb", "C"]),
            ("G7", [7, 11, 14, 17], ["G", "B", "D", "F"]),
            ("G7b9", [7, 11, 14, 17, 20], ["G", "B", "D", "F", "Ab"]),
            ("G7#11", [7, 11, 14, 17, 25], ["G", "B", "D", "F", "C#"]),
            ("Gm7", [7, 10, 14, 17], ["G", "Bb", "D", "F"]),
            ("C6", [0, 4, 7, 9], ["C", "E", "G", "A"]),
            ("C#m7b9b5", [1, 4, 7, 11, 14], ["C#", "E", "G", "B", "D"]),
            ("Db5", [1, 8], ["Db", "Ab"]),
            ("D(b5)", [2, 6, 8], ["D", "F#", "Ab"]),
            ("Cno5", [0, 4], ["C", "E"]),
            ("Cadd4", [0, 4, 5, 7], ["C", "E", "F", "G"]),
            ("CMadd4", [0, 4, 5, 7], ["C", "E", "F", "G"]),
            ("Cmadd4", [0, 3, 5, 7], ["C", "Eb", "F", "G"]),
            ("Csus4add9", [0, 5, 7, 14], ["C", "F", "G", "D"]),
            ("Cm7add11", [0, 3, 7, 10, 17], ["C", "Eb", "G", "Bb", "F"]),
            ("CM7add11", [0, 4, 7, 11, 17], ["C", "E", "G", "B", "F"]),
            ("Dm7b5", [2, 5, 8, 12], ["D", "F", "Ab", "C"]),
            ("Bm7-5", [11, 14, 17, 21], ["B", "D", "F", "A"]),
            ("Ebm7b5", [3, 6, 9, 13], ["Eb", "Gb", "Bbb", "Db"]),
            ("CmM7add11", [0, 3, 7, 11, 17], ["C", "Eb", "G", "B", "F"]),
            ("CM7add13", [0, 4, 7, 11, 21], ["C", "E", "G", "B", "A"]),
            ("C11", [0, 4, 7, 10, 14, 17], ["C", "E", "G", "Bb", "D", "F"]),
            ("C13", [0, 4, 7, 10, 14, 17, 21], ["C", "E", "G", "Bb", "D", "F", "A"]),
        ]
    )
    def test_chord_components(self, chord, qualities, notes):
        """Validates if a chord is made up of specified qualities and notes.

        :param str chord: A chord, specified as a string, e.g. "C7"
        :param qualities: The expected qualities of the chord, as a list of numbers
        :param notes: The expected notes of the chord, as a list of strings
        """
        c = Chord(chord)
        com0 = c.components(visible=False)
        self.assertEqual(qualities, com0)
        com1 = c.components(visible=True)
        self.assertEqual(notes, com1)

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


class TestChordComponentWithPitch(unittest.TestCase):
    @parameterized.expand(
        [
            ("C", 1, ["C1", "E1", "G1"]),
            ("Am", 2, ["A2", "C3", "E3"]),
            ("Dm7/G", 3, ["G3", "D4", "F4", "A4", "C5"]),
            ("Eadd9", 5, ["E5", "G#5", "B5", "F#6"]),
        ]
    )
    def test_basic_chords_with_pitch(self, chord, root_pitch, expected):
        """Validates if a chord with pitch is correctly calculated.

        :param str chord: A chord, specified as a string, e.g. "C"
        :param int root_pitch: The root pitch for the chord
        :param list expected: The expected components with pitch
        """
        c = Chord(chord)
        com = c.components_with_pitch(root_pitch=root_pitch)
        self.assertEqual(expected, com)

    def test_first_order_inversion(self):
        c = Chord("G/1")
        com = c.components_with_pitch(root_pitch=4)
        self.assertEqual(com, ["B4", "D5", "G5"])
        c2 = Chord("G13b9/1")
        com2 = c2.components_with_pitch(root_pitch=4)
        self.assertEqual(com2, ["B4", "D5", "F5", "G#5", "C6", "E6", "G6"])

    def test_second_order_inversion(self):
        c = Chord("G/2")
        com = c.components_with_pitch(root_pitch=4)
        self.assertEqual(com, ["D5", "G5", "B5"])
        c2 = Chord("G13b9/2")
        com2 = c2.components_with_pitch(root_pitch=4)
        self.assertEqual(com2, ["D5", "F5", "G#5", "C6", "E6", "G6", "B6"])

    def test_third_order_inversion(self):
        c = Chord("Cm7/3")
        com = c.components_with_pitch(root_pitch=4)
        self.assertEqual(com, ["Bb4", "C5", "Eb5", "G5"])
        c2 = Chord("F#7/3")
        com2 = c2.components_with_pitch(root_pitch=4)
        self.assertEqual(com2, ["E5", "F#5", "A#5", "C#6"])
        c3 = Chord("G13b9/3")
        com3 = c3.components_with_pitch(root_pitch=4)
        self.assertEqual(com3, ["F5", "G#5", "C6", "E6", "G6", "B6", "D7"])

    def test_fourth_order_inversion(self):
        c = Chord("F7b9")
        com = c.components_with_pitch(root_pitch=4)
        self.assertEqual(com, ["F4", "A4", "C5", "Eb5", "Gb5"])
        c2 = Chord("G13b9/4")
        com2 = c2.components_with_pitch(root_pitch=4)
        self.assertEqual(com2, ["G#5", "C6", "E6", "G6", "B6", "D7", "F7"])

    def test_fifth_order_inversion(self):
        c = Chord("G13b9/5")
        com = c.components_with_pitch(root_pitch=4)
        self.assertEqual(com, ["C6", "E6", "G6", "B6", "D7", "F7", "G#7"])

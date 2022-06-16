import unittest

from pychord import Chord


class TestChordCreations(unittest.TestCase):

    def test_normal_chord(self):
        c = Chord("C")
        self.assertEqual(c.root, "C")
        self.assertEqual(c.quality.quality, "")

    def test_invalid_chord(self):
        self.assertRaises(ValueError, Chord, "H")

    def test_minor_chord(self):
        c = Chord("Am")
        self.assertEqual(c.root, "A")
        self.assertEqual(c.quality.quality, "m")

    def test_minor_chord_with_minus(self):
        c = Chord("A-")
        self.assertEqual(c.root, "A")
        self.assertEqual(c.quality.quality, "-")

    def test_69_chord(self):
        c = Chord("C69")
        self.assertEqual(c.root, "C")
        self.assertEqual(c.quality.quality, "69")

    def test_m75_chord(self):
        c = Chord("Bm7-5")
        self.assertEqual(c.root, "B")
        self.assertEqual(c.quality.quality, "m7-5")

    def test_invalid_quality_chord(self):
        self.assertRaises(ValueError, Chord, "Csus3")

    def test_slash_chord(self):
        c = Chord("F/G")
        self.assertEqual(c.root, "F")
        self.assertEqual(c.quality.quality, "")
        self.assertEqual(c.on, "G")

    def test_minor_slash_chord(self):
        c = Chord("Dm/G")
        self.assertEqual(c.root, "D")
        self.assertEqual(c.quality.quality, "m")
        self.assertEqual(c.on, "G")

    def test_minor_7b5_chord(self):
        c = Chord("Dm7b5")
        self.assertEqual(c.root, "D")
        self.assertEqual(c.quality.quality, "m7b5")

    def test_invalid_slash_chord(self):
        self.assertRaises(ValueError, Chord, "C/H")

    def test_1st_order_inversion(self):
        c = Chord("C/1")
        self.assertEqual(c.root, "C")
        self.assertEqual(c.quality.quality, "")
        self.assertEqual(c.components(), ["E", "G", "C"])

    def test_2nd_order_inversion(self):
        c = Chord("C/2")
        self.assertEqual(c.root, "C")
        self.assertEqual(c.quality.quality, "")
        self.assertEqual(c.components(), ["G", "C", "E"])

    def test_inversion_complicated(self):
        c = Chord("Dm7b5/1")
        self.assertEqual(c.root, "D")
        self.assertEqual(c.quality.quality, "m7b5")
        self.assertEqual(c.components(), ["F", "G#", "C", "D"])

    def test_inversion_with_alternate_bass(self):
        c = Chord("C/1/F")
        self.assertEqual(c.root, "C")
        self.assertEqual(c.quality.quality, "")
        self.assertEqual(c.components(), ["F", "E", "G", "C"])

    def test_eq(self):
        c1 = Chord("C")
        c2 = Chord("C")
        self.assertEqual(c1, c2)

    def test_eq_alias(self):
        c1 = Chord("Cmaj7")
        c2 = Chord("CM7")
        self.assertEqual(c1, c2)

    def test_invalid_eq(self):
        c = Chord("C")
        with self.assertRaises(TypeError):
            print(c == 0)

    def test_components(self):
        c = Chord("C/E")
        quality_components_before = c.quality.components
        c.components()
        self.assertEqual(c.quality.components, quality_components_before)


class TestChordFromNoteIndex(unittest.TestCase):
    def test_note_1(self):
        chord = Chord.from_note_index(note=1, quality="", scale="Cmaj")
        self.assertEqual(chord, Chord("C"))

    def test_note_2(self):
        chord = Chord.from_note_index(note=2, quality="m7", scale="F#min")
        self.assertEqual(chord, Chord("G#m7"))

    def test_note_3(self):
        chord = Chord.from_note_index(note=3, quality="sus2", scale="Cmin")
        self.assertEqual(chord, Chord("Ebsus2"))

    def test_note_7(self):
        chord = Chord.from_note_index(note=7, quality="7", scale="Amin")
        self.assertEqual(chord, Chord("G7"))

    def test_note_8(self):
        chord = Chord.from_note_index(note=8, quality="", scale="Emaj")
        self.assertEqual(chord, Chord("E"))

    def test_note_0(self):
        with self.assertRaises(ValueError):
            Chord.from_note_index(note=0, quality="", scale="Cmaj")

    def test_note_9(self):
        with self.assertRaises(ValueError):
            Chord.from_note_index(note=9, quality="", scale="Fmaj")

    def test_diatonic_note_1(self):
        chord = Chord.from_note_index(note=1, quality="", diatonic=True, scale="Dmaj")
        self.assertEqual(chord, Chord("D"))

    def test_diatonic_note_2_mode(self):
        chord = Chord.from_note_index(note=2, quality="7", diatonic=True, scale="BLoc")
        self.assertEqual(chord, Chord("Cmaj7"))

    def test_diatonic_note_3_mode(self):
        chord = Chord.from_note_index(note=3, quality="m", diatonic=True, scale="G#Mix")
        self.assertEqual(chord, Chord("Cdim"))

    def test_diatonic_note_4_mode(self):
        chord = Chord.from_note_index(note=4, quality="-", diatonic=True, scale="AbDor")
        self.assertEqual(chord, Chord("C#"))

    def test_diatonic_note_nongeneric(self):
        with self.assertRaises(NotImplementedError):
            Chord.from_note_index(note=5, quality="sus", diatonic=True, scale="Fmaj")


if __name__ == '__main__':
    unittest.main()

import unittest

from pychord import Chord


class TestChordCreations(unittest.TestCase):
    def test_chord_creation(self):
        for chord, expected_root, expected_quality in [
            ("C", "C", ""),
            ("Am", "A", "m"),
            ("A-", "A", "-"),
            ("C69", "C", "69"),
            ("Bm7-5", "B", "m7-5"),
            ("Dm7b5", "D", "m7b5"),
        ]:
            with self.subTest(chord=chord):
                c = Chord(chord)
                self.assertEqual(expected_root, c.root)
                self.assertEqual(expected_quality, c.quality.quality)

    def test_invalid_chord(self):
        for chord in [
            "",
            "Ab#",  # mix of flat and sharp
            "A#b",  # mix of flat and sharp
            "Abbb",  # too many flats
            "A###",  # too many sharps
            "H",
            "Csus3",
            "C/B###",
        ]:
            with self.subTest(chord=chord):
                self.assertRaises(ValueError, Chord, chord)

    def test_slash_chord(self):
        for chord, expected_root, expected_quality, expected_on in [
            ("F/G", "F", "", "G"),
            ("Dm/G", "D", "m", "G"),
        ]:
            with self.subTest(chord=chord):
                c = Chord(chord)
                self.assertEqual(expected_root, c.root)
                self.assertEqual(expected_quality, c.quality.quality)
                self.assertEqual(expected_on, c.on)

    def test_invalid_slash_chord(self):
        self.assertRaises(ValueError, Chord, "C/H")

    def test_inversion(self):
        for chord, expected_root, expected_quality, expected_components in [
            ("C/1", "C", "", ["E", "G", "C"]),
            ("C/2", "C", "", ["G", "C", "E"]),
            ("Dm7b5/1", "D", "m7b5", ["F", "Ab", "C", "D"]),
            ("C/1/F", "C", "", ["F", "E", "G", "C"]),
        ]:
            with self.subTest(chord=chord):
                c = Chord(chord)
                self.assertEqual(expected_root, c.root)
                self.assertEqual(expected_quality, c.quality.quality)
                self.assertEqual(expected_components, c.components())

    def test_eq(self):
        self.assertEqual(Chord("C"), Chord("C"))
        self.assertEqual(Chord("C/G"), Chord("C/G"))

    def test_eq_quality_alias(self):
        self.assertEqual(Chord("Cmaj7"), Chord("CM7"))

    def test_eq_root_alias(self):
        self.assertEqual(Chord("C#"), Chord("Db"))

    def test_eq_invalid(self):
        with self.assertRaises(TypeError):
            Chord("C") == 0

    def test_eq_different_root(self):
        self.assertNotEqual(Chord("C"), Chord("D"))

    def test_eq_different_quality(self):
        self.assertNotEqual(Chord("C"), Chord("Cm"))

    def test_eq_different_on(self):
        self.assertNotEqual(Chord("C"), Chord("C/G"))
        self.assertNotEqual(Chord("C/G"), Chord("C"))
        self.assertNotEqual(Chord("C/B"), Chord("C/G"))

    def test_components(self):
        c = Chord("C/E")
        quality_components_before = c.quality.components
        c.components()
        self.assertEqual(c.quality.components, quality_components_before)

    def test_info(self):
        c = Chord("Cmaj7")

        # String representations.
        self.assertEqual(repr(c), "<Chord: Cmaj7>")
        self.assertEqual(str(c), "Cmaj7")

        # Properties.
        self.assertEqual(c.chord, "Cmaj7")
        self.assertEqual(str(c.quality), "maj7")
        self.assertEqual(c.root, "C")

        # Methods.
        self.assertEqual(
            c.info(),
            """Cmaj7
root=C
quality=maj7
appended=[]
on=""",
        )


class TestChordFromNoteIndex(unittest.TestCase):
    def test_from_note_index(self):
        for note, quality, scale, expected_chord_str in [
            (1, "", "Cmaj", "C"),
            (2, "m7", "F#min", "G#m7"),
            (3, "sus2", "Cmin", "Ebsus2"),
            (7, "7", "Amin", "G7"),
        ]:
            with self.subTest(note=note, quality=quality, scale=scale):
                chord = Chord.from_note_index(note=note, quality=quality, scale=scale)
                self.assertEqual(str(chord), expected_chord_str)

    def test_from_note_index_with_chromatic(self):
        for note, quality, scale, chromatic, expected_chord_str in [
            (1, "", "Cmaj", -1, "Cb"),
            (1, "", "Cmaj", 1, "C#"),
        ]:
            with self.subTest(
                note=note, quality=quality, scale=scale, chromatic=chromatic
            ):
                chord = Chord.from_note_index(
                    note=note, quality=quality, scale=scale, chromatic=chromatic
                )
                self.assertEqual(str(chord), expected_chord_str)

    def test_invalid_note_index(self):
        for note, quality, scale, exception_str in [
            (0, "", "Cmaj", "Invalid note 0"),
            (8, "", "Fmaj", "Invalid note 8"),
        ]:
            with self.subTest(note=note, quality=quality, scale=scale):
                with self.assertRaises(ValueError) as cm:
                    Chord.from_note_index(note=note, quality=quality, scale=scale)
                self.assertEqual(str(cm.exception), exception_str)

    def test_invalid_scale(self):
        for note, quality, scale, exception_str in [
            (1, "", "Xmaj", "Invalid note X"),
            (1, "", "Cbob", "Invalid mode bob"),
        ]:
            with self.subTest(note=note, quality=quality, scale=scale):
                with self.assertRaises(ValueError) as cm:
                    Chord.from_note_index(note=note, quality=quality, scale=scale)
                self.assertEqual(str(cm.exception), exception_str)

    def test_diatonic_from_note_index(self):
        for note, quality, diatonic, scale, expected_chord_str in [
            (1, "", True, "Dmaj", "D"),
            (2, "7", True, "BLoc", "CM7"),
            (3, "m", True, "G#Mix", "B#dim"),
            (4, "-", True, "AbDor", "Db"),
        ]:
            with self.subTest(note=note, quality=quality, scale=scale):
                chord = Chord.from_note_index(
                    note=note, quality=quality, diatonic=diatonic, scale=scale
                )
                self.assertEqual(str(chord), expected_chord_str)

    def test_diatonic_note_non_generic(self):
        with self.assertRaises(NotImplementedError):
            Chord.from_note_index(note=5, quality="sus", diatonic=True, scale="Fmaj")

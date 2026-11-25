import unittest

from pychord import Chord, ChordProgression


class TestChordProgressionCreations(unittest.TestCase):
    def test_none(self):
        cp = ChordProgression()
        self.assertEqual(cp.chords, [])
        self.assertEqual(str(cp), "")
        self.assertEqual(repr(cp), "<ChordProgression: >")

    def test_one_chord(self):
        c = Chord("C")
        cp = ChordProgression(c)
        self.assertEqual(cp.chords, [c])
        self.assertEqual(str(cp), "C")
        self.assertEqual(repr(cp), "<ChordProgression: C>")

    def test_one_chord_str(self):
        c = "C"
        cp = ChordProgression(c)
        self.assertEqual(cp.chords, [Chord(c)])
        self.assertEqual(str(cp), "C")
        self.assertEqual(repr(cp), "<ChordProgression: C>")

    def test_one_chord_invalid_type(self):
        with self.assertRaises(TypeError):
            ChordProgression(1)

    def test_one_chord_list(self):
        c = Chord("C")
        cp = ChordProgression([c])
        self.assertEqual(cp.chords, [c])

    def test_one_chord_list_str(self):
        c = "C"
        cp = ChordProgression([c])
        self.assertEqual(cp.chords, [Chord(c)])
        self.assertEqual(str(cp), "C")
        self.assertEqual(repr(cp), "<ChordProgression: C>")

    def test_one_chord_list_invalid_type(self):
        with self.assertRaises(TypeError):
            ChordProgression([1])

    def test_multiple_chords(self):
        c1 = Chord("C")
        c2 = Chord("D")
        cp = ChordProgression([c1, c2])
        self.assertEqual(cp.chords, [c1, c2])
        self.assertEqual(str(cp), "C | D")
        self.assertEqual(repr(cp), "<ChordProgression: C | D>")

    def test_multiple_chords_str(self):
        c1 = "C"
        c2 = "D"
        cp = ChordProgression([c1, c2])
        self.assertEqual(cp.chords, [Chord(c1), Chord(c2)])
        self.assertEqual(str(cp), "C | D")
        self.assertEqual(repr(cp), "<ChordProgression: C | D>")


class TestChordProgressionFunctions(unittest.TestCase):
    def test_append(self):
        cp = ChordProgression(["C", "D", "E"])
        cp.append("F")
        self.assertEqual(len(cp), 4)
        self.assertEqual(cp.chords[-1], Chord("F"))

    def test_insert(self):
        cp = ChordProgression(["C", "D", "E"])
        cp.insert(0, "F")
        self.assertEqual(len(cp), 4)
        self.assertEqual(cp.chords[0], Chord("F"))

    def test_pop(self):
        cp = ChordProgression(["C", "D", "E"])
        c = cp.pop()
        self.assertEqual(len(cp), 2)
        self.assertEqual(c, Chord("E"))

    def test_transpose(self):
        cp = ChordProgression(["C", "F", "G"])
        cp.transpose(3)
        self.assertEqual(cp.chords, [Chord("Eb"), Chord("Ab"), Chord("Bb")])

    def test_transpose_same_chord_instance(self):
        shared = Chord("C")
        cp = ChordProgression([shared, Chord("D"), shared])

        cp.transpose(2)

        self.assertEqual(cp.chords, [Chord("D"), Chord("E"), Chord("D")])
        self.assertEqual(shared, Chord("C"))

    def test_transpose_repeated_progression(self):
        original = ChordProgression(["C", "G"])
        repeated = original + original

        repeated.transpose(2)

        self.assertEqual(
            repeated.chords, [Chord("D"), Chord("A"), Chord("D"), Chord("A")]
        )
        self.assertEqual(original.chords, [Chord("C"), Chord("G")])

    def test_repeated_progression_does_not_share_chords(self):
        original = ChordProgression(["C", "G"])
        repeated = original + original

        repeated[0].transpose(2)

        self.assertEqual(
            repeated.chords, [Chord("D"), Chord("G"), Chord("C"), Chord("G")]
        )

    def test_passed_chords_are_copied(self):
        c = Chord("C")
        cps = {
            "init_one": ChordProgression(c),
            "init_list": ChordProgression([c, c]),
        }
        appended = ChordProgression()
        appended.append(c)
        appended.append(c)
        cps["append"] = appended
        inserted = ChordProgression()
        inserted.insert(0, c)
        inserted.insert(0, c)
        cps["insert"] = inserted
        set_item = ChordProgression(["D", "D"])
        set_item[0] = c
        set_item[1] = c
        cps["set_item"] = set_item

        for name, cp in cps.items():
            with self.subTest(name=name):
                self.assertTrue(all(chord is not c for chord in cp.chords))
                cp[0].transpose(2)
                self.assertEqual(cp[0], Chord("D"))
                self.assertTrue(all(chord == Chord("C") for chord in cp.chords[1:]))
        self.assertEqual(c, Chord("C"))

    def test_add(self):
        cp1 = ChordProgression(["C", "F", "G"])
        cp2 = ChordProgression(["Am", "Em"])
        cp = cp1 + cp2
        self.assertEqual(len(cp), 5)
        self.assertEqual(
            cp.chords, [Chord("C"), Chord("F"), Chord("G"), Chord("Am"), Chord("Em")]
        )

        # Check the original progressions have not changed.
        self.assertEqual(len(cp1), 3)
        self.assertEqual(len(cp2), 2)

    def test_add_does_not_share_chords(self):
        cp1 = ChordProgression(["C", "F"])
        cp2 = ChordProgression(["G"])
        cp = cp1 + cp2
        cp.transpose(2)
        self.assertEqual(cp.chords, [Chord("D"), Chord("G"), Chord("A")])

        # Check the original progressions have not been transposed.
        self.assertEqual(cp1.chords, [Chord("C"), Chord("F")])
        self.assertEqual(cp2.chords, [Chord("G")])

    def test_self_add(self):
        cp1 = ChordProgression(["C", "F", "G"])
        cp2 = ChordProgression(["Am", "Em"])
        cp1 += cp2
        self.assertEqual(len(cp1), 5)
        self.assertEqual(
            cp1.chords, [Chord("C"), Chord("F"), Chord("G"), Chord("Am"), Chord("Em")]
        )

    def test_get_item(self):
        cp = ChordProgression(["C", "F", "G"])
        self.assertEqual(cp[0], Chord("C"))
        self.assertEqual(cp[1], Chord("F"))
        self.assertEqual(cp[-1], Chord("G"))

    def test_set_item(self):
        cp = ChordProgression(["C", "F", "G"])
        cp[1] = Chord("E")
        self.assertEqual(cp[0], Chord("C"))
        self.assertEqual(cp[1], Chord("E"))
        self.assertEqual(cp[2], Chord("G"))
        self.assertEqual(len(cp), 3)

    def test_set_item_str(self):
        cp = ChordProgression(["C", "F", "G"])
        cp[1] = "E"
        self.assertEqual(cp[1], Chord("E"))
        self.assertIsInstance(cp[1], Chord)

    def test_set_item_invalid_type(self):
        cp = ChordProgression(["C", "F", "G"])
        with self.assertRaises(TypeError):
            cp[1] = 1

    def test_slice(self):
        cp = ChordProgression(["C", "F", "G"])
        self.assertEqual(cp[0:1], [Chord("C")])
        self.assertEqual(cp[1:], [Chord("F"), Chord("G")])
        self.assertEqual(cp[0::2], [Chord("C"), Chord("G")])

    def test_eq(self):
        cp1 = ChordProgression(["C", "F", "G"])
        cp2 = ChordProgression(["C", "F", "G"])
        self.assertEqual(cp1, cp2)
        self.assertIsNot(cp1, cp2)

    def test_invalid_eq(self):
        cp = ChordProgression(["C", "F", "G"])
        with self.assertRaises(TypeError):
            print(cp == 0)

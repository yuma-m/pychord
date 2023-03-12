from typing import List, Union

from .constants import NOTE_VAL_DICT, VAL_NOTE_DICT
from .constants.scales import RELATIVE_KEY_DICT
from .parser import parse
from .quality import QualityManager, Quality
from .utils import transpose_note, display_appended, display_on, note_to_val, val_to_note


class Chord:
    """ Class to handle a chord.

    Attributes:
        _chord: Name of the chord. (e.g. C, Am7, F#m7-5/A)
        _root: The root note of chord. (e.g. C, A, F#)
        _quality: The quality of chord. (e.g. maj, m7, m7-5)
        _appended: The appended notes on chord.
        _on: The base note of slash chord.
    """

    def __init__(self, chord: str):
        """ Constructor of Chord instance

        :param chord: Name of chord (e.g. C, Am7, F#m7-5/A).
        """
        root, quality, appended, on = parse(chord)
        self._chord: str = chord
        self._root: str = root
        self._quality: Quality = quality
        self._appended: List[str] = appended
        self._on: str = on

        self._append_on_chord()

    def __unicode__(self):
        return self._chord

    def __str__(self):
        return self._chord

    def __repr__(self):
        return f"<Chord: {self._chord}>"

    def __eq__(self, other):
        if not isinstance(other, Chord):
            raise TypeError(f"Cannot compare Chord object with {type(other)} object")
        if note_to_val(self._root) != note_to_val(other.root):
            return False
        if self._quality != other.quality:
            return False
        if self._appended != other.appended:
            return False
        if self._on and other.on:
            if note_to_val(self._on) != note_to_val(other.on):
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    @classmethod
    def from_note_index(
        cls,
        note: int,
        quality: str,
        scale: str,
        diatonic: bool = False,
        chromatic: int = 0,
    ) -> "Chord":
        """Create a Chord from note index in a scale

        Chord.from_note_index(1, "", "Cmaj") returns I of C major => Chord("C")
        Chord.from_note_index(3, "m7", "Fmaj") returns IIImin of F major => Chord("Am7")
        Chord.from_note_index(5, "7", "Amin") returns Vmin of A minor => Chord("E7")
        Chord.from_note_index(2, "", "Cmaj") returns II of C major => Chord("D")
        Chord.from_note_index(2, "m", "Cmaj") returns IImin of C major => Chord("Dm")
        Chord.from_note_index(2, "", "Cmaj", diatonic=True) returns IImin of C major => Chord("Dm")
        Chord.from_note_index(2, "", "Cmin", chromatic=-1) returns bII of C minor => Chord("Db")

        :param note: Scale degree of the chord's root (1-7)
        :param quality: Quality of the chord (e.g. m7, sus4)
        :param scale: Base scale (e.g. Cmaj, Amin, F#maj, Ebmin)
        :param diatonic: If True, chord quality is determined using the base scale (overrides :param quality)
        :param chromatic: Lower or raise the scale degree (and all notes of the chord) by semitone(s)
        """
        if not 1 <= note <= 8:
            raise ValueError(f"Invalid note {note}")
        relative_key = RELATIVE_KEY_DICT[scale[-3:]][note - 1]
        root_num = NOTE_VAL_DICT[scale[:-3]] + chromatic
        root = VAL_NOTE_DICT[(root_num + relative_key) % 12][0]

        scale_degrees = RELATIVE_KEY_DICT[scale[-3:]]

        if diatonic:
            # construct the chord based on scale degrees, within 1 octave
            third = scale_degrees[(note + 1) % 7]
            fifth = scale_degrees[(note + 3) % 7]
            seventh = scale_degrees[(note + 5) % 7]

            # adjust the chord to its root position (as a stack of thirds),
            # then set the root to 0
            # e.g. (9, 0, 4) -> [0, 3, 7]
            def get_diatonic_chord(chord):
                uninverted = []
                for note in chord:
                    if not uninverted:
                        uninverted.append(note)
                    elif note > uninverted[-1]:
                        uninverted.append(note)
                    else:
                        uninverted.append(note + 12)
                uninverted = [x - uninverted[0] for x in uninverted]
                return uninverted

            if quality in ["", "-", "maj", "m", "min"]:
                triad = (relative_key, third, fifth)
                q = get_diatonic_chord(triad)
            elif quality in ["7", "M7", "maj7", "m7"]:
                seventh_chord = (relative_key, third, fifth, seventh)
                q = get_diatonic_chord(seventh_chord)
            else:
                raise NotImplementedError("Only generic chords (triads, sevenths) are supported")

            # look up QualityManager to determine chord quality
            quality_manager = QualityManager()
            quality = quality_manager.find_quality_from_components(q)
            if not quality:
                raise RuntimeError(f"Quality with components {q} not found")

        return cls(f"{root}{quality}")

    @property
    def chord(self):
        """ The name of chord """
        return self._chord

    @property
    def root(self):
        """ The root note of chord """
        return self._root

    @property
    def quality(self):
        """ The quality of chord """
        return self._quality

    @property
    def appended(self):
        """ The appended notes on chord """
        return self._appended

    @property
    def on(self):
        """ The base note of slash chord """
        return self._on

    def info(self):
        """ Return information of chord to display """
        return f"""{self._chord}
root={self._root}
quality={self._quality}
appended={self._appended}
on={self._on}"""

    def transpose(self, trans: int, scale: str = "C") -> None:
        """ Transpose the chord

        :param trans: Transpose key
        :param scale: key scale
        """
        if not isinstance(trans, int):
            raise TypeError(f"Expected integers, not {type(trans)}")
        self._root = transpose_note(self._root, trans, scale)
        if self._on:
            self._on = transpose_note(self._on, trans, scale)
        self._reconfigure_chord()

    def components(self, visible: bool = True) -> Union[List[str], List[int]]:
        """ Return the component notes of chord

        :param visible: returns the name of notes if True else list of int
        :return: component notes of chord
        """
        return self._quality.get_components(root=self._root, visible=visible)

    def components_with_pitch(self, root_pitch: int) -> List[str]:
        """ Return the component notes of chord formatted like ["C4", "E4", "G4"]

        :param root_pitch: the pitch of the root note
        :return: component notes of chord
        """
        components = self._quality.get_components(root=self._root)
        if components[0] < 0:
            components = [c + 12 for c in components]
        return [f"{val_to_note(c, scale=self._root)}{root_pitch + c // 12}" for c in components]

    def _append_on_chord(self):
        if self._on:
            self._quality.append_on_chord(self.on, self.root)

    def _reconfigure_chord(self):
        # TODO: Use appended
        self._chord = "{}{}{}{}".format(self._root,
                                        self._quality.quality,
                                        display_appended(self._appended),
                                        display_on(self._on))

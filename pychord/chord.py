# -*- coding: utf-8 -*-
from .constants import NOTE_VAL_DICT, VAL_NOTE_DICT
from .constants.scales import RELATIVE_KEY_DICT
from .parser import parse
from .utils import transpose_note, display_appended, display_on, note_to_val, val_to_note


class Chord(object):
    """ Class to handle a chord.

    :param str _chord: Name of the chord. (e.g. C, Am7, F#m7-5/A)
    :param str _root: The root note of chord.
    :param pychord.Quality _quality: The quality of chord. (e.g. m7, 6, M9, ...)
    :param list[str] _appended: The appended notes on chord.
    :param str _on: The base note of slash chord.
    """
    def __init__(self, chord):
        """ Constructor of Chord instance

        :param str chord: Name of chord.
        """
        self._chord = chord
        self._root, self._quality, self._appended, self._on = "", "", "", ""
        self._parse(chord)

    def __unicode__(self):
        return self._chord

    def __str__(self):
        return self._chord

    def __repr__(self):
        return "<Chord: {}>".format(self._chord)

    def __eq__(self, other):
        if not isinstance(other, Chord):
            raise TypeError("Cannot compare Chord object with {} object".format(type(other)))
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
    def from_note_index(cls, note, quality, scale):
        """ Create a Chord from note index in a scale

        Chord.from_note_index(1, "", "Cmaj") returns I of C major => Chord("C")
        Chord.from_note_index(3, "m7", "Fmaj") returns IIImin of F major => Chord("Am7")
        Chord.from_note_index(5, "7", "Amin") returns Vmin of A minor => Chord("E7")

        :param int note: Note index in a Scale I, II, ..., VIII
        :param str quality: Quality of a chord (m7, sus4, ...)
        :param str scale: Base scale (Cmaj, Amin, F#maj, Ebmin, ...)
        :rtype: Chord
        """
        if not 1 <= note <= 8:
            raise ValueError("Invalid note {}".format(note))
        relative_key = RELATIVE_KEY_DICT[scale[-3:]][note - 1]
        root_num = NOTE_VAL_DICT[scale[:-3]]
        root = VAL_NOTE_DICT[(root_num + relative_key) % 12][0]
        return cls("{}{}".format(root, quality))

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
        return """{}
root={}
quality={}
appended={}
on={}""".format(self._chord, self._root, self._quality, self._appended, self._on)

    def transpose(self, trans, scale="C"):
        """ Transpose the chord

        :param int trans: Transpose key
        :param str scale: key scale
        :return:
        """
        if not isinstance(trans, int):
            raise TypeError("Expected integers, not {}".format(type(trans)))
        self._root = transpose_note(self._root, trans, scale)
        if self._on:
            self._on = transpose_note(self._on, trans, scale)
        self._reconfigure_chord()

    def components(self, visible=True):
        """ Return the component notes of chord

        :param bool visible: returns the name of notes if True else list of int
        :rtype: list[(str or int)]
        :return: component notes of chord
        """
        if self._on:
            self._quality.append_on_chord(self.on, self.root)

        return self._quality.get_components(root=self._root, visible=visible)

    def components_with_pitch(self, root_pitch):
        """ Return the component notes of chord formatted like ["C4", "E4", "G4"]

        :param int root_pitch: the pitch of the root note
        :rtype: list[str]
        :return: component notes of chord
        """
        if self._on:
            self._quality.append_on_chord(self.on, self.root)

        components = self._quality.get_components(root=self._root)
        if components[0] < 0:
            components = [c + 12 for c in components]
        return ["{}{}".format(val_to_note(c, scale=self._root), root_pitch + c // 12) for c in components]

    def _parse(self, chord):
        """ parse a chord

        :param str chord: Name of chord.
        """
        root, quality, appended, on = parse(chord)
        self._root = root
        self._quality = quality
        self._appended = appended
        self._on = on

    def _reconfigure_chord(self):
        # TODO: Use appended
        self._chord = "{}{}{}{}".format(self._root,
                                        self._quality._quality,
                                        display_appended(self._appended),
                                        display_on(self._on))


def as_chord(chord):
    """ convert from str to Chord instance if input is str

    :type chord: str|pychord.Chord
    :param chord: Chord name or Chord instance
    :rtype: pychord.Chord
    :return: Chord instance
    """
    if isinstance(chord, Chord):
        return chord
    elif isinstance(chord, str):
        return Chord(chord)
    else:
        raise TypeError("input type should be str or Chord instance.")

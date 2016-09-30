# -*- coding: utf-8 -*-


from .parser import parse
from .utils import transpose_note, display_appended, display_on


class Chord(object):
    """ Class to handle a chord.

    :param str chord: Name of the chord. (e.g. C, Am7, F#m7-5/A)
    """
    def __init__(self, chord):
        self.chord = chord
        self.root, self.quality, self.appended, self.on = "", "", "", ""
        self._parse(chord)

    def __unicode__(self):
        return self.chord

    def __str__(self):
        return self.chord

    def __repr__(self):
        return "<Chord: {}>".format(self.chord)

    def __eq__(self, other):
        return self.chord == other.chord

    def info(self):
        return """{}
root={}
quality={}
appended={}
on={}""".format(self.chord, self.root, self.quality, self.appended, self.on)

    def transpose(self, trans):
        """ Transpose the chord

        :param int trans: Transpose key
        :return:
        """
        if not isinstance(trans, int):
            raise TypeError("Expected integers, not {}".format(type(trans)))
        self.root = transpose_note(self.root, trans)
        if self.on:
            self.on = transpose_note(self.on, trans)
        self._reconfigure_chord()

    def components(self, visible=True):
        return self.quality.get_components(root=self.root, visible=visible)

    def _parse(self, chord):
        root, quality, appended, on = parse(chord)
        self.root = root
        self.quality = quality
        self.appended = appended
        self.on = on

    def _reconfigure_chord(self):
        # TODO: Use appended
        self.chord = "{}{}{}{}".format(self.root,
                                       self.quality.quality,
                                       display_appended(self.appended),
                                       display_on(self.on))


def as_chord(chord):
    """ convert from str to Chord instance if input is str

    :type chord: str|pychord.Chord
    :param chord: Chord name or Chord instance
    :return pychord.Chord: Chord instance
    """
    if isinstance(chord, Chord):
        return chord
    elif isinstance(chord, str):
        return Chord(chord)
    else:
        raise TypeError("input type should be str or Chord instance.")
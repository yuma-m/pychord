# -*- coding: utf-8 -*-


from .parser import parse
from .utils import transpose_note, display_appended, display_on


class Chord(object):
    """ Class to handle a chord.

    :param str chord: Name of the chord. (e.g. C, Am7, F#m7-5/A)
    :param str _root: The root note of chord.
    :param pychord.Quality _quality: The quality of chord. ex) m7, 6, M9, ...
    :param str _on: The base note of slash chord.
    """
    def __init__(self, chord):
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
        return self._chord == other.chord

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

    def transpose(self, trans):
        """ Transpose the chord

        :param int trans: Transpose key
        :return:
        """
        if not isinstance(trans, int):
            raise TypeError("Expected integers, not {}".format(type(trans)))
        self._root = transpose_note(self._root, trans)
        if self._on:
            self._on = transpose_note(self._on, trans)
        self._reconfigure_chord()

    def components(self, visible=True):
        """ Return the component notes of chord

        :param bool visible: returns the name of notes if True else list of int
        :rtype: list[(str or int)]
        :return component notes of chord
        """
        return self._quality.get_components(root=self._root, visible=visible)

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
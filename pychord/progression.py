# -*- coding: utf-8 -*-

from .chord import as_chord, Chord


class ChordProgression(object):
    """ Class to handle chord progressions.

    :param list[pychord.Chord] _chords: component chords of chord progression.
    """

    def __init__(self, initial_chords=None):
        """ Constructor of ChordProgression instance.

        :type initial_chords: str|pychord.Chord|list
        :param initial_chords: Initial chord or chords of the chord progressions
        """
        if initial_chords is None:
            initial_chords = []
        if isinstance(initial_chords, Chord):
            self._chords = [initial_chords]
        elif isinstance(initial_chords, str):
            self._chords = [as_chord(initial_chords)]
        elif isinstance(initial_chords, list):
            self._chords = [as_chord(chord) for chord in initial_chords]
        else:
            raise TypeError("Cannot initialize ChordProgression with argument of {} type".format(type(initial_chords)))

    def __unicode__(self):
        return " | ".join([chord.chord for chord in self._chords])

    def __str__(self):
        return " | ".join([chord.chord for chord in self._chords])

    def __repr__(self):
        return "<ChordProgression: {}>".format(" | ".join([chord.chord for chord in self._chords]))

    def __add__(self, other):
        self._chords += other.chords
        return self

    def __len__(self):
        return len(self._chords)

    def __getitem__(self, item):
        return self._chords[item]

    @property
    def chords(self):
        """ Get component chords of chord progression

        :rtype: list[pychord.Chord]
        """
        return self._chords

    def append(self, chord):
        """ Append a chord to chord progressions

        :type chord: str|pychord.Chord
        :param chord: A chord to append
        :return:
        """
        self._chords.append(as_chord(chord))

    def insert(self, index, chord):
        """ Insert a chord to chord progressions

        :param int index: Index to insert a chord
        :type chord: str|pychord.Chord
        :param chord: A chord to insert
        :return:
        """
        self._chords.insert(index, as_chord(chord))

    def pop(self, index=-1):
        """ Pop a chord from chord progressions

        :param int index: Index of the chord to pop (default: -1)
        :return pychord.Chord:
        """
        return self._chords.pop(index)

    def transpose(self, trans):
        """ Transpose whole chord progressions

        :param int trans: Transpose key
        :return:
        """
        for chord in self._chords:
            chord.transpose(trans)

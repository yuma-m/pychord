# -*- coding: utf-8 -*-

from .chord import as_chord, Chord


class ChordProgression(object):
    """ Class to handle chord progressions.

    :type initial_chords: str|pychord.Chord|list
    :param initial_chords: Initial chord or chords of the chord progressions
    """

    def __init__(self, initial_chords=None):
        if initial_chords is None:
            initial_chords = []
        if isinstance(initial_chords, Chord):
            self.chords = [initial_chords]
        elif isinstance(initial_chords, str):
            self.chords = [as_chord(initial_chords)]
        elif isinstance(initial_chords, list):
            self.chords = [as_chord(chord) for chord in initial_chords]
        else:
            raise TypeError("Cannot initialize ChordProgression with argument of {} type".format(type(initial_chords)))

    def get_chords(self):
        return self.chords

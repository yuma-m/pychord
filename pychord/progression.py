from typing import Union, List

from .chord import Chord


class ChordProgression:
    """ Class to handle chord progressions.

    Attributes:
        _chords: component chords of chord progression.
    """

    def __init__(self, initial_chords: Union[str, Chord, List[Union[str, Chord]]] = []):
        """ Constructor of ChordProgression instance.

        :param initial_chords: Initial chord or chords of the chord progressions
        """
        if isinstance(initial_chords, Chord):
            chords = [initial_chords]
        elif isinstance(initial_chords, str):
            chords = [self._as_chord(initial_chords)]
        elif isinstance(initial_chords, list):
            chords = [self._as_chord(chord) for chord in initial_chords]
        else:
            raise TypeError(
                f"Cannot initialize ChordProgression with argument of {type(initial_chords)} type")
        self._chords: List[Chord] = chords

    def __unicode__(self):
        return " | ".join([chord.chord for chord in self._chords])

    def __str__(self):
        return " | ".join([chord.chord for chord in self._chords])

    def __repr__(self):
        return f"<ChordProgression: {' | '.join([chord.chord for chord in self._chords])}>"

    def __add__(self, other):
        self._chords += other.chords
        return self

    def __len__(self):
        return len(self._chords)

    def __getitem__(self, item):
        return self._chords[item]

    def __setitem__(self, key, value):
        self._chords[key] = value

    def __eq__(self, other):
        if not isinstance(other, ChordProgression):
            raise TypeError(
                f"Cannot compare ChordProgression object with {type(other)} object")
        if len(self) != len(other):
            return False
        for c, o in zip(self, other):
            if c != o:
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def chords(self) -> List[Chord]:
        """ Get component chords of chord progression """
        return self._chords

    def append(self, chord: Union[str, Chord]) -> None:
        """ Append a chord to chord progressions

        :param chord: A chord to append
        """
        self._chords.append(self._as_chord(chord))

    def insert(self, index: int, chord: Union[str, Chord]) -> None:
        """ Insert a chord to chord progressions

        :param index: Index to insert a chord
        :param chord: A chord to insert
        """
        self._chords.insert(index, self._as_chord(chord))

    def pop(self, index: int = -1) -> Chord:
        """ Pop a chord from chord progressions

        :param index: Index of the chord to pop (default: -1)
        """
        return self._chords.pop(index)

    def transpose(self, trans: int) -> None:
        """ Transpose whole chord progressions

        :param trans: Transpose key
        """
        for chord in self._chords:
            chord.transpose(trans)

    @staticmethod
    def _as_chord(chord: Union[str, Chord]) -> Chord:
        """ Convert from str to Chord instance if input is str

        :param chord: Chord name or Chord instance
        :return: Chord instance
        """
        if isinstance(chord, Chord):
            return chord
        elif isinstance(chord, str):
            return Chord(chord)
        else:
            raise TypeError("input type should be str or Chord instance.")

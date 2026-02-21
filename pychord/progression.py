from typing import Any

from .chord import Chord


class ChordProgression:
    """Class to handle chord progressions.

    Attributes:
        _chords: component chords of chord progression.
    """

    def __init__(
        self, initial_chords: str | Chord | list[str] | list[Chord] = []
    ) -> None:
        """Constructor of ChordProgression instance.

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
                f"Cannot initialize ChordProgression with argument of {type(initial_chords)} type"
            )
        self._chords: list[Chord] = chords

    def __str__(self) -> str:
        return " | ".join([chord.chord for chord in self._chords])

    def __repr__(self) -> str:
        return f"<ChordProgression: {self}>"

    def __add__(self, other: "ChordProgression") -> "ChordProgression":
        self._chords += other.chords
        return self

    def __len__(self) -> int:
        return len(self._chords)

    def __getitem__(self, key: int) -> Chord:
        return self._chords[key]

    def __setitem__(self, key: int, value: Chord) -> None:
        self._chords[key] = value

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ChordProgression):
            raise TypeError(
                f"Cannot compare ChordProgression object with {type(other)} object"
            )
        return self._chords == other._chords

    @property
    def chords(self) -> list[Chord]:
        """Get component chords of chord progression"""
        return self._chords

    def append(self, chord: str | Chord) -> None:
        """Append a chord to chord progressions

        :param chord: A chord to append
        """
        self._chords.append(self._as_chord(chord))

    def insert(self, index: int, chord: str | Chord) -> None:
        """Insert a chord to chord progressions

        :param index: Index to insert a chord
        :param chord: A chord to insert
        """
        self._chords.insert(index, self._as_chord(chord))

    def pop(self, index: int = -1) -> Chord:
        """Pop a chord from chord progressions

        :param index: Index of the chord to pop (default: -1)
        """
        return self._chords.pop(index)

    def transpose(self, trans: int) -> None:
        """Transpose whole chord progressions

        :param trans: Transpose key
        """
        for chord in self._chords:
            chord.transpose(trans)

    @staticmethod
    def _as_chord(chord: str | Chord) -> Chord:
        """Convert from str to Chord instance if input is str

        :param chord: Chord name or Chord instance
        :return: Chord instance
        """
        if isinstance(chord, Chord):
            return chord
        elif isinstance(chord, str):
            return Chord(chord)
        else:
            raise TypeError("input type should be str or Chord instance.")

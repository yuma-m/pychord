import copy
from typing import Any

from .chord import Chord


class ChordProgression:
    """
    A chord progression, which is a sequence of :class:`Chord` instances.

    :class:`Chord` instances passed to the progression are copied, so later
    changes to them do not affect the progression and vice versa.

    :param initial_chords: Initial chord or chords of the chord progression.
    """

    def __init__(
        self, initial_chords: str | Chord | list[str] | list[Chord] | None = None
    ) -> None:
        chords: list[Chord]
        if initial_chords is None:
            chords = []
        elif isinstance(initial_chords, (str, Chord)):
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
        return ChordProgression(self._chords + other._chords)

    def __len__(self) -> int:
        return len(self._chords)

    def __getitem__(self, key: int) -> Chord:
        return self._chords[key]

    def __setitem__(self, key: int, value: str | Chord) -> None:
        self._chords[key] = self._as_chord(value)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ChordProgression):
            raise TypeError(
                f"Cannot compare ChordProgression object with {type(other)} object"
            )
        return self._chords == other._chords

    @property
    def chords(self) -> list[Chord]:
        """
        A copy of the list of component chords.

        Modifying the returned list does not change the progression; use
        :meth:`append`, :meth:`insert`, :meth:`pop` or item assignment instead.
        """
        return list(self._chords)

    def append(self, chord: str | Chord) -> None:
        """
        Append a chord to the chord progression.

        :param chord: A chord to append.
        """
        self._chords.append(self._as_chord(chord))

    def insert(self, index: int, chord: str | Chord) -> None:
        """
        Insert a chord into the chord progression.

        :param index: Index to insert a chord.
        :param chord: A chord to insert.
        """
        self._chords.insert(index, self._as_chord(chord))

    def pop(self, index: int = -1) -> Chord:
        """
        Pop a chord from the chord progression.

        :param index: Index of the chord to pop (default: -1).
        """
        return self._chords.pop(index)

    def transpose(self, trans: int) -> None:
        """
        Transpose the whole chord progression.

        :param trans: The number of semitones.
        """
        for chord in self._chords:
            chord.transpose(trans)

    @staticmethod
    def _as_chord(chord: str | Chord) -> Chord:
        """Convert from str to Chord instance, or copy a Chord instance.

        :param chord: Chord name or :class:`Chord` instance.
        """
        if isinstance(chord, Chord):
            return copy.deepcopy(chord)
        elif isinstance(chord, str):
            return Chord(chord)
        else:
            raise TypeError("input type should be str or Chord instance.")

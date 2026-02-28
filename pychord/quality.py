import copy
import functools
import re
from typing import Any, Literal, overload

from .constants.qualities import DEFAULT_QUALITIES
from .constants.scales import RELATIVE_KEY_DICT
from .utils import note_to_val


class Quality:
    """Chord quality"""

    def __init__(self, name: str, intervals: tuple[str, ...]) -> None:
        """Constructor of chord quality

        :param name: name of quality
        :param components: components of quality
        """
        self._quality: str = name
        self._intervals = intervals

    def __str__(self) -> str:
        return self._quality

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Quality):
            raise TypeError(f"Cannot compare Quality object with {type(other)} object")
        return self.components == other.components

    @property
    def components(self) -> tuple[int, ...]:
        return tuple(_get_interval_pitch(i) for i in self._intervals)

    @property
    def quality(self) -> str:
        """Get name of quality"""
        return self._quality

    @overload
    def get_components(self, root: str, visible: Literal[True]) -> list[str]: ...

    @overload
    def get_components(self, root: str, visible: Literal[False]) -> list[int]: ...

    @overload
    def get_components(self, root: str, visible: bool) -> list[str] | list[int]: ...

    def get_components(
        self, root: str = "C", visible: bool = False
    ) -> list[str] | list[int]:
        """Get components of chord quality

        :param str root: the root note of the chord
        :param bool visible: returns the name of notes if True
        :rtype: list[str|int]
        :return: components of chord quality
        """
        if visible:
            return [_apply_interval_to_note(root, i) for i in self._intervals]
        else:
            root_val = note_to_val(root)
            return [v + root_val for v in self.components]


class QualityManager:
    """Singleton class to manage the qualities"""

    def __new__(cls) -> "QualityManager":
        if not hasattr(cls, "_instance"):
            cls._instance = super(QualityManager, cls).__new__(cls)
            cls._instance.load_default_qualities()
        return cls._instance

    def load_default_qualities(self) -> None:
        self._qualities = {q: Quality(q, c) for q, c in DEFAULT_QUALITIES}

    def get_quality(self, name: str, inversion: int = 0) -> Quality:
        if name not in self._qualities:
            raise ValueError(f"Unknown quality: {name}")
        # Create a new instance not to affect any existing instances
        q = copy.deepcopy(self._qualities[name])
        # apply requested inversion :
        for i in range(inversion):
            max_a, max_o = _parse_interval(q._intervals[-1])
            a, o = _parse_interval(q._intervals[0])
            while o < max_o:
                o += 7
            q._intervals = q._intervals[1:] + (f"{a}{o + 1}",)
        return q

    def get_qualities(self) -> dict[str, Quality]:
        return dict(self._qualities)

    def set_quality(self, name: str, intervals: tuple[str, ...]) -> None:
        """Set a Quality

        This method will not affect any existing Chord instances.
        :param name: name of quality
        :param intervals: intervals of quality
        """
        self._qualities[name] = Quality(name, intervals)

    def find_quality_from_components(self, components: list[int]) -> Quality | None:
        """Find a quality from components

        :param components: components of quality
        """
        for q in self._qualities.values():
            if list(q.components) == components:
                return copy.deepcopy(q)
        return None


def _apply_interval_to_note(root: str, interval: str) -> str:
    alterations, offset = _parse_interval(interval)

    # Apply the interval and alteration.
    notes_in_key = _scale_notes(root, "maj")
    note = notes_in_key[offset % 7]
    for alteration in alterations:
        if alteration == "#":
            note = _augment(note)
        else:
            note = _diminish(note)
    return note


def _get_interval_pitch(interval: str) -> int:
    alterations, offset = _parse_interval(interval)

    value = RELATIVE_KEY_DICT["maj"][offset % 7] + 12 * (offset // 7)
    for alteration in alterations:
        if alteration == "#":
            value += 1
        else:
            value -= 1
    return value


def _parse_interval(interval: str) -> tuple[str, int]:
    m = re.match(r"^([b#]*)(\d+)$", interval)
    assert m, f"Invalid interval {interval}"
    alterations = m.group(1)
    offset = int(m.group(2)) - 1
    return alterations, offset


def _augment(note: str) -> str:
    """
    Augment the given note.
    """
    if note.endswith("b"):
        return note[:-1]
    else:
        return note + "#"


def _diminish(note: str) -> str:
    """
    Diminish the given note.
    """
    if note.endswith("#"):
        return note[:-1]
    else:
        return note + "b"


@functools.lru_cache()
def _scale_notes(root: str, mode: str) -> list[str]:
    """
    Return the list of note names in the given major scale.
    """
    alphabet = ["C", "D", "E", "F", "G", "A", "B"]
    root_val = note_to_val(root)

    # Determine whether we use a flatted or sharped scale.
    if root == "F" or len(root) > 1 and root[1] == "b":
        alter = _diminish
    else:
        alter = _augment

    # Name notes in the key.
    notes = [root]
    index = alphabet.index(root[0])
    for offset in RELATIVE_KEY_DICT[mode][1:-1]:
        index = (index + 1) % 7
        note_val = (root_val + offset) % 12

        # Find the accidental to match the pitch.
        letter = alphabet[index]
        for note in [
            _diminish(_diminish(letter)),
            _diminish(letter),
            letter,
            _augment(letter),
            _augment(_augment(letter)),
        ]:
            if note_to_val(note) == note_val:
                notes.append(note)
                break
            note = alter(note)
        else:
            raise ValueError(f"{root}{mode} scale requires too many accidentals")

    return notes

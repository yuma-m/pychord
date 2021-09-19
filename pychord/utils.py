from typing import List

from .constants import NOTE_VAL_DICT, SCALE_VAL_DICT


def note_to_val(note: str) -> int:
    """ Get index value of a note

    >>> note_to_val("C")
    0
    >>> note_to_val("B")
    11
    """
    if note not in NOTE_VAL_DICT:
        raise ValueError(f"Unknown note {note}")
    return NOTE_VAL_DICT[note]


def val_to_note(val: int, scale: str = "C") -> str:
    """ Return note by index in a scale

    >>> val_to_note(0)
    "C"
    >>> val_to_note(11, "D")
    "D#"
    """
    val %= 12
    return SCALE_VAL_DICT[scale][val]


def transpose_note(note: str, transpose: int, scale: str = "C") -> str:
    """ Transpose a note

    >>> transpose_note("C", 1)
    "Db"
    >>> transpose_note("D", 4, "A")
    "F#"
    """
    val = note_to_val(note)
    val += transpose
    return val_to_note(val, scale)


def display_appended(appended: List[str]) -> str:
    # TODO: Implement this
    return ""


def display_on(on_note: str) -> str:
    if on_note:
        return f"/{on_note}"
    return ""

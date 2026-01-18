from typing import List, Optional

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


def val_to_note(val: int, scale: str = "C", index: Optional[int] = None, quality: Optional[str] = None) -> str:
    """ Return note by index in a scale

    >>> val_to_note(0)
    "C"
    >>> val_to_note(11, "D")
    "D#"
    """
    def process(n: str) -> str:
        return n.replace("#b", "").replace("b#", "")

    val %= 12
    if index is None or quality is None:
        return SCALE_VAL_DICT[scale][val]
    if (quality.find("b5") >= 1 or quality.find("-5") >= 1) and index == 2:
        temp = SCALE_VAL_DICT[scale][val + 1 % 12]
        return process(f"{temp}b")
    if (quality.find("#5") >= 1 or quality.find("+5") >= 1) and index == 2:
        temp = SCALE_VAL_DICT[scale][val - 1 % 12]
        return process(f"{temp}#")
    if (quality.find("b9") >= 1 or quality.find("-9") >= 1) and index == 4:
        temp = SCALE_VAL_DICT[scale][val + 1 % 12]
        return process(f"{temp}b")
    if (quality.find("#9") >= 1 or quality.find("+9") >= 1) and index == 4:
        temp = SCALE_VAL_DICT[scale][val - 1 % 12]
        return process(f"{temp}#")
    if (quality.find("7#11") >= 0 or quality.find("7+11") >= 0) and index == 5:
        temp = SCALE_VAL_DICT[scale][val - 1 % 12]
        return process(f"{temp}#")
    if (quality in ("13#11", "13+11")) and index == 5:
        temp = SCALE_VAL_DICT[scale][val - 1 % 12]
        return process(f"{temp}#")
    if (quality.find("9#11") >= 0 or quality.find("9+11") >= 0) and index == 6:
        temp = SCALE_VAL_DICT[scale][val - 1 % 12]
        return process(f"{temp}#")

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

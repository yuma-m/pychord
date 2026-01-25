from typing import List, Optional

from .constants import NOTE_VAL_DICT, SCALE_VAL_DICT


def note_to_val(note: str) -> int:
    """Get index value of a note

    >>> note_to_val("C")
    0
    >>> note_to_val("B")
    11
    """
    if note not in NOTE_VAL_DICT:
        raise ValueError(f"Unknown note {note}")
    return NOTE_VAL_DICT[note]


def val_to_note(
    val: int,
    root: str = "C",
    quality: Optional[str] = None,
    index: Optional[int] = None,
) -> str:
    """Return note by index in a scale
    val: index value of note
    root: root note of the chord
    quality: quality of the chord
    index: index of the note in the chord

    >>> val_to_note(0)
    "C"
    >>> val_to_note(1, "A")
    "D#"
    >>> val_to_note(1, "B")
    "Cb"
    >>> val_to_note(3, "C", "m", 1)
    "Eb"
    >>> val_to_note(3, "B", "maj", 1)
    "D#"
    """
    val %= 12
    if index is None or quality is None:
        return SCALE_VAL_DICT[root][val]

    # NOTE: Is there a better way to implement this?
    is_flatted = (
        (quality.startswith("dim") and index == 1)
        or (
            (
                quality.find("b5") >= 1
                or quality.find("-5") >= 1
                or quality.startswith("dim")
            )
            and index == 2
        )
        or ((quality == "dim7") and index == 3)
        or ((quality.find("b9") >= 1 or quality.find("-9") >= 1) and index == 4)
        # TODO: Remove special logic below for Gm
        or (
            val == 10
            and index == 1
            and (
                (quality.startswith("m") and not quality.startswith("maj"))
                or quality.startswith("dim")
            )
        )
    )
    if is_flatted:
        temp = SCALE_VAL_DICT[root][(val + 1) % 12]
        return f"{temp}b".replace("#b", "")

    is_sharped = (
        (
            (quality.find("#5") >= 1 or quality.find("+5") >= 1 or quality == "aug")
            and index == 2
        )
        or ((quality.find("#9") >= 1 or quality.find("+9") >= 1) and index == 4)
        or ((quality.find("7#11") >= 0 or quality.find("7+11") >= 0) and index == 5)
        or ((quality in ("13#11", "13+11")) and index == 5)
        or ((quality.find("9#11") >= 0 or quality.find("9+11") >= 0) and index == 6)
    )
    if is_sharped:
        temp = SCALE_VAL_DICT[root][(val - 1) % 12]
        return f"{temp}#".replace("b#", "")

    return SCALE_VAL_DICT[root][val]


def transpose_note(note: str, transpose: int, scale: str = "C") -> str:
    """Transpose a note

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

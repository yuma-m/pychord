from .constants import SCALE_VAL_DICT
from .constants.scales import NOTE_VALUES


def note_to_val(note: str) -> int:
    """Get index value of a note

    >>> note_to_val("C")
    0
    >>> note_to_val("B")
    11
    """
    try:
        pitch = NOTE_VALUES[note[0]]
    except KeyError:
        raise ValueError(f"Unknown note {note}")
    for alteration in note[1:]:
        if alteration == "b":
            pitch -= 1
        else:
            pitch += 1
    return pitch % 12


def transpose_note(note: str, transpose: int, scale: str = "C") -> str:
    """Transpose a note

    >>> transpose_note("C", 1)
    "Db"
    >>> transpose_note("D", 4, "A")
    "F#"
    """
    val = note_to_val(note)
    val += transpose
    return SCALE_VAL_DICT[scale][val % 12]

from typing import Tuple, List

from .quality import QualityManager, Quality
from .utils import NOTE_VAL_DICT


def parse(chord: str) -> Tuple[str, Quality, List[str], str]:
    """ Parse a string to get chord component

    :param chord: str expression of a chord
    :return: (root, quality, appended, on)
    """

    if len(chord) > 1 and chord[1] in ("b", "#"):
        root = chord[:2]
        rest = chord[2:]
    else:
        root = chord[:1]
        rest = chord[1:]

    def check_note(note: str):
        """ Raise ValueError if note is invalid """
        if note not in NOTE_VAL_DICT:
            raise ValueError(f"Invalid note {note}")

    check_note(root)
    on_chord_idx = rest.find("/")
    if on_chord_idx >= 0:
        on = rest[on_chord_idx + 1:]
        rest = rest[:on_chord_idx]
        check_note(on)
    else:
        on = ""
    quality = QualityManager().get_quality(rest)
    # TODO: Implement parser for appended notes
    appended: List[str] = []
    return root, quality, appended, on

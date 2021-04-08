# -*- coding: utf-8 -*-

from .quality import QualityManager
from .utils import NOTE_VAL_DICT


def parse(chord):
    """ Parse a string to get chord component

    :param str chord: str expression of a chord
    :rtype: (str, pychord.Quality, str, str)
    :return: (root, quality, appended, on)
    """

    if len(chord) > 1 and chord[1] in ("b", "#"):
        root = chord[:2]
        rest = chord[2:]
    else:
        root = chord[:1]
        rest = chord[1:]

    check_note(root, chord)
    on_chord_idx = rest.find("/")
    if on_chord_idx >= 0:
        on = rest[on_chord_idx + 1:]
        rest = rest[:on_chord_idx]
        check_note(on, chord)
    else:
        on = None
    quality = QualityManager().get_quality(rest)
    # TODO: Implement parser for appended notes
    appended = []
    return root, quality, appended, on


def check_note(note, chord):
    """ Return True if the note is valid.

    :param str note: note to check its validity
    :param str chord: the chord which includes the note
    :rtype: bool
    """
    if note not in NOTE_VAL_DICT:
        raise ValueError("Invalid chord {}: Unknown note {}".format(chord, note))
    return True

# -*- coding: utf-8 -*-

from .quality import Quality
from .constants import QUALITY_DICT
from .utils import NOTE_VAL_DICT


def parse(chord):
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
    if rest in QUALITY_DICT:
        quality = Quality(rest)
    else:
        raise ValueError("Invalid chord {}: Unknown quality {}".format(chord, rest))
    appended = []
    return root, quality, appended, on


def check_note(note, chord):
    if note not in NOTE_VAL_DICT:
        raise ValueError("Invalid chord {}: Unknown note {}".format(chord, note))
    return True

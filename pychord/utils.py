# -*- coding: utf-8 -*-

from .constants import NOTE_VAL_DICT, SCALE_VAL_DICT


def note_to_val(note):
    if note not in NOTE_VAL_DICT:
        raise ValueError("Unknown note {}".format(note))
    return NOTE_VAL_DICT[note]


def val_to_note(val, scale="C"):
    val = val % 12
    return SCALE_VAL_DICT[scale][val]


def transpose_note(note, transpose):
    val = note_to_val(note)
    val += transpose
    return val_to_note(val)


def display_appended(appended):
    # TODO: Implement this
    return ""


def display_on(on_note):
    if on_note:
        return "/{}".format(on_note)
    return ""

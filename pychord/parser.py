# -*- coding: utf-8 -*-

from .quality import Quality
from .constants import QUALITY_DICT
from .constants.scales import RELATIVE_KEY_DICT, FLATTED_SCALE
from .utils import NOTE_VAL_DICT, note_to_val, transpose_note


def parse(chord):
    """ Parse a string to get chord component

    :param str chord: str expression of a chord
    :rtype: (str, pychord.Quality, str, str)
    :return: (root, quality, appended, on)
    """
    # For main chord
    output = chord.split('$')
    if len(output) == 2:
        chord = output[0]
        key = output[1]
    else:
        chord = output[0]
        key = []
    if len(chord) > 1 and chord[1] in ("b", "#"):
        root = chord[:2]
        rest = chord[2:]
    else:
        root = chord[:1]
        rest = chord[1:]

    # check if chord is numeric
    numeric_condition = 0
    for numeric_key in range(0,10):
        numeric_condition += 1 if (str(root[0]) == str(numeric_key)) else 0
    if ( numeric_condition ): # if numeric chord
        # Determine scale quality
        if key != []:
            if len(key) > 1 and chord[1] in ("b", "#"):
                key_root = key[:2]
                key_rest = key[2:]
            else:
                key_root = key[:1]
                key_rest = key[1:]
            relative_key = RELATIVE_KEY_DICT[key_rest][int(root)-1]
            root = FLATTED_SCALE[\
                relative_key\
            ] # shift root relative to C scale
            transpose = note_to_val(key_root) - note_to_val('C') # shift scale relative to C key
            root = transpose_note(root, transpose) # transpose root
        else:
            raise ValueError("No key specified for chord {}.".format(chord))

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

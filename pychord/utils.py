# -*- coding: utf-8 -*-

from .constants import NOTE_VAL_DICT, SCALE_VAL_DICT, SHARPED_SCALE


def note_to_val(note):
    """ Convert note to int

    >>> note_to_val("C")
    0
    >>> note_to_val("B")
    11

    :type note: str
    :rtype: int
    """
    if note not in NOTE_VAL_DICT:
        raise ValueError("Unknown note {}".format(note))
    return NOTE_VAL_DICT[note]


def val_to_note(val, scale="C"):
    """ Convert int to note

    >>> val_to_note(0)
    "C"
    >>> val_to_note(11, "D")
    "D#"

    :type val: int
    :param str scale: key scale
    :rtype: str
    """
    val %= 12
    return SCALE_VAL_DICT[scale][val]


def transpose_note(note, transpose, scale="C"):
    """ Transpose a note

    :param str note: note to transpose
    :type transpose: int
    :param str scale: key scale
    :rtype: str
    :return: transposed note
    """
    val = note_to_val(note)
    val += transpose
    return val_to_note(val, scale)


def display_appended(appended):
    # TODO: Implement this
    return ""


def display_on(on_note):
    if on_note:
        return "/{}".format(on_note)
    return ""

def sharp_or_flat(scale):
    """ Determine whether the scale provided uses flats or sharps

        sharp_or_flat('Cmaj') returns flats => 'FLATTED'
        sharp_or_flat('C#min') returns sharps => 'SHARPED'
        
        :param str scale: Base scale (Cmaj, Amin, F#maj, Ebmin, ...)
        :rtype: str
        """
    root = scale[:-3]
    # if scale is minor, get sharp/flat from relative major
    if scale[-3:] == 'min':
        root = SCALE_VAL_DICT[root][3]
    
    # figure out whether sharps or flats are correct
    if SCALE_VAL_DICT[root] == SHARPED_SCALE:
        return 'SHARPED'
    else:
        return 'FLATTED'
    

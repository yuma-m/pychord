# -*- coding: utf-8 -*-

NOTE_VAL_DICT = {
    'Ab': 8,
    'A': 9,
    'A#': 10,
    'Bb': 10,
    'B': 11,
    'Cb': 11,
    'C': 0,
    'C#': 1,
    'Db': 1,
    'D': 2,
    'D#': 3,
    'Eb': 3,
    'E': 4,
    'F': 5,
    'F#': 6,
    'Gb': 6,
    'G': 7,
    'G#': 8,
}


VAL_NOTE_DICT = {
    0: ['C'],
    1: ['Db', 'C#'],
    2: ['D'],
    3: ['Eb', 'D#'],
    4: ['E'],
    5: ['F'],
    6: ['F#', 'Gb'],
    7: ['G'],
    8: ['Ab', 'G#'],
    9: ['A'],
    10: ['Bb', 'A#'],
    11: ['B', 'Cb']
}


def note_to_val(note):
    if note not in NOTE_VAL_DICT:
        raise ValueError("Unknown note {}".format(note))
    return NOTE_VAL_DICT[note]


def val_to_note(val):
    val = val % 12
    return VAL_NOTE_DICT[val][0]

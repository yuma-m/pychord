# -*- coding: utf-8 -*-

from .chord import Chord
from .utils import note_to_val


def note_to_chord(notes):
    """ convert note list to chord list

    :param list[str] notes: list of note arranged from lower note. ex) ["C", "Eb", "G"]
    :return list[pychord.Chord]: list of chord.
    """
    chords = []
    if not notes:
        raise ValueError("Please specify notes which consist a chord.")
    root = notes[0]
    positions = notes_to_positions(notes, root)


def notes_to_positions(notes, root):
    """ Get notes positions.

    ex) notes_to_positions(["C", "E", "G"], "C") -> [0, 4, 7]

    :param list[str] notes: list of notes
    :param str root: the root note
    :return list[int]: list of note positions
    """
    root_pos = note_to_val(root)
    current_pos = root_pos
    positions = []
    for note in notes:
        note_pos = note_to_val(note)
        if note_pos < current_pos:
            note_pos += 12 * ((current_pos - note_pos) / 12 + 1)
        positions.append(note_pos - root_pos)
        current_pos = note_pos
    return positions

# -*- coding: utf-8 -*-

from .chord import Chord
from .constants.qualities import QUALITY_DICT
from .utils import note_to_val


def note_to_chord(notes):
    """ Convert note list to chord list

    :param list[str] notes: list of note arranged from lower note. ex) ["C", "Eb", "G"]
    :rtype: list[pychord.Chord]
    :return: list of chord
    """
    if not notes:
        raise ValueError("Please specify notes which consist a chord.")
    root = notes[0]
    root_and_positions = []
    for rotated_notes in get_all_rotated_notes(notes):
        rotated_root = rotated_notes[0]
        root_and_positions.append([rotated_root, notes_to_positions(rotated_notes, rotated_notes[0])])
    chords = []
    for temp_root, positions in root_and_positions:
        quality = find_quality(positions)
        if quality is None:
            continue
        if temp_root == root:
            chord = "{}{}".format(root, quality)
        else:
            chord = "{}{}/{}".format(temp_root, quality, root)
        chords.append(Chord(chord))
    return chords


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
            note_pos += 12 * ((current_pos - note_pos) // 12 + 1)
        positions.append(note_pos - root_pos)
        current_pos = note_pos
    return positions


def get_all_rotated_notes(notes):
    """ Get all rotated notes

    get_all_rotated_notes([1,3,5]) -> [[1,3,5],[3,5,1],[5,1,3]]

    :type notes: list[str]
    :rtype: list[list[str]]
    """
    notes_list = []
    for x in range(len(notes)):
        notes_list.append(notes[x:] + notes[:x])
    return notes_list


def find_quality(positions):
    """ Find a quality consists of positions

    :param list[int] positions: note positions
    :rtype: str|None
    """
    for q, p in QUALITY_DICT.items():
        if positions == p:
            return q
    return None

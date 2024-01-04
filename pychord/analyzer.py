from typing import List

from .chord import Chord
from .quality import QualityManager
from .utils import note_to_val


def find_chords_from_notes(notes: List[str]) -> List[Chord]:
    """ Find possible chords consisted from notes

    :param notes: List of note arranged from lower note. ex) ["C", "Eb", "G"]
    :return: List of chord
    """
    if not notes:
        raise ValueError("Please specify notes which consist a chord.")
    root = notes[0]
    root_and_positions = []
    for rotated_notes in get_all_rotated_notes(notes):
        rotated_root = rotated_notes[0]
        root_and_positions.append((rotated_root, notes_to_positions(rotated_notes, rotated_notes[0])))
    chords = []
    for temp_root, positions in root_and_positions:
        quality = QualityManager().find_quality_from_components(positions)
        if quality is None:
            continue
        if temp_root == root:
            chord = "{}{}".format(root, quality)
        else:
            chord = "{}{}/{}".format(temp_root, quality, root)
        chords.append(Chord(chord))
    return chords


def notes_to_positions(notes: List[str], root: str) -> List[int]:
    """ Get notes positions from the root note

    >>> notes_to_positions(["C", "E", "G"], "C")
    [0, 4, 7]

    :param notes: List of notes
    :param root: Root note
    :return: List of note positions
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


def get_all_rotated_notes(notes: List[str]) -> List[List[str]]:
    """ Get all rotated notes

    get_all_rotated_notes([A,C,E]) -> [[A,C,E],[C,E,A],[E,A,C]]
    """
    if len(notes) == 0:
        return []
    if len(notes) == 1:
        return [notes]
    if len(notes) == 2:
        return [[notes[0], notes[1]], [notes[1], notes[0]]]
    list_of_chords = []
    for i in range(0, len(notes)):
        m = notes[i]
        remaining_list = notes[:i] + notes[i + 1:]
        permutations_on_remaining_list = get_all_rotated_notes(remaining_list)
        for p in permutations_on_remaining_list:
            list_of_chords.append([m] + p)
    return list_of_chords

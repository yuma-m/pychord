# -*- coding: utf-8 -*-

from .constants import QUALITY_DICT
from .utils import note_to_val, val_to_note


class Quality(object):
    def __init__(self, quality):
        if quality not in QUALITY_DICT:
            raise ValueError("unknown quality {}".format(quality))
        self.quality = quality
        self.components = QUALITY_DICT[quality]

    def __unicode__(self):
        return self.quality

    def __str__(self):
        return self.quality

    def get_components(self, root='C', visible=False):
        root_val = note_to_val(root)
        components = [v + root_val for v in self.components]
        if visible:
            components = [val_to_note(c, scale=root) for c in components]
        return components

    def append_on_chord(self, on_chord, root):
        """Append on chord

        To create Am7/G
        q = Quality('m7')
        q.append_on_chord('G', root='A')
        """
        root_val = note_to_val(root)
        on_chord_val = note_to_val(on_chord) - root_val
        for idx, val in enumerate(self.components):
            if val % 12 == on_chord_val:
                scale = val / 12
                self._rotate_components(idx, scale)
                break
        if on_chord_val > root_val:
            on_chord_val -= 12
        if on_chord_val not in self.components:
            self.components.insert(0, on_chord_val)

    def _rotate_components(self, stop_idx, scale):
        for idx, val in enumerate(self.components[:stop_idx]):
            self.components[idx] += (scale + 1) * 12

    def append_note(self, note, root, scale=0):
        root_val = note_to_val(root)
        note_val = note_to_val(note) - root_val + scale * 12
        if note_val not in self.components:
            self.components.append(note_val)
            self.components.sort()

    def append_notes(self, notes, root, scale=0):
        for note in notes:
            self.append_note(note, root, scale)

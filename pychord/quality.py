# -*- coding: utf-8 -*-
import copy
from collections import OrderedDict

from .constants.qualities import DEFAULT_QUALITIES
from .utils import note_to_val, val_to_note


class Quality(object):
    """ Chord quality

    :param str _quality: str expression of chord quality
    """
    def __init__(self, name, components):
        """ Constructor of chord quality

        :param str name: name of quality
        :param Tuple[int]: components of quality
        """
        self._quality = name
        self.components = list(components)

    def __unicode__(self):
        return self._quality

    def __str__(self):
        return self._quality

    def __eq__(self, other):
        if not isinstance(other, Quality):
            raise TypeError("Cannot compare Quality object with {} object".format(type(other)))
        return self.components == other.components

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def quality(self):
        """ Get name of quality """
        return self._quality

    def get_components(self, root='C', visible=False):
        """ Get components of chord quality

        :param str root: the root note of the chord
        :param bool visible: returns the name of notes if True
        :rtype: list[str|int]
        :return: components of chord quality
        """
        root_val = note_to_val(root)
        components = [v + root_val for v in self.components]

        if visible:
            components = [val_to_note(c, scale=root) for c in components]

        return components

    def append_on_chord(self, on_chord, root):
        """ Append on chord

        To create Am7/G
        q = Quality('m7')
        q.append_on_chord('G', root='A')

        :param str on_chord: bass note of the chord
        :param str root: root note of the chord
        """
        root_val = note_to_val(root)
        on_chord_val = note_to_val(on_chord) - root_val

        list_ = list(self.components)
        for idx, val in enumerate(list_):
            if val % 12 == on_chord_val:
                self.components.remove(val)
                break

        if on_chord_val > root_val:
            on_chord_val -= 12

        if on_chord_val not in self.components:
            self.components.insert(0, on_chord_val)

    def append_note(self, note, root, scale=0):
        """ Append a note to quality

        :param str note: note to append on quality
        :param str root: root note of chord
        :param int scale: key scale
        """
        root_val = note_to_val(root)
        note_val = note_to_val(note) - root_val + scale * 12
        if note_val not in self.components:
            self.components.append(note_val)
            self.components.sort()

    def append_notes(self, notes, root, scale=0):
        """ Append notes to quality

        :param list[str] notes: notes to append on quality
        :param str root: root note of chord
        :param int scale: key scale
        """
        for note in notes:
            self.append_note(note, root, scale)


class QualityManager(object):
    """ Singleton class to manage the qualities """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(QualityManager, cls).__new__(cls)
            cls._instance.load_default_qualities()
        return cls._instance

    def load_default_qualities(self):
        self._qualities = OrderedDict([
            (q, Quality(q, c)) for q, c in DEFAULT_QUALITIES
        ])

    def get_quality(self, name):
        if name not in self._qualities:
            raise ValueError("Unknown quality: {}".format(name))
        # Create a new instance not to affect any existing instances
        return copy.deepcopy(self._qualities[name])

    def set_quality(self, name, components):
        """ Set a Quality

        This method will not affect any existing Chord instances.
        :param str name: name of quality
        :param Tuple[int] components: components of quality
        """
        self._qualities[name] = Quality(name, components)

    def find_quality_from_components(self, components):
        for q in self._qualities.values():
            if q.components == components:
                return copy.deepcopy(q)
        return None

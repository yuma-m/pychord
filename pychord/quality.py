import copy
from collections import OrderedDict
from typing import Tuple, List

from .constants.qualities import DEFAULT_QUALITIES
from .utils import note_to_val, val_to_note


class Quality:
    """ Chord quality """

    def __init__(self, name: str, components: Tuple[int, ...]):
        """ Constructor of chord quality

        :param name: name of quality
        :param components: components of quality
        """
        self._quality: str = name
        self.components: Tuple[int, ...] = components

    def __unicode__(self):
        return self._quality

    def __str__(self):
        return self._quality

    def __eq__(self, other):
        if not isinstance(other, Quality):
            raise TypeError(f"Cannot compare Quality object with {type(other)} object")
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

        components = list(self.components)
        for idx, val in enumerate(self.components):
            if val % 12 == on_chord_val:
                components.remove(val)
                break

        if on_chord_val > root_val:
            on_chord_val -= 12

        if on_chord_val not in components:
            components = [on_chord_val] + [
                v for v in components if v % 12 != on_chord_val % 12
            ]

        self.components = tuple(components)


class QualityManager:
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

    def get_quality(self, name: str, inversion: int = 0) -> Quality:
        if name not in self._qualities:
            raise ValueError(f"Unknown quality: {name}")
        # Create a new instance not to affect any existing instances
        q = copy.deepcopy(self._qualities[name])
        # apply requested inversion :
        for i in range(inversion):
            n = q.components[0]
            while n < q.components[-1]:
                n += 12
            q.components = q.components[1:] + (n,)
        return q

    def set_quality(self, name: str, components: Tuple[int, ...]):
        """ Set a Quality

        This method will not affect any existing Chord instances.
        :param name: name of quality
        :param components: components of quality
        """
        self._qualities[name] = Quality(name, components)

    def find_quality_from_components(self, components: List[int]):
        """ Find a quality from components

        :param components: components of quality
        """
        for q in self._qualities.values():
            if list(q.components) == components:
                return copy.deepcopy(q)
        return None

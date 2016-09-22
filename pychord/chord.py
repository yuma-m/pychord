# -*- coding: utf-8 -*-


from .parser import parse
from .utils import transpose_note, display_appended, display_on


class Chord(object):
    def __init__(self, chord):
        self.chord = chord
        self.root, self.quality, self.appended, self.on = "", "", "", ""
        self._parse(chord)

    def __unicode__(self):
        return self.chord

    def __str__(self):
        return self.chord

    def info(self):
        return """{}
root={}
quality={}
appended={}
on={}""".format(self.chord, self.root, self.quality, self.appended, self.on)

    def transpose(self, trans):
        if not isinstance(trans, int):
            raise TypeError("Expected integers, not {}".format(type(trans)))
        self.root = transpose_note(self.root, trans)
        if self.on:
            self.on = transpose_note(self.on, trans)
        self._reconfigure_chord()

    def components(self, visible=True):
        return self.quality.get_components(root=self.root, visible=visible)

    def _parse(self, chord):
        root, quality, appended, on = parse(chord)
        self.root = root
        self.quality = quality
        self.appended = appended
        self.on = on

    def _reconfigure_chord(self):
        # TODO: Use appended
        self.chord = "{}{}{}{}".format(self.root,
                                       self.quality.quality,
                                       display_appended(self.appended),
                                       display_on(self.on))

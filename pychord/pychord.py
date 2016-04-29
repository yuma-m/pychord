# -*- coding: utf-8 -*-

from __future__ import print_function

from parser import parse


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

    def _parse(self, chord):
        root, quality, appended, on = parse(chord)
        self.root = root
        self.quality = quality
        self.appended = appended
        self.on = on

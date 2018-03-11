pychord |Build Status| |Documentation Status|
=============================================

Overview
--------

Pychord is a python library to handle musical chords.

Installation
------------

.. code:: sh

    $ pip install pychord

Basic Usage
-----------

Create a Chord
~~~~~~~~~~~~~~

.. code:: python

    >>> from pychord import Chord
    >>> c = Chord("Am7")
    >>> c
    <Chord: Am7>
    >>> c.info()
    """
    Am7
    root=A
    quality=m7
    appended=[]
    on=None
    """

Transpose a Chord
~~~~~~~~~~~~~~~~~

.. code:: python

    >>> c = Chord("Am7/G")
    >>> c.transpose(3)
    >>> c
    <Chord: Cm7/Bb>

Get component notes
~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> c = Chord("Am7")
    >>> c.components()
    ['A', 'C', 'E', 'G']

Compare Chords
~~~~~~~~~~~~~~

.. code:: python

    >>> Chord("C") == Chord("D")
    False
    >>> Chord("C#") == Chord("Db")
    True
    >>> c = Chord("C")
    >>> c.transpose(2)
    >>> c == Chord("D")
    True

Find Chords
~~~~~~~~~~~

.. code:: python

    >>> from pychord import note_to_chord
    >>> note_to_chord(["C", "E", "G"])
    [<Chord: C>]
    >>> note_to_chord(["F#", "A", "C", "D"])
    [<Chord: D7/F#>]
    >>> note_to_chord(["F", "G", "C"])
    [<Chord: Fsus2>, <Chord: Csus4/F>]

Create and handle chord progressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> from pychord import ChordProgression
    >>> cp = ChordProgression(["C", "G/B", "Am"])
    >>> cp
    <ChordProgression: C | G/B | Am>

    >>> cp.append("Em/G")
    >>> cp
    <ChordProgression: C | G/B | Am | Em/G>

    >>> cp.transpose(+3)
    >>> cp
    <ChordProgression: Eb | Bb/D | Cm | Gm/Bb>

    >>> cp[1]
    <Chord: Bb/D>

Supported Python Versions
-------------------------

-  2.7
-  3.3 and above

Links
-----

-  PyPI: https://pypi.python.org/pypi/pychord
-  GitHub: https://github.com/yuma-m/pychord
-  Documentation: http://pychord.readthedocs.io/en/latest/

Author
------

-  `Yuma Mihira <http://yurax2.com/>`__

License
-------

-  MIT License

.. |Build Status| image:: https://travis-ci.org/yuma-m/pychord.svg?branch=master
   :target: https://travis-ci.org/yuma-m/pychord
.. |Documentation Status| image:: https://readthedocs.org/projects/pychord/badge/?version=latest
   :target: http://pychord.readthedocs.io/en/latest/?badge=latest

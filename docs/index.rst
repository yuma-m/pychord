PyChord
=======

PyChord is a Python library to handle musical chords: parse chord names,
transpose them, list their component notes, compare them, find chords from
notes and manage chord progressions.

.. code-block:: sh

   pip install pychord

.. code-block:: python

   >>> from pychord import Chord
   >>> c = Chord("Am7")
   >>> c.components()
   ['A', 'C', 'E', 'G']

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   pychord


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

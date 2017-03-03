# py-beep-music
Make Music with python vie beep

# Installation

`beep` has to be installed and you need to be allowed to execute it.

# Usage

Just execute one of the songs with python (eg. `python popcorn.py`).

To write play new songs you can use

```
from py_beep_music import *

# This array expects tuples like (note, length). Please use the constants in py_beep_music (A3, As3, VIERTEL etc)
tune = []

# You also can add a speed. This defaults to 150bpm
play(tune)
```

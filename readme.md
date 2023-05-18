Bricklights
===========

[![Build](https://github.com/jncraton/bricklights/actions/workflows/build.yml/badge.svg)](https://github.com/jncraton/bricklights/actions/workflows/build.yml)

A [Pybricks](https://pybricks.com/)-based lighting controller for LEGO models.

Installation
------------

Include bricklights.py in your PyBricks project.

Usage
-----

Here is an example demonstrating basic usage controlling 6 sets of LEDs in various patterns using an InventorHub:

```python
from pybricks.parameters import Port

from bricklights import Flame, Crossfader, Fader, Lerp

lights = [
    Crossfader([Port.A, Port.C, Port.E], period=30000, intensity=.6),
    Flame(Port.B, period=120, intensity=1.0),
    Lerp(Port.D, period=1000, keyframes=[0,5,20,100,20,5]),
    Fader(Port.F, period=1000, intensity=.5),
]

while True:
    for light in lights:
        light.update()
```

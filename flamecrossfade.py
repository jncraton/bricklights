from pybricks.parameters import Port
from pybricks.tools import wait

from bricklights import Flame, Crossfader

lights = [
    Crossfader([Port.A, Port.C, Port.E], period=30000),
    Flame(Port.B, period=50),
    Flame(Port.D, period=50),
    Flame(Port.F, period=50),
]

while 1:
    wait(10)
    for light in lights:
        light.update(10)

from pybricks.parameters import Port
from pybricks.tools import wait

from bricklights import Lerp, Flame

lights = [
    Lerp(Port.A, keyframes=[0,100,0,0,0,0], period=15000),
    Lerp(Port.C, keyframes=[0,0,0,100,0,0], period=15000),
    Lerp(Port.E, keyframes=[0,0,0,0,0,100], period=15000),
    Flame(Port.B, period=50),
    Flame(Port.D, period=50),
    Flame(Port.F, period=50),
]

while(1):
    wait(10)
    for light in lights:
        light.update()

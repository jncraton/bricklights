from pybricks.parameters import Port

from bricklights import Flame, Crossfader, Fader, Lerp

lights = [
    Crossfader([Port.A, Port.C, Port.E], period=30000, intensity=0.6),
    Flame(Port.B, period=120, intensity=1.0),
    Lerp(Port.D, period=1000, keyframes=[0, 0.05, 0.2, 1, 0.2, 0.05]),
    Fader(Port.F, period=1000, intensity=0.5),
]

while True:
    for light in lights:
        light.update()

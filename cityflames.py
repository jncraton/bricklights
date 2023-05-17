from pybricks.parameters import Port, Color
from pybricks.hubs import CityHub
from pybricks.tools import wait

from bricklights import Flame, RGBFlame

lights = [Flame(Port.A), Flame(Port.B), RGBFlame(CityHub().light, Color(30, 100, 100))]

while 1:
    wait(10)
    for light in lights:
        light.update()

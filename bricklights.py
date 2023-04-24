from pybricks.pupdevices import Light
from pybricks.parameters import Port
from pybricks.tools import wait

from urandom import randint

def update_flame(light):
    wait(75)
    light.on(randint(10,30))

light = Light(Port.A)

while True:
    update_flame(light)

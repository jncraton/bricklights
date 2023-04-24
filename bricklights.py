from pybricks.pupdevices import Light
from pybricks.parameters import Port
from pybricks.tools import wait

from urandom import randint

class ManagedLight:
    def __init__(self, port, speed=1.0, intensity=1.0):
        self.light = Light(port)
        self.speed = speed
        self.intensity = intensity
        self.time = 0

class Flame(ManagedLight):
    def update(self):
        self.time += 1

        if self.time % 8*self.speed == 0:
            self.light.on(randint(int(self.intensity*100-25),int(self.intensity*100)))

class Fader(ManagedLight):
    def update(self):
        self.time += 1

        step = (self.time*self.speed) % 200

        brightness = step if step < 100 else 200 - step

        self.light.on(brightness*self.intensity)

light1 = Flame(Port.A)
light2 = Flame(Port.C)
light3 = Fader(Port.E, speed=.1)

while(1):
    wait(10)
    light1.update()
    light2.update()
    light3.update()

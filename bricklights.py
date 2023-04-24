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

    def update(self):
        self.time += self.speed

class Steady(ManagedLight):
    def update(self):
        self.light.on(self.intensity*100)

class Flame(ManagedLight):
    def update(self):
        super().update()

        if self.time % 8 == 0:
            self.light.on(randint(int(self.intensity*100-25),int(self.intensity*100)))

class Fader(ManagedLight):
    def update(self):
        super().update()

        step = self.time % 200

        brightness = step if step < 100 else 200 - step

        self.light.on(brightness*self.intensity)

light1 = Flame(Port.A)
light2 = Steady(Port.C)
light3 = Fader(Port.E, speed=.1)

while(1):
    wait(10)
    light1.update()
    light2.update()
    light3.update()

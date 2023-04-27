from pybricks.pupdevices import Light
from pybricks.parameters import Port
from pybricks.tools import wait

from urandom import randint

class ManagedLight:
    def __init__(self, port, period=1000, intensity=1.0, time_offset=0):
        self.light = Light(port)
        self.period = period
        self.intensity = intensity
        self.time = time_offset

    def update(self):
        self.time += 10

class Steady(ManagedLight):
    def update(self):
        self.light.on(self.intensity*100)

class Flame(ManagedLight):
    def update(self):
        super().update()

        if self.time % self.period == 0:
            self.light.on(self.intensity*randint(25, 100))

class Fader(ManagedLight):
    def update(self):
        super().update()

        step = self.time % self.period

        brightness = step if step < self.period/2 else self.period - step

        self.light.on((100/self.period)*brightness*self.intensity)

light1 = Flame(Port.A, period=80)
light2 = Fader(Port.C, time_offset=5000, period=10000)
light3 = Fader(Port.E, period=10000)

while(1):
    wait(10)
    light1.update()
    light2.update()
    light3.update()

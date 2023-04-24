from pybricks.pupdevices import Light
from pybricks.parameters import Port
from pybricks.tools import wait

from urandom import randint

class Flame:
    def __init__(self, port, delay=8, intensity=30):
        self.light = Light(port)
        self.delay = delay
        self.intensity = intensity
        self.time = 0

    def update(self):
        self.time += 1

        if self.time % self.delay == 0:
            self.light.on(randint(self.intensity-25,self.intensity))

flame1 = Flame(Port.A)
flame2 = Flame(Port.C)
flame3 = Flame(Port.E)

while(1):
    wait(10)
    flame1.update()
    flame2.update()
    flame3.update()

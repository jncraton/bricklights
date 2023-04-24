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

class Fader:
    def __init__(self, port, speed=1, intensity=100):
        self.light = Light(port)
        self.speed = speed
        self.intensity = intensity
        self.time = 0

    def update(self):
        self.time += 1

        step = (self.time*self.speed) % 200

        brightness = step if step < 100 else 200 - step

        self.light.on(brightness*self.intensity/100)

light1 = Flame(Port.A)
light2 = Flame(Port.C)
light3 = Fader(Port.E, speed=.1)

while(1):
    wait(10)
    light1.update()
    light2.update()
    light3.update()

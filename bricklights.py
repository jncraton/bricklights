from pybricks.pupdevices import Light
from pybricks.parameters import Color
from pybricks.tools import StopWatch

from urandom import randint


class ManagedLight:
    def __init__(self, port, period=1000, intensity=1.0):
        self.light = Light(port)
        self.period = period
        self.intensity = intensity
        self.stopwatch = StopWatch()

    def update(self):
        if self.stopwatch.time() > self.period:
            self.stopwatch.reset()


class Steady(ManagedLight):
    def update(self):
        self.light.on(self.intensity * 100)


class Flame(ManagedLight):
    def __init__(self, port, period=120, intensity=1.0):
        super().__init__(port, period, intensity)

    def update(self):
        super().update()

        if self.stopwatch.time() == 0:
            self.light.on(self.intensity * randint(80, 100))


class Fader(ManagedLight):
    def update(self):
        super().update()

        step = self.stopwatch.time() % self.period

        brightness = step if step < self.period / 2 else self.period - step

        self.light.on((100 / self.period) * brightness * self.intensity)


class Lerp(ManagedLight):
    def __init__(self, port, period=1000, keyframes=[0, 100]):
        super().__init__(port, period, 1.0)
        self.keyframes = keyframes

    def update(self):
        super().update()

        n_float = len(self.keyframes) * self.stopwatch.time() / self.period
        n = int(n_float) % len(self.keyframes)
        weight = n_float % 1

        current = self.keyframes[n]
        upcoming = self.keyframes[(n + 1) % len(self.keyframes)]

        intensity = (1 - weight) * current + (weight) * upcoming

        self.light.on(intensity)


class Crossfader:
    def __init__(self, ports, period):
        self.period = period

        self.lights = []

        for i, port in enumerate(ports):
            keyframes = [0] * len(ports) * 2
            keyframes[i * 2] = 100

            self.lights.append(Lerp(port, keyframes=keyframes, period=self.period))

    def update(self):
        for light in self.lights:
            light.update()


class RGBFlame(ManagedLight):
    def __init__(self, light, color, period=120):
        self.light = light
        self.color = color
        self.period = period

    def update(self):
        super().update()

        if self.stopwatch.time() == 0:
            self.light.on(
                Color(self.color.h, self.color.s, self.color.v - randint(0, 20))
            )

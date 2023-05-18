from pybricks.pupdevices import Light
from pybricks.parameters import Color
from pybricks.tools import StopWatch

from urandom import randint


class ManagedLight:
    """Manages various types of lights supported by the module"""

    def __init__(self, port, period=1000, intensity=1.0):
        self.light = Light(port)
        self.period = period
        self.intensity = intensity
        self.stopwatch = StopWatch()

    def update(self):
        if self.stopwatch.time() > self.period:
            self.stopwatch.reset()


class Steady(ManagedLight):
    """A light that stays on"""

    def update(self):
        self.light.on(self.intensity * 100)


class Lerp(ManagedLight):
    """A light that fades between values

    This provides a high degree of control over a light pattern.

    Patterns are defined using a series of keyframes of varying intensities.
    """

    def __init__(self, port, period=1000, keyframes=[0, 1.0]):
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

        self.light.on(100*intensity)


class Fader(Lerp):
    """A light that fades on and off"""
    def __init__(self, port, period=1000, intensity=1.0):
        super().__init__(port, period, [0, 100*intensity])


class Crossfader:
    """A set of lights that fade in and out in sequence"""

    def __init__(self, ports, period, intensity=1.0):
        self.period = period

        self.lights = []

        for i, port in enumerate(ports):
            keyframes = [0] * len(ports) * 2
            keyframes[i * 2] = 100 * intensity

            self.lights.append(Lerp(port, keyframes=keyframes, period=self.period))

    def update(self):
        for light in self.lights:
            light.update()


class Flame(ManagedLight):
    """A light that flickers randomly like a flame"""

    def __init__(self, port, period=120, intensity=1.0):
        super().__init__(port, period, intensity)

    def update(self):
        if randint(0, self.period) < self.stopwatch.time():
            self.light.on(self.intensity * randint(80, 100))

        self.stopwatch.reset()


class RGBFlame(ManagedLight):
    """An RGB light that flickers randomly like a flame"""

    def __init__(self, light, color, period=120):
        self.light = light
        self.color = color
        self.period = period

    def update(self):
        if randint(0, self.period) < self.stopwatch.time():
            self.light.on(
                Color(self.color.h, self.color.s, self.color.v - randint(0, 20))
            )

        self.stopwatch.reset()

from pybricks.pupdevices import Light

from urandom import randint


class ManagedLight:
    def __init__(self, port, period=1000, intensity=1.0):
        self.light = Light(port)
        self.period = period
        self.intensity = intensity
        self.time = 0

    def update(self):
        self.time += 10
        if self.time > self.period:
            self.time = 0


class Steady(ManagedLight):
    def update(self):
        self.light.on(self.intensity * 100)


class Flame(ManagedLight):
    def update(self):
        super().update()

        if self.time == 0:
            self.light.on(self.intensity * randint(25, 100))


class Fader(ManagedLight):
    def update(self):
        super().update()

        step = self.time % self.period

        brightness = step if step < self.period / 2 else self.period - step

        self.light.on((100 / self.period) * brightness * self.intensity)


class Lerp(ManagedLight):
    def __init__(self, port, period=1000, keyframes=[0, 100]):
        super().__init__(port, period, 1.0)
        self.keyframes = keyframes

    def update(self):
        super().update()

        n_float = len(self.keyframes) * self.time / self.period
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

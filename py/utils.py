
from random import randint
import math


def any(a, ommitting = []):
    f = a[randint(0, len(a) - 1)]
    if f in ommitting:
        return any(a, ommitting)
    return f


class MovingAvg():
    def __init__(self, size):
        self.size = size
        self.clear()

    def clear(self):
        self.values = []
        self.avg = 0.0

    def add(self, v):
        self.avg += (v * 1.0 / self.size)
        self.values.append(v)
        if (len(self.values) > self.size):
            p = self.values.pop(0)
            self.avg -= (p * 1.0 / self.size)

    def first(self):
        return self.values[0]

    def value(self):
        return self.avg if (len(self.values) == self.size) else (self.avg * self.size / len(self.values))


class AbsMovingAvg(MovingAvg):
    def __init__(self, size):
        MovingAvg.__init__(self, size)

    def add(self, v):
        self.avg += (abs(v) * 1.0 / self.size)
        self.values.append(v)
        if (len(self.values) > self.size):
            p = self.values.pop(0)
            self.avg -= (abs(p) * 1.0 / self.size)


class DelayTimes():
    def __init__(self, tempo, intraBeat = False):
        msPer16th = 15000.0 / tempo
        if intraBeat:
            self.time = math.floor(4 * msPer16th)
            self.leftTap = 75
        else:
            max16thsPossible = math.floor(1300 / msPer16th)

            self.time = math.floor(max16thsPossible * msPer16th)
            self.leftTap = math.floor(100.0 * randint(2, max16thsPossible - 1) / max16thsPossible)


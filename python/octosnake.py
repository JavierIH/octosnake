import time
import math
from scipy import signal


class Oscillator(object):

    def __init__(self, signal=None,  period=2000, amplitude=50, phase=0, offset=0):
        self.period = period
        self.amplitude = amplitude
        self.phase = phase
        self.offset = offset
        self.stop = False
        self.ref_time = time.time()*1000
        self.delta_time = 0
        self.signal = signal or math.sin

    def refresh(self):
        self.delta_time = (time.time()*1000-self.ref_time*1000) % self.period
        self.output = self.amplitude*self.signal(self.time_to_radians(self.delta_time) + self.degrees_to_radians(self.phase)) + self.offset
        return self.output

    def reset(self):
        self.ref_time = time.time()*1000

    def time_to_radians(self, time):
        return float(time)*2*math.pi/self.period

    def degrees_to_radians(self, degrees):
        return float(degrees)*2*math.pi/360

    def degrees_to_time(self, degrees):
        return float(degrees)*self.period/360


def sawtooth(val):
    return signal.sawtooth(val)


def semiSin(val):
    out = math.sin(val)
    if out <= 0:
        out = 0
    return out


def triangle(self, val):
    # return (self.amplitude*2/math.pi)*math.asin(math.sin(val*2*math.pi/self.period))
    val += 1
    return abs((val % 2)-1)

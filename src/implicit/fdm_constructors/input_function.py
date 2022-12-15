import matplotlib.pyplot as plt
import json
from scipy import interpolate
import numpy as np


def input_f(dt, input_plot):
    f = open('signal.json')
    data = json.load(f)
    amplitude = data['amplitude']
    time = data['time']
    time = [i*1000000 for i in time]
    function = interpolate.interp1d(time, amplitude)
    lowest = np.amin(time)
    highest = np.amax(time)
    new_time = np.arange(lowest, highest, dt)
    new_amplitude = function(new_time)  # use interpolation function returned by `interp1d`
    if input_plot:
        plt.plot(time, amplitude, 'r', new_time, new_amplitude, 'o')
        plt.xlabel("time")
        plt.ylabel("amplitude")
        plt.title("input in MHz")
        plt.legend(["interpolated input", "input"])
        plt.grid()
        plt.show()
    return new_amplitude

from typing import List
import matplotlib.pyplot as plt
import json
from scipy import interpolate
import numpy as np


def input_f(dt: float) -> list: #No entiendo por que usar _time, pero lo dejo
    f = open('signal.json')
    data = json.load(f)
    amplitude = data['amplitude']
    time = data['time']

    interpolate_function = interpolate.interp1d(time, amplitude)

    lowest = np.amin(time)
    highest = np.amax(time)

    new_time = np.arange(lowest, highest, dt)
    new_amplitude = interpolate_function(new_time)  # use interpolation function returned by `interp1d`

    plt.plot(time, amplitude, 'o', new_time, new_amplitude, '-')
    plt.show()

    return new_amplitude

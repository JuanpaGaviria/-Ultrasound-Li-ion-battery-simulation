# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 10:19:04 2022

@author: EQ01
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


def graph(nodes, file, n_steps, dimensionless_length, path, fig_steps, low_limit, upper_limit, pause):
    os.chdir(path)
    h = np.loadtxt(file, delimiter=',')
    x = np.linspace(0, dimensionless_length, nodes)

    for i in range(0, n_steps + 1, fig_steps):
        plt.cla()  # borra pantalla anterior del plot
        plt.xlim(0, 1.)
        plt.ylim(low_limit, upper_limit)
        _iteration = i
        plt.plot(x, h[:, i], color='r', label=_iteration)
        plt.legend()
        plt.title(file)
        plt.grid()
        plt.pause(pause)

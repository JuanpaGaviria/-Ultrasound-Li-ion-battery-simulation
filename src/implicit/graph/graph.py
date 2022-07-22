# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 10:19:04 2022

@author: EQ01
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import re


def graph(nodes, file, n_steps, dimensionless_length):

    h = np.loadtxt(file, delimiter=',')
    x = np.linspace(0, dimensionless_length, nodes)

    for i in range(0, n_steps + 1, 30):
        plt.cla()  # borra pantalla anterior del plot
        plt.xlim(0, 1.)
        plt.ylim(-0.01, 0.01)
        _iteration = i
        plt.plot(x, h[:, i], color='r', label=_iteration)
        plt.legend()
        plt.title(file)
        plt.grid()
        plt.pause(0.00000000000000001)
    
path = "C:/Users/EQ01/Desktop/Folders/Trabajo/UPB/Research group/SOH/codes/WebEquation/src/results/layer_number/dataframes"
os.chdir(path)
n_steps = 16500
dimensionless_length = 1

for file in os.listdir():
    if file.endswith("nsteps-16500-nodes-500-dt-7e-08-layer-4.csv"):
        df = np.loadtxt(file, delimiter =',')
        # nodes_str = re.split("[-]", file)  # Takes de nodes in the file name
        # nodes_str = f'{nodes_str[1]}'
        # nodes = int(nodes_str)
        nodes = 500
        graph(nodes, file, n_steps, dimensionless_length)

#h = np.loadtxt('C:/Users/EQ01/Desktop/Folders/Trabajo/UPB/Research group/SOH/codes/WebEquation/src/results/fdm_implicit/node-200-dt-1e-08.csv', delimiter=',')


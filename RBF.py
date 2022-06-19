# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 21:30:00 2022

@author: EQ01
"""

import numpy as np
from numpy.linalg import inv
import matplotlib.pylab as plt
import winsound

nodes = 150
distance = 1
dx = distance/(nodes-1)
_x = np.linspace(0, distance, nodes)
#f = np.sin(np.pi * _x)
phi = np.zeros((nodes, nodes))
c = 35
n_steps = 50
dt = 1e-7
time = n_steps * dt
elastic_modulus = 1
density = 2
initial_velocity = 1
k = ((elastic_modulus*dt**2)/density)
_y = [ 0, 0.47675, -0.62681, 0.66253, -0.55683, 0.08213, -0.052714, 0.020251, -0.0069143, 0.0016148]

def phi_matrix_f(node, _x):
    for row in range(node):
        for col in range(node):
            r = np.linalg.norm(_x[row]-_x[col])
            phi[row, col] = np.sqrt(r**2 + c**2)
    return phi


def fo_phi_f(_x, node):
    fo_phi = np.zeros((node, node))
    for row in range(node):
        for col in range(node):
            r = np.linalg.norm(_x[row] - _x[col])
            fo_phi[row, col] = ((r**2+c**2)**(-1/2))*(_x[row]-_x[col])
    return fo_phi


def so_phi_f(_x, node):
    so_phi = np.zeros((node, node))
    for row in range(nodes):
        for col in range(nodes):
            r = np.linalg.norm(_x[row] - _x[col])
            so_phi[row, col] = c**2/((c**2+r**2)**(3/2))
    return so_phi

#uj0 = np.sin(np.pi * _x)
uj0  = np.zeros(nodes)
uj0[0] = _y[0]
uj0[-1] = 0
uj1 = np.zeros(nodes)
uj_1 = np.zeros(nodes)
h = np.zeros((nodes, n_steps+1))  # Matrix where the solution is stored after iteration

# h[:, 0] = uj0


uj_1 = uj0 - initial_velocity*dt

for j in range(0, n_steps):
    if j == 0:
        _phi = phi_matrix_f(nodes, _x)
        alpha = np.linalg.solve(_phi, uj0)
        function_rbf = np.dot(_phi, alpha)

        _so_phi = so_phi_f(_x, nodes)
        so_rbf = np.dot(_so_phi, alpha)
        so_function_analytical = -np.sin(_x)

        #k_so_rbf = np.dot(k, so_rbf)
        k_so_rbf = k * so_rbf
        uj1 = k_so_rbf + uj0
        h[:, j+1] = uj1[:]
        uj_1 = uj0
        uj0 = uj1

    if j > 0:
        if j < len(_y):
            uj0[0] = _y[j]
        else:
            uj0[0] = 0
        
        uj0[-1] = 0
        _phi = phi_matrix_f(nodes, _x)
        alpha = np.linalg.solve(_phi, uj0)
        function_rbf = np.dot(_phi, alpha)

        _so_phi = so_phi_f(_x, nodes)
        so_rbf = np.dot(_so_phi, alpha)
        so_function_analytical = -np.sin(_x)

        #k_so_rbf = np.dot(k, so_rbf)
        k_so_rbf = k * so_rbf
        uj1 = k_so_rbf + (2*uj0)-uj_1
        h[:, j+1] = uj1[:]
        uj_1 = uj0
        uj0 = uj1

duration = 1000  # milliseconds
freq = 380  # Hz
winsound.Beep(freq, duration)

x = np.linspace(0, distance, nodes)

for i in range(0, n_steps + 1):
    plt.cla()  # borra pantalla anterior del plot
    plt.xlim(0, 1.)
    plt.ylim(-1e-12, 1e-12)
    _iteration = i
    plt.plot(x, h[:, i], color='r', label=_iteration)
    plt.legend()
    plt.grid()
    plt.pause(0.00000000000000001)
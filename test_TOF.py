import numpy as np
import matplotlib.pyplot as plt


H = np.loadtxt('h_500_dt_1e7.csv', delimiter=',')
node_zero = []
node_one = []
dt = 1e-7
deformation = []
times = []
n_steps = 20000
time = n_steps * dt

for i in range(H.shape[1] - 2):

    u0 = H[0, i]
    u1 = H[0, i + 1]
    u2 = H[0, i + 2]


    derivative_1 = (u1 - u0) / dt
    derivative_2 = (u2 - u1) / dt

    sign_1 = np.sign(derivative_1)
    sign_2 = np.sign(derivative_2)

    if sign_1 != sign_2:
        # prom_deformation = (H[0, i+1] + H[0, i+2])/2
        iter_time = (i * time) / n_steps
        # deformation.append(prom_deformation)
        deformation.append(H[0, i+1])
        times.append(iter_time)

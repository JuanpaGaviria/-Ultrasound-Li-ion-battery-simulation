import numpy as np
import matplotlib.pyplot as plt

def tof(dt, n_steps):
    H = np.loadtxt('test_400n_2000it.csv', delimiter=',')
    node_zero = []
    node_one = []
    dt = 1e-7
    deformation = []
    times = []
    n_steps = 2000
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
            iter_time = (i * time) / n_steps
            deformation.append(H[0, i + 1])
            times.append(iter_time)

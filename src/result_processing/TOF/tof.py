import numpy as np


def tof(dt, n_steps, file, save):

    """
    Take the time a wave is passing through the boundary with the amplitude
    """

    H = file
    time = dt * n_steps
    deformation = []
    times = []

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
            deformation.append(H[0, i+1])
            times.append(iter_time)

    return times, deformation


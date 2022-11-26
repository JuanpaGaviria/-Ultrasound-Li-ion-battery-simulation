import numpy as np
from scipy import signal
import scipy.fft
from scipy.fft import rfftfreq


def tof(dt, n_steps, file, name):

    """
    Take the time a wave is passing through the boundary with the amplitude
    """

    H = np.loadtxt(file, delimiter=",", dtype=float)
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

    signal = [times, deformation]
    np.savetxt(f'{name}_0.txt', signal)  # Must be created

def slice_tof(file, first_limit, second_limit, dt, name):  # times are expressed in terms of the iterations
    
    """
    Slice the solution and return a characteristic peack
    """

    H = np.loadtxt(file, delimiter=",", dtype=float)
    amplitudes = H[0,first_limit:second_limit]
    first_limit = first_limit*dt
    second_limit = second_limit*dt
    times = np.linspace(first_limit, second_limit, amplitudes.size)
    signal_sliced = [times, amplitudes]
    np.savetxt('../../QUM/results/signal_sliced_results/'f'{name}.txt', signal_sliced, delimiter=',')  # Must be created

def hanning_window(length):
    window = signal.hann(length)
    return window

def conv(window, signal):
    convolved = np.convolve(signal, window)
    return convolved

def fft(signal):
    fft_signal = np.abs(scipy.fft.rfft(signal))
    d = 1/(7e-08)
    freq = rfftfreq(signal.size, d)
    return freq, fft_signal

def normalized_spectrums(ref_signal, signal):
    NE = 10*np.log10(signal[1]/ref_signal[1])
    return NE
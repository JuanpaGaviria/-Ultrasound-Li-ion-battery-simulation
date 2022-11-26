from . import functions
import os
import re
import numpy as np


def tof_iterative_fun(reading_path, dt, n_steps):

    """
    Return when a wave is comming
    """

    os.chdir(reading_path)

    for file in os.listdir():
        if file.endswith(".csv"):
            name = re.split("[.]", file)
            name = name[0]
            functions.tof(dt, n_steps, file, name)

def signal_slice_iterative_fun(reading_path, dt):

    """
    Slice the Dataset. This uses the H matrix solution
    """
    
    os.chdir(reading_path)
    for file in os.listdir():
        if file.endswith(".csv"):
            name = re.split("[.]", file)
            name = name[0]
            if name == '0' or name == '10' or name == '20' or name == '30':
                first_limit = 3800
                second_limit = 7550
            else:
                first_limit = 2800
                second_limit = 6550
            
            functions.slice_tof(file, first_limit, second_limit, dt, name)

def windowing_convolve(reading_path):
    os.chdir(reading_path)
    for file in os.listdir():
        if file.endswith(".txt"):
            name = re.split("[.]", file)
            name = name[0]+'convolve'
            length = len(file)
            window = functions.hanning_window(length)
            signal = np.loadtxt(file, delimiter=",")
            signal = signal[1]
            convolved = functions.conv(window, signal)
            np.savetxt('./convolve/'f'{name}.txt', convolved, delimiter=',')  # Must be created

def fft_iterative_fun(reading_path):
    os.chdir(reading_path)
    for file in os.listdir():
        if file.endswith(".txt"):
            name = re.split("[.]", file)
            name = name[0]+' fft'
            signal = np.loadtxt(file, delimiter=",")
            freq, fft_signal = functions.fft(signal)
            np.savetxt('./FFT/'f'{name}.txt', (freq, fft_signal), delimiter=',')  # Must be created

def normalized_spectrums_iterative(reading_path):
    os.chdir(reading_path)
    ref_signal = np.loadtxt('100convolve fft.txt', delimiter=',')
    for file in os.listdir():
        if file.endswith(".txt"):
            name = re.split("[.]", file)
            name = name[0]+' fft'
            signal = np.loadtxt(file, delimiter=",")
            NE = functions.normalized_spectrums(ref_signal, signal)
            np.savetxt('./NE/'f'{name}.txt', NE, delimiter=',')  # Must be created


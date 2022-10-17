# Requirements
import pandas as pd
import os

# Internal Numerical Methods
from src.explicit.numerical_method import numerical_method_explicit
from src.implicit.numerical_method import numerical_method_implicit

# Processing functions
from src.result_processing.stability.stability import *
from src.result_processing.layer_number.layer_number_ import layer_number_f
from src.result_processing.SOC.SOC_df import *
from src.result_processing.SOC.SOC_fun import *
from src.result_processing.SOC.functions import *
from src.result_processing.QUM.iterations import *

# Numerical Methods
# url = './src/database/materials_properties.csv'
# df = pd.read_csv(url)
# indexes = [0, 11]  # materials definition discharged
# dt = 70e-9
# nodes = 300
# n_steps = 16500
# time = n_steps*dt
# name = f'nodes-{nodes}-dt{dt}'
# layer_number = 4  # The condition is that the numbers half must be an even number
# numerical_method_implicit(indexes, layer_number, nodes, n_steps, dt, initial_velocity, df, name, save=False, save_path, main_path)
# numerical_method_explicit(indexes, df, nodes, time, n_steps, name, layer_number, save=False)

# QUM
reading_path = "src/result_processing/QUM/results/signal_sliced_results/convolve/FFT"
# reading_path = "src/result_processing/SOC/Dataset/"
dt = 7e-8
nsteps = 16500
# tof_iterative_fun(reading_path, dt, nsteps)
# signal_slice_iterative_fun(reading_path, dt)
# windowing_convolve(reading_path)
# fft_iterative_fun(reading_path)
normalized_spectrums_iterative(reading_path)


# SOC comparison function.
# main_path = os.path.dirname(__file__)
# reading_path = 'src/result_processing/SOC/Dataset'
# saving_path = 'src/result_processing/SOC/SOC_output'
# style = 'seaborn-poster'
# SOC_comparison(reading_path, main_path, cut_imput = 14)
# n = 11
# df, n = df_creation(saving_path)
# plot(df, n, style)


# Heat map 
# iterative_stability_f(indexes, layer_number, n_steps, initial_velocity, amplitude, period, input_time, url, df, nodes_array, dt_array, save=False)
# stability_f(dt_array, n_steps, reading_path, save_path, main_path)
# equal_data_files(n_steps, dt_array, reading_path, save_path)  # Reading is where the stability_f stores the results
# heat_map_f(reading_path, saving_path)

# Layer analysis
# layer_number_f(layers, indexes, nodes, n_steps, dt, time, initial_velocity, amplitude, period, input_time, url, df, name, save=False)



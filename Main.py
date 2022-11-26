# Requirements
import pandas as pd
import os
# import explicit

# Internal Numerical Methods
from src.explicit.numerical_method import numerical_method_explicit
from src.implicit.numerical_method import numerical_method_implicit

# Processing functions
from src.result_processing.stability.stability import *
from src.result_processing.layer_number.layer_number_ import layer_number_f
from src.result_processing.SOC.SOC_df import *
from src.result_processing.SOC.SOC_fun import *
from src.result_processing.SOC.functions import *
from src.result_processing.QUS.iterations import *
from src.implicit.graph.graph import graph
from src.implicit.courant import courant

method_switcher = {
    "implicit": numerical_method_implicit,
    "explicit": numerical_method_explicit,
}
# Numerical Methods
main_path = os.path.dirname(__file__)
saving_path = 'src/result_processing/Simulation'
url = './src/database/materials_properties.csv'
initial_velocity = 1
df = pd.read_csv(url)
# indexes = [0,1,2,3,4,15]  # materials definition discharged
# geometry_unit = [1,15,2,15,1,4,3,4]  # Geometry
indexes = [15,4]  # materials definition discharged
geometry_unit = [15,15,4]  # Geometry

dt = 5e-07
nodes = 500
dx = 1/nodes
n_steps = 500
time = n_steps*dt
layer_number = 4  # The condition is that the half of the number must be an even number
interpolation_points = 5
name = 'neumann_'f'{0}''_nodes_'f'{nodes}''_dt_'f'{dt}''_int_'f'{interpolation_points}''.csv'
# method_switcher.get("implicit")(indexes, geometry_unit, layer_number, nodes, n_steps, dt, dx, initial_velocity, df, name, saving_path, main_path, interpolation_points, save=True)

fig_steps, low_limit, upper_limit, pause= 1, -0.01, 0.01, 0.001
graph(nodes, name, n_steps, 1, saving_path, fig_steps, low_limit, upper_limit, pause)


# QUM
# reading_path = "src/result_processing/QUM/results/"
# tof_iterative_fun(reading_path, dt, n_steps)
# signal_slice_iterative_fun(reading_path, dt)
# windowing_convolve(reading_path)
# fft_iterative_fun(reading_path)
# normalized_spectrums_iterative(reading_path)


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



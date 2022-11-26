# Requirements
from operator import index
import pandas as pd
import os

# Internal Numerical Methods
from src.explicit.numerical_method import numerical_method_explicit
from src.implicit.numerical_method import numerical_method_implicit



"""material selection
"""

indexes = [0, 11]  # materials definition discharged
layer_number = 4  # The condition is that the numbers half must be an even number

url = './src/database/materials_properties.csv'
df = pd.read_csv(url)

dt = 70e-9
nodes = 150
n_steps = 600
time = n_steps*dt
name = f'nodes-{nodes}-dt{dt}'

numerical_method_explicit(indexes, df, nodes, time, n_steps, name, layer_number, save=False)

# main_path = os.path.dirname(__file__)
# reading_path = 'src/result_processing/SOC/Dataset'
# saving_path = 'src/result_processing/SOC/SOC_output'
# style = 'seaborn-poster'

# SOC_comparison(reading_path, main_path, cut_imput = 14)
# n = 11
# df, n = df_creation(saving_path)
# plot(df, n, style)


# functions.df_creation(name)
# functions.plot(df, count, style)
# numerical_method_implicit(indexes, layer_number, nodes, n_steps, dt, initial_velocity, df, name, save=False, save_path, main_path)
# iterative_stability_f(indexes, layer_number, n_steps, initial_velocity, amplitude, period, input_time, url, df, nodes_array, dt_array, save=False)
# stability_f(dt_array, n_steps, reading_path, save_path, main_path)
# equal_data_files(n_steps, dt_array, reading_path, save_path)  # Reading is where the stability_f stores the results
# heat_map_f(reading_path, saving_path)
#layer_number_f(layers, indexes, nodes, n_steps, dt, time, initial_velocity, amplitude, period, input_time, url, df, name, save=False)
#numerical_method_explicit(indexes, df, nodes, time, n_steps, name, layer_number, save=False)

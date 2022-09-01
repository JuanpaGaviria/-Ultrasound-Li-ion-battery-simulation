from operator import index
import pandas as pd
from src.implicit.results.stability.stability import *
from src.implicit.numerical_method import numerical_method_implicit
from src.implicit.iterative_stability_results import iterative_stability_f
from src.implicit.results.layer_number.layer_number_ import layer_number_f
from src.explicit.numerical_method import numerical_method_explicit


"""material selection
0, 2: anode charged, anode discharged 
1, 3: cathode charged, cathode discharged
6: separator
4,5,7,8,9: others (check csv)
10, 11: benzene electrolyte, carbon tetrachloride electrolyte 
"""
indexes = [0, 11]  # materials definition discharged
layer_number = 4  # The condition is that the numbers half must be an even number

initial_velocity, amplitude, period, input_time = 0, 2, 2, 0.1

url = './src/database/materials_properties.csv'
df = pd.read_csv(url)

nodes_array = [300, 400, 500]
dt = 70e-9
nodes = 200
n_steps = 100
time = n_steps*dt
dt_array = [1e-7, 70e-9, 5e-8]
layers = [512]
name = f'nodes-{nodes}-dt{dt}'
# numerical_method_implicit(indexes, layer_number, nodes, n_steps, dt, time, initial_velocity, amplitude, period, input_time, url, df, name, save=False)
#iterative_stability_f(indexes, layer_number, n_steps, initial_velocity, amplitude, period, input_time, url, df, nodes_array, dt_array, name, save=False)
stability_f(dt_array, n_steps)
equal_data_files(n_steps, dt_array)
heat_map_f()
#layer_number_f(layers, indexes, nodes, n_steps, dt, time, initial_velocity, amplitude, period, input_time, url, df, name, save=False)
#numerical_method_explicit(indexes, df, nodes, time, n_steps, name, layer_number, save=False)

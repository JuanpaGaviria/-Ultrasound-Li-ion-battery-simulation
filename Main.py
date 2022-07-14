import pandas as pd
from src.results.stability.stability import *
from src.results.numerical_method import numerical_method_f
from src.results.iterative_stability_results import iterative_stability_f

"""material selection
0, 2: anode charged, anode discharged 
1, 3: cathode charged, cathode discharged
6: separator
4,5,7,8,9: others (check csv)
10, 11: benzene electrolyte, carbon tetrachloride electrolyte 
"""
indexes = [0, 1]  # materials definition
layer_number = 32  # The condition is that the numbers half must be an even number

nodes= 150
dt = 1e-7
initial_velocity, amplitude, period, input_time = 0, 2, 2, 0.1

url = './src/database/materials_properties.csv'
df = pd.read_csv(url)

nodes_array = [200, 300, 400, 500, 600]
n_steps = 6000
dt_array = [1e-8, 1e-9, 5e-09, 5e-10]

#numerical_method_f(indexes, layer_number, nodes, n_steps, dt, time, initial_velocity, amplitude, period, input_time, url, df)
#iterative_stability_f(indexes, layer_number, n_steps, initial_velocity, amplitude, period, input_time, url, df, nodes_array, dt_array)
#stability_f(dt_array, n_steps)
equal_data_files(n_steps, dt_array)

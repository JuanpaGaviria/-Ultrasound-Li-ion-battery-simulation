import pandas as pd
from src.results.stability.stability import stability_f
from src.results.numerical_method import numerical_method_f


"""material selection
0, 2: anode charged, anode discharged 
1, 3: cathode charged, cathode discharged
6: separator
4,5,7,8,9: others (check csv)
10, 11: benzene electrolyte, carbon tetrachloride electrolyte 
"""
indexes = [2, 3]  # materials definition
layer_number = 32  # The condition is that the numbers half must be an even number

nodes, n_steps = 150, 100
dt = 1e-7
time = n_steps * dt
initial_velocity, amplitude, period, input_time = 0, 2, 2, 0.1

url = './src/database/materials_properties.csv'
df = pd.read_csv(url)

nodes_array = [200, 250, 300, 350, 400, 450, 500, 550, 600]
n_steps = 1500
dt_array = [1e-8, 1e-9, 5e-09, 5e-10]

#numerical_method_f(indexes, layer_number, nodes, n_steps, dt, time, initial_velocity, amplitude, period, input_time, url, df)
stability_f(dt_array, n_steps)


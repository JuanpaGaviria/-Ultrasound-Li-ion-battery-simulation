import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src import Bigbang
from src.battery_construction import battery_structure
from src.FDM_implicit import fdm_implicit


indexes = [2, 3]  # materials definition
layer_number = 32  # The condition is that the numbers half must be an even number

nodes_array = [200, 250, 300, 350, 400, 450, 500, 550, 600]
n_steps = 100
dt_array = [1e-7, 1e-8, 1e-8/2, 1e-9, 1e-9/2]
initial_velocity, amplitude, period, input_time = 0, 2, 2, 0.1

url = './src/database/materials_properties.csv'
df = pd.read_csv(url)

def run(indexes, layer_number, nodes, n_steps, dt, time, initial_velocity, amplitude, period, input_time, url):
    
    interphase_number, battery_map = battery_structure(indexes, layer_number)

    materials, materials_summary, materials_number, materials_thickness, material_dimensionless_length, length,\
            dx, x, interphase_position, summary_e_modulus, gamma_map, phi_map = Bigbang.big_bang(indexes, df, nodes,
                                                                                                battery_map, dt)
    print(interphase_position)

    H = fdm_implicit(interphase_position, nodes, x, n_steps, dt, initial_velocity, battery_map, summary_e_modulus, 
                    gamma_map, phi_map)

    np.savetxt(f'results/node-{nodes}-dt-{dt}.csv', H, delimiter=',')

for i in range(len(nodes_array)):
    for j in range(len(dt_array)):
        nodes = nodes_array[i]
        dt = dt_array[j]
        time = n_steps * dt
        run(indexes, layer_number, nodes, n_steps, dt, time, initial_velocity, amplitude, period, input_time, url)
    


from . import Bigbang
from .battery_construction import battery_structure
from .FDM_implicit import fdm_implicit
import numpy as np


def numerical_method_f(indexes, layer_number, nodes, n_steps, dt, time, initial_velocity, amplitude, period, input_time, url, df):
    
    interphase_number, battery_map = battery_structure(indexes, layer_number)

    materials, materials_summary, materials_number, materials_thickness, material_dimensionless_length, length,\
            dx, x, interphase_position, _e_modulus_dict, gamma_map, phi_map = Bigbang.big_bang(indexes, df, nodes,
                                                                                                battery_map, dt)
    

    H = fdm_implicit(interphase_position, nodes, x, n_steps, dt, initial_velocity, battery_map, _e_modulus_dict, 
                    gamma_map, phi_map)

    name = f'nsteps-{n_steps}-nodes-{nodes}-dt-{dt}-layer-{layer_number}'
    # np.savetxt(f'src/results/layer_number/dataframes/{name}.csv', H, delimiter=',')
    # print('saved: ', layer_number,'.csv')
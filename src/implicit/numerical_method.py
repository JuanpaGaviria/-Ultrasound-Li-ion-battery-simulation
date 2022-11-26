from . import Bigbang
from .battery_construction import battery_structure
from .FDM_implicit import fdm_implicit
from .courant import courant
import numpy as np
import os


def numerical_method_implicit(indexes, geometry_unit, layer_number, nodes, n_steps, dt, dx, initial_velocity, df, name, saving_path, main_path, interpolation_points, save=True):
    
    battery_map = battery_structure(geometry_unit, layer_number)

    x, interphase_position, _e_modulus_dict, gamma_map, phi_map, materials_summary = Bigbang.big_bang(indexes, df, nodes, battery_map, dt)
    
    courant_list = courant(dx, dt, indexes, materials_summary)
    print(courant_list)
    H = fdm_implicit(interphase_position, nodes, x, n_steps, dt, initial_velocity, battery_map, _e_modulus_dict, 
                    gamma_map, phi_map, interpolation_points)

    if save:
        os.chdir(saving_path)
        np.savetxt(name, H, delimiter=',')
        print('saved: ', f'{name}')
        os.chdir(main_path)

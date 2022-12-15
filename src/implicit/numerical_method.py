from . import Bigbang
from .battery_construction import battery_structure
from .FDM_implicit import fdm_implicit
from .courant import courant
import numpy as np
import os


def numerical_method_implicit(indexes, geometric_unit  ,layer_number, n_steps, dt, initial_velocity, df, name, saving_path,
                            main_path, interpolation_points, cfl, nodes, case, dimensionless, input_plot, save):
    
    battery_map = battery_structure(geometric_unit, layer_number, case)

    if dimensionless == True:
        interphase_dimensionless_condition = True
    else:
        interphase_dimensionless_condition = False

    x , interphase_position, _e_modulus_dict, gamma_map, phi_map, materials_summary, nodes, dx, higher_velocity = Bigbang.big_bang(indexes, df, nodes, battery_map, dt, cfl, dimensionless)
    
    cfl_value = courant(dx, dt, higher_velocity)
    H = fdm_implicit(dx, interphase_position, nodes, x, n_steps, dt, initial_velocity, battery_map, _e_modulus_dict, 
                    gamma_map, phi_map, interpolation_points, input_plot, interphase_dimensionless_condition)

    if save:
        os.chdir(saving_path)
        np.savetxt(name, H, delimiter=',')
        print('saved: ', f'{name}')
        os.chdir(main_path)
    
    return nodes

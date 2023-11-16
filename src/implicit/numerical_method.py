from . import Bigbang
from .battery_construction import battery_structure
from .FDM_implicit import fdm_implicit
from .courant import courant
import numpy as np
import os


def numerical_method_implicit(indexes, geometric_unit  ,layer_number, n_steps, dt, initial_velocity, df, name, saving_path,
                            main_path, interpolation_points, cfl, nodes, rescale_t, rescale_x, rescale_thickness, 
                            case, dimensionless, input_plot, save, tol, condition_number):
    
    battery_map = battery_structure(geometric_unit, layer_number, case)

    x , interphase_position, _e_modulus_dict, gamma_map, phi_map, materials_summary, nodes, dx, higher_velocity, _thickness_dict = Bigbang.big_bang(indexes, 
                                                                        df, nodes, battery_map, dt, cfl, dimensionless, rescale_t, rescale_x, rescale_thickness)
    
    cfl_value = courant(dx, dt,rescale_t,rescale_x, higher_velocity)
    print(f'Courant: {cfl_value}')
    H = fdm_implicit(interphase_position, nodes, x, n_steps, dt, initial_velocity, battery_map, _e_modulus_dict, _thickness_dict,  
                    gamma_map, phi_map, interpolation_points, input_plot, rescale_x,rescale_thickness, tol, condition_number)


    if save:
        os.chdir(saving_path)
        np.savetxt(name, H, delimiter=',')
        print('saved: ', f'{name}')
        os.chdir(main_path)
    
    return nodes

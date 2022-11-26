import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import winsound
from src.explicit import big_bang
from src.explicit.courant_constructor import courant
from src.explicit.fem import fm
from src.explicit.battery_construction import battery_structure



def numerical_method_explicit(indexes, layer_number, nodes, n_steps, dt, initial_velocity, df, name, save_path, main_path, save=False):

    battery_map = battery_structure(indexes, layer_number)

    dx, x, dimensionless_length, dimensionless_position , material, \
            dimensionless_thickness, materials_summary, thickness_summary,\
            dimensionless_lengths, materials, _e_modulus_dict, materials_summary=big_bang.big_bang_f(indexes, df, nodes, battery_map, n_steps)

    courants = courant(dx, dt, materials_summary)

    H = fm(nodes, n_steps, dx, dt, materials_summary, courants,\
        indexes, dimensionless_position,x, _e_modulus_dict, battery_map)

    if save:
        np.savetxt(f'{name}', H, delimiter=",")
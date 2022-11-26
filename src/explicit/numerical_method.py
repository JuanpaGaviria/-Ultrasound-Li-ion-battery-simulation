import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.explicit import big_bang
from src.explicit.courant_constructor import courant
from src.explicit.fem import fm
from src.explicit.battery_construction import battery_structure



def numerical_method_explicit(indexes, df, nodes, time, nsteps, name, layer_number, save):

    interphase_number, battery_map = battery_structure(indexes, layer_number)

    dx, dt, x, dimensionless_length, dimensionless_position , material, \
            dimensionless_thickness, materials_summary, thickness_summary,\
            dimensionless_lengths, materials, _e_modulus_dict=big_bang.big_bang_f(indexes, df, nodes, time, nsteps, battery_map)

    courants = courant(dx, dt, materials_summary, indexes, materials)

    H = fm(nodes, nsteps, dx, dt, materials_summary, courants,\
        indexes, dimensionless_position,x, _e_modulus_dict, battery_map)

    if save:
        np.savetxt(f'{name}', H, delimiter=",")
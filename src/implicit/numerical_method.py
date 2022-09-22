import os

import numpy as np

from . import Bigbang
from .battery_construction import battery_structure
from .FDM_implicit import fdm_implicit


def numerical_method_implicit(
    indexes,
    layer_number,
    nodes,
    n_steps,
    dt,
    initial_velocity,
    df,
    name,
    save,
    save_path,
    main_path,
):

    battery_map = battery_structure(indexes, layer_number)

    x, interphase_position, _e_modulus_dict, gamma_map, phi_map = Bigbang.big_bang(
        indexes, df, nodes, battery_map, dt
    )

    H = fdm_implicit(
        interphase_position,
        nodes,
        x,
        n_steps,
        dt,
        initial_velocity,
        battery_map,
        _e_modulus_dict,
        gamma_map,
        phi_map,
    )

    if save:
        os.chdir(save_path)
        np.savetxt(f"{name}", H, delimiter=",")
        print("saved: ", f"{name}")
        os.chdir(main_path)

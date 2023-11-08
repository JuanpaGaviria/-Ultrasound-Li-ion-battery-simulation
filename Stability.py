# Requirements
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

#change the working directory
os.chdir(os.path.dirname(__file__))

# import explicit

# Internal Numerical Methods
from src.explicit.numerical_method import numerical_method_explicit
from src.implicit.numerical_method_condition import numerical_method_implicit_condition

# Processing functions
from src.result_processing.stability.stability import *
from src.result_processing.layer_number.layer_number_ import layer_number_f
from src.result_processing.SOC.SOC_df import *
from src.result_processing.SOC.SOC_fun import *
from src.result_processing.SOC.functions import *
from src.result_processing.QUS.iterations import *
from src.result_processing.output_signal.output_signal import *
from src.implicit.graph.graph import graph
from src.implicit.courant import courant

def condition_number(nodes):
    method_switcher = {
        "implicit": numerical_method_implicit_condition,
        "explicit": numerical_method_explicit,
    }
    # Numerical Methods
    main_path = os.path.dirname(__file__)
    saving_path = 'src/result_processing/Simulation'
    url = './src/database/materials_properties.csv'
    initial_velocity = 1
    df = pd.read_csv(url, dtype=object)
    indexes = [4,15]  # materials definition discharged
    geometry_unit = [4,15]  # Geometry

    dt = 1.45e-3
    cfl = False
    time = 6
    n_steps = int(time/dt)
    layer_number = 4 # The condition is that the half of the number must be an even number
    interpolation_points = 5
    rescale_t = False
    rescale_x = False
    name = 'steps_'f'{n_steps}''_nodes_'f'{nodes}''_dt_'f'{dt}''_int_'f'{interpolation_points}''_rt_'f'{rescale_t}''_rx_'f'{rescale_x}''.csv'
    cond_num = method_switcher.get("implicit")(indexes, geometry_unit  ,layer_number, n_steps, dt, initial_velocity, df, name, saving_path, 
                                            main_path, interpolation_points, cfl, nodes, rescale_t, rescale_x, 
                                            rescale_thickness=False, case = False, dimensionless=True, input_plot=False, save=True)
    return cond_num

node_array = np.arange(100, 200, 5).astype(int)
cond_num_array = []
for node in node_array:
    cond_num = condition_number(node)
    cond_num_array.append(cond_num)

plt.plot(node_array, cond_num_array)
plt.yscale('log')
from operator import index
import os
import numpy as np


def dict_iter_number_f(dt_array, n_steps):

    """
    Define a dict to know how many iterations must be used for each particular result being processed
    array : iter number
    This guarantee to have everything at the same time.
    """


    iter_numbers = []
    max_time_intersection = n_steps * (min(dt_array))  # time taken in each df
    for i in range(len(dt_array)):
        iter_number = max_time_intersection/dt_array[i]  # Computes the corresponding iteration number for each dt
        iter_numbers.append(iter_number)  # stores each value in a list
    slice_dict = dict(zip(dt_array, iter_numbers))  # Generates de dict
    
    return slice_dict


def read_iter_number(dt, slice_dict):

    """
    Reads the dict
    """

    iter_number = slice_dict[dt]
    
    return int(iter_number)

def slice_df(iter_number, df, nodes_str, dt_str, save_path, reading_path):

    """
    Takes the amplitude value with the dict key value
    """

    df_node_0 = df[0,:iter_number]
    os.chdir(save_path)  # saves it in a different folder
    np.savetxt(f'node-{nodes_str}-dt-{dt_str}.csv', df_node_0, delimiter=',')
    os.chdir(reading_path)  # Change the path to read the datasets


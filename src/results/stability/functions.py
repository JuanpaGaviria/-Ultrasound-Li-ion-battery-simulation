from operator import index
import pandas as pd
import os
import numpy as np


def dict_iter_number_f(dt_array, n_steps):

    iter_numbers = []  # loop to determine the iteration numbers to have the data at the same time
    max_time_intersection = n_steps * (min(dt_array))  # time taken in each df
    for i in range(len(dt_array)):
        iter_number = max_time_intersection/dt_array[i]  # Computes the corresponding iteration number of each dt
        iter_numbers.append(iter_number)  # stores each value in a list
    slice_dict = dict(zip(dt_array, iter_numbers))  # Generates de dict
    
    return slice_dict


def read_iter_number(dt, slice_dict):

    iter_number = slice_dict[dt]  # Reads the iter number to slice the df
    
    return int(iter_number)

def slice_df(iter_number, df, nodes_str, dt_str):  # This function allows to obtain the new datasets.
        df_node_0 = df[0,:iter_number]
        #df_node_0 = df.iloc[0,:iter_number]  # Slice the dataframe
        path_TOF = "C:/Users/EQ01/Desktop/Folders/Trabajo/UPB/Research group/SOH/codes/WebEquation/src/results/stability/TOF_df"
        os.chdir(path_TOF)  # saves it in a different folder
        #df_node_0.to_csv(f'node-{nodes_str}-dt-{dt_str}.csv', index=False)  # Stores it with this name
        np.savetxt(f'node-{nodes_str}-dt-{dt_str}.csv', df_node_0, delimiter=',')
        path = "C:/Users/EQ01/Desktop/Folders/Trabajo/UPB/Research group/SOH/codes/WebEquation/src/results/stability/dataframes"
        os.chdir(path)  # Change the path to read the datasets


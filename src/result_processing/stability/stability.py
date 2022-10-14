import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
from scipy import interpolate
import os
from src.result_processing.stability import functions
import re
from src.implicit.numerical_method import numerical_method_implicit


def iterative_stability_f(indexes, layer_number, n_steps, initial_velocity, amplitude, period, input_time, url, df, nodes_array, dt_array, save, save_path, main_path):

    """
    Iteration varying the nodes and dt
    """

    for i in range(len(nodes_array)):
        for j in range(len(dt_array)):
            nodes = nodes_array[i]
            dt = dt_array[j]
            time = n_steps * dt
            name = f'nodes-{nodes}-dt{dt}'
            numerical_method_implicit(indexes, layer_number, nodes, n_steps, dt, time, initial_velocity, amplitude, period, input_time, url, df, name, save, save_path, main_path)



def stability_f(dt_array, n_steps, reading_path, save_path, main_path):

    """
    1. Read the results
    2. Takes the dt and the nodes from the file name
    3. Define the maximum common time that all the results have
    """

    slice_dict = functions.dict_iter_number_f(dt_array, n_steps)  # Return a dict to allow the slicing of the dataframes

    os.chdir(reading_path)  # Change the path to read the datasets 
    for file in os.listdir():  # for loop for all the files
        if file.endswith(".csv"):  # if they are .csv
            df = np.loadtxt(file, delimiter=',')
            dt_str = re.split("[-dt.]", file)  # Takes the dt in the file name
            dt_str = f'{dt_str[-3]}-{dt_str[-2]}'  # Takes the dt in the file name
            dt = float(dt_str)
            nodes_str = re.split("[-]", file)  # Takes de nodes in the file name
            nodes_str = f'{nodes_str[1]}'
            iter_number = functions.read_iter_number(dt, slice_dict)  # Checks the iter number to slice the corresponding to the current dataset            
            functions.slice_df(iter_number, df, nodes_str, dt_str, save_path, reading_path)  # Saves the new dataset


def equal_data_files(n_steps, dt_array, reading_path, save_path):

    """
    Function that interpolates all the datasets to match the number of data and time
    """


    max_time_intersection = max_time_intersection_f(n_steps, dt_array)  # Function that measure the common maxium time in all the files 
    length_dataset = lenght_dataset_f(max_time_intersection, dt_array)  # Function that measure the amount of data in the biggest file
    os.chdir(reading_path)

    for file in os.listdir():
        if file.endswith(".csv"):
            df = np.loadtxt(file, delimiter =',')  # Deformation array
            nodes_str = re.split("[-]", file)  # Takes de nodes in the file name
            nodes_str = f'{nodes_str[1]}'
            dt_str = re.split("[-dt.]", file)  # Takes the dt in the file name
            dt_str = f'{dt_str[-3]}-{dt_str[-2]}'  # Takes the dt in the file name
            dt = float(dt_str)
            y, lowest_time, highest_time = time_array(dt, n_steps, max_time_intersection)  # Generates the time array
            function = interpolate.interp1d(y, df)  # Interpolate function of time vs deformation
            interpolation(length_dataset, function, lowest_time, highest_time, nodes_str, dt_str, save_path, reading_path)  # interpolates adding the number of data as the biggest file

def heat_map_f(reading_path, saving_path):

    # set the path to the files

    # create a list of the files matching the pattern
    files = list(reading_path.glob(f'*.csv'))

    # alternative, creates 1 dataframe from all files
    df = pd.concat([pd.read_csv(f, header=0) for f in files], axis = 1)

    columns = []
    for file in os.listdir():
        if file.endswith(".csv"):
            dt_str = re.split("[-dt.]", file)  # Takes the dt in the file name
            dt_str = f'{dt_str[-3]}-{dt_str[-2]}'  # Takes the dt in the file name
            nodes_str = re.split("[-]", file)  # Takes de nodes in the file name
            nodes_str = f'{nodes_str[1]}'
            column = f'{dt_str}_{nodes_str}'
            columns.append(column)
    df.columns = columns
    heatmap = df.corr()

    plt.style.use("seaborn-paper")

    # 3. Plot the heatmap
    plt.figure(figsize=(12,12))
    heat_map = sns.heatmap( heatmap, linewidth = 1 , annot = True)
    plt.title( "Stability time step and nodes" )
    plt.show()
    os.chdir(saving_path)  # Change the path to read the datasets
    plt.savefig()

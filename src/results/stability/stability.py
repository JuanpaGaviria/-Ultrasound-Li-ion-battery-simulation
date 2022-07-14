import numpy as np
from scipy import interpolate
import os
from . import functions
import re
from .matching_functions import *

def stability_f(dt_array, n_steps):
    slice_dict = functions.dict_iter_number_f(dt_array, n_steps)  # Return a dict to allow the slicing of the dataframes
    print(slice_dict)

    path = "C:/Users/EQ01/Desktop/Folders/Trabajo/UPB/Research group/SOH/codes/WebEquation/src/results/stability/dataframes"
    os.chdir(path)  # Change the path to read the datasets 
    for file in os.listdir():  # for loop for all the files
        if file.endswith(".csv"):  # if they are .csv
            #file_path = f"{path}/{file}"  # This allows to take the absolute path of each file
            #df = pd.read_csv(file)  # reads the dataset
            df = np.loadtxt(file, delimiter=',')
            dt_str = re.split("[-dt.]", file)  # Takes the dt in the file name
            dt_str = f'{dt_str[-3]}-{dt_str[-2]}'  # Takes the dt in the file name
            dt = float(dt_str)
            nodes_str = re.split("[-]", file)  # Takes de nodes in the file name
            nodes_str = f'{nodes_str[1]}'
            # res = isinstance(str_1, str)
            # print("Is variable a string ? : " + str(res))
            iter_number = functions.read_iter_number(dt, slice_dict)  # Checks the iter number to slice the corresponding to the current dataset            
            functions.slice_df(iter_number, df, nodes_str, dt_str)  # Saves the new dataset


def equal_data_files(n_steps, dt_array):  # Function that interpolates all the datasets to match the number of data and time
    max_time_intersection = max_time_intersection_f(n_steps, dt_array)  # Function that measure the common maxium time in all the files 
    length_dataset = lenght_dataset_f(max_time_intersection, dt_array)  # Function that measure the amount of data in the biggest file
    path = "C:/Users/EQ01/Desktop/Folders/Trabajo/UPB/Research group/SOH/codes/WebEquation/src/results/stability/TOF_df"
    os.chdir(path)

    for file in os.listdir():
        if file.endswith(".csv"):
            df = np.loadtxt(file, delimiter =',')  # Deformation array
            nodes_str = re.split("[-]", file)  # Takes de nodes in the file name
            nodes_str = f'{nodes_str[1]}'
            dt_str = re.split("[-dt.]", file)  # Takes the dt in the file name
            dt_str = f'{dt_str[-3]}-{dt_str[-2]}'  # Takes the dt in the file name
            dt = float(dt_str)
            y, lowest_time, highest_time = time_array(dt, n_steps, dt_array, max_time_intersection)  # Generates the time array
            function = interpolate.interp1d(y, df)  # Interpolate function of time vs deformation
            interpolation(length_dataset, function, lowest_time, highest_time, nodes_str, dt_str)  # interpolates adding the number of data as the biggest file
import pandas as pd
import os
from . import functions
import re

def stability_f(dt_array, n_steps):
    slice_dict = functions.dict_iter_number_f(dt_array, n_steps)  # Return a dict to allow the slicing of the dataframes

    path = "C:/Users/EQ01/Desktop/Folders/Trabajo/UPB/Research group/SOH/codes/WebEquation/src/results/stability/dataframes"
    os.chdir(path)  # Change the path to read the datasets 
    for file in os.listdir():  # for loop for all the files
        if file.endswith(".csv"):  # if they are .csv
            #file_path = f"{path}/{file}"  # This allows to take the absolute path of each file
            df = pd.read_csv(file)  # reads the dataset
            dt_str = re.split("[-dt.]", file)  # Takes de dt in the file name
            dt_str = f'{dt_str[-3]}-{dt_str[-2]}'  # Takes de dt in the file name
            dt = float(dt_str)
            nodes_str = re.split("[-]", file)  # Takes de nodes in the file name
            nodes_str = f'{nodes_str[1]}'
            # res = isinstance(str_1, str)
            # print("Is variable a string ? : " + str(res))
            iter_number = functions.read_iter_number(dt, slice_dict)  # Checks the iter number to slice the corresponding to the current dataset            
            functions.slice_df(iter_number, df, nodes_str, dt_str)  # Saves the new dataset

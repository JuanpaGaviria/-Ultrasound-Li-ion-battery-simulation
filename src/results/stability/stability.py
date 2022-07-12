import pandas as pd
import os

def stability_f():
    path = "C:/Users/EQ01/Desktop/Folders/Trabajo/UPB/Research group/SOH/codes/WebEquation/src/results/stability/dataframes"
    os.chdir(path)
        
    for file in os.listdir():
        if file.endswith(".csv"):
            #file_path = f"{path}/{file}"
            df = pd.read_csv(file)
        

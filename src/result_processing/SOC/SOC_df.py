import pandas as pd
import os
import re
from .functions import *


def SOC_comparison(reading_path, main_path, cut_imput):

    """
    1. Read the dataset
    2. Split the deformation at the first node of all the results and creates a new dataset
    3. Create a dataframe with all the results with columns, where each column is a result
    4. Plot the dataframe
    """

    os.chdir(reading_path)  # saves it in a different folder

    count = 0
    for file in os.listdir():
        if file.endswith(".csv"):
            name = re.split("[.]", file)
            name = name[0]
            dataset = pd.read_csv(file, header=None, delimiter=",")
            output_dataframe(dataset, name, cut_imput)

    os.chdir(main_path)


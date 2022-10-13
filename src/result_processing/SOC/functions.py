import matplotlib.pyplot as plt
import pandas as pd
import os
import re


def output_dataframe(dataset, name, cut_imput):

    """
    Read the amplitude at node = 0
    A folder called Dataset and other folder called SOC_output must be created.
    """

    df_node_0 = dataset.iloc[0, cut_imput:]
    os.chdir('../SOC_output/')
    df_node_0.to_pickle(f'{name}.pkl')
    print('saved', f'{name}')
    os.chdir('../Dataset')

def df_creation(reading_path):

    """
    Creates the new dataframe
    """

    os.chdir(reading_path)

    columns = []
    files = []
    count = 0
    for file in os.listdir():
        if file.endswith(".pkl"):
            name = re.split("[.]", file)
            name = name[0]
            columns.append(name)
            files.append(file)
            count += 1

    df = pd.concat([pd.read_pickle(f) for f in files], axis = 1)
    df.columns = columns
    sort_columns = ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100']
    df = df.reindex(columns = sort_columns)

    return df, count

def plot(df, n, style):

    """
    Plot the SOC comparison
    """

    plt.style.use(style)
    fig, a = plt.subplots(n, 1, figsize=(20, 20), tight_layout=True, sharex = True)
    df.plot(ax=a, subplots=True, rot=60)
    plt.savefig('SOC.png')
import numpy as np
import os


def max_time_intersection_f(n_steps, dt_array):  # Function that measure the common maxium time in all the files 
    dt_array.sort()  # Sorts the dt_array
    max_time_intersection = n_steps*dt_array[0]  # computes the maximum time value that intersect the datasets
    return max_time_intersection

def lenght_dataset_f(max_time_intersection, dt_array):  # Function that measure the amount of data in the biggest file
    dt_array.sort()
    dt = dt_array[0]
    length_dataset = max_time_intersection/dt
    return length_dataset

def time_array(dt, n_steps, dt_array, max_time_intersection):  # Function to generate the Y time array    
    number = int(max_time_intersection/dt)  #+1  # determine the shape of the time array
    time = (n_steps * dt)  # Computes the time interval 
    times = np.linspace(0, time, num = number)  # generates the array
    lowest_time = np.amin(times)
    highest_time = np.amax(times)
    return times, lowest_time, highest_time

def interpolation(length_dataset, function, lowest_time, highest_time, nodes_str, dt_str):
    step = highest_time/length_dataset
    new_time = np.arange(lowest_time, highest_time, step)
    df = function(new_time)
    path_TOF_matching_data = "C:/Users/EQ01/Desktop/Folders/Trabajo/UPB/Research group/SOH/codes/WebEquation/src/implicit/results/stability/TOF_matching_data"
    os.chdir(path_TOF_matching_data)  # saves it in a different folder
    np.savetxt(f'node-{nodes_str}-dt-{dt_str}.csv', df, delimiter=',')
    path = "C:/Users/EQ01/Desktop/Folders/Trabajo/UPB/Research group/SOH/codes/WebEquation/src/implicit/results/stability/TOF_df"
    os.chdir(path)  # Change the path to read the datasets
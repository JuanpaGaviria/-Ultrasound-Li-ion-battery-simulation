import numpy as np
import pandas as pd

def courant(dx, dt, ms, idx, mat):

    courant_material=[]

    for i in range(len(ms)):
        courant_material.append((ms[i].square_velocity*dt**2)/dx**2)
        if courant_material[i] >= 1:
            print("Courant higher than 1, with a value of", courant_material[i],\
                ", name", idx[i],"-", mat[i])

    return courant_material 

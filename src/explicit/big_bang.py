# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 15:32:05 2021

@author: EQ01
"""
import numpy as np
from src.explicit.boundary import Material

# Class instantiation for each material and methods implementation
def big_bang_f(indexes, df, nodes, battery_map):

    materials=[] #Materials list for the test
    materials_summary=[]#Objects
    thickness_summary=[] #Dimensional thickness for each material in the test
    dimensionless_lengths=[] #Dimensionless thickness for each material in the test
    dimensionless_position=[] #Dimensionless position of each material
    #courant_material=[] #Courant list for each material
    materials_e_modulus = []
    materials_number=int(len(indexes))
    dimensionless_thickness=None
    dimensionless_length=None

    for i in range(materials_number):
        g=indexes[i]
        a=df._get_value(g,'Type')
        materials.append(a)

    df=df.set_index('Type')
    for j in range(materials_number):
        b=materials[j]#Takes a material from the data frame
        density=df.loc[b,'density']
        e_modulus=df.loc[b, 'e_modulus']
        thickness=df.loc[b, 'thickness']
        State=df.loc[b, 'state']
        bulk_modulus=df.loc[b, 'bulk_modulus']
        material=Material(density, e_modulus, State, bulk_modulus)#constructor
        materials_e_modulus.append(material.e_modulus)  # stores each elastic modulus in a list
        materials_summary.append(material)
        material.length(thickness)#length
        thickness_summary.append(material.thickness_summary[-1])

        #Definning the length where the wave propagates
        if j==materials_number-1:
        # dimensional length
            summ=0
            for i in range(len(thickness_summary)):#Sum the thickness of each material
                summ=summ + thickness_summary[i]

            dimensionless_length=0
            # dimensionless length
            for i in range(len(thickness_summary)):
                value=thickness_summary[i]
                dimensionless_thickness=value/summ
                dimensionless_lengths.append(dimensionless_thickness)
                dimensionless_length=dimensionless_length+dimensionless_thickness

            #The dimensionless position of each material
            positions=0
            #print(thickness_summary)
            for i in range(len(thickness_summary)):
                positions=positions+dimensionless_lengths[i]
                dimensionless_position.append(positions)


    _e_modulus_dict = dict(zip(indexes, materials_e_modulus))
    for _e_modulus in range(len(battery_map)):
        _id = battery_map[_e_modulus]
        e_modulus = _e_modulus_dict[_id]

    dx=dimensionless_length/(nodes-1)
    
    x=np.linspace(0,dimensionless_length,nodes)

    return dx, x, dimensionless_length, dimensionless_position , material, \
        dimensionless_thickness, materials_summary, thickness_summary,\
            dimensionless_lengths, materials, _e_modulus_dict
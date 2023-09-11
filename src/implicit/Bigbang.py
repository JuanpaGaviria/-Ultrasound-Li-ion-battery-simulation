import numpy as np
import pandas as pd
from src.implicit.material_constructor import Material

def big_bang(indexes, df, nodes, battery_map, dt, cfl, dimensionless):

    materials = []  # Material type present in the test (str)
    materials_summary = []  # Material instantiation
    materials_number = int(len(indexes))  # Amount of different materials present in the test
    materials_thickness = []  # thickness
    material_dimensionless_length = []  # dimensionaless thickness
    material_dimensional_length = []  # dimensionaless thickness
    interphase_position = []  # interphase position
    materials_e_modulus = []  # e_modulus for each index
    summary_e_modulus = []  # e_modulus for the map
    materials_gamma = []
    gamma_map = []
    materials_phi = []
    phi_map = []
    # Obtaining the materials type
    for i in range(materials_number):
        idx = indexes[i]  # takes index i
        _type = df._get_value(idx, "Type")  # From de data frame (df) takes the str Type at the index i
        materials.append(_type)  # Add the str Type in the list materials

    # Obtaining the materials attributes
    df = df.set_index('Type')  # Type column is set as the index of the data frame
    df['density'] = df['density'].astype(float)
    df['thickness'] = df['thickness'].astype(float)
    df['e_modulus'] = df['e_modulus'].astype(float)
    df['c'] = df['c'].astype(float)
    for j in range(materials_number):
        _material = materials[j]  # takes each materials type to get attributes
        density = df.loc[_material, 'density'] # Takes density for each material
        e_modulus = df.loc[_material, 'e_modulus']  # Takes elastic modulus for each material
        thickness = df.loc[_material, 'thickness']  # Takes thickness for each material
        state = df.loc[_material, 'state']  # Takes state for each material
        bulk_modulus = df.loc[_material, 'bulk_modulus']  # Takes bulk modulus for each material

        # Material class instantiation
        material = Material(density, e_modulus, state, bulk_modulus, thickness, _material)  # material instantiation
        materials_summary.append(material)  # stores each material in a list
        materials_thickness.append(material.thickness)  # stores each material thickness in a list
        materials_e_modulus.append(material.e_modulus)  # stores each elastic modulus in a list

    # Length definition
    length = 0
    _dict = dict(zip(indexes, materials_thickness))  # creates a dictionary
    for _length in range(len(battery_map)):  # computes the total length
        _id = battery_map[_length]
        thick = _dict[_id]
        length = length + thick

    _e_modulus_dict = dict(zip(indexes, materials_e_modulus))
    for _e_modulus in range(len(battery_map)):
        _id = battery_map[_e_modulus]
        e_modulus = _e_modulus_dict[_id]
        summary_e_modulus.append(e_modulus)
    
    max_velocity = 0
    for _velocity in range(len(indexes)):
        _material = materials[_velocity]  # takes each materials type to get attributes
        velocity = df.loc[_material, 'c']
        if velocity > max_velocity:
            max_velocity = velocity
    if dimensionless:
        
        # dimensionless length definition
        for _dimensionless_thicks in range(len(battery_map)):  # computes the dimensionless thickness
            _id = battery_map[_dimensionless_thicks]
            dimensionless_thickness = _dict[_id] / length
            material_dimensionless_length.append(dimensionless_thickness)  # save each dimensionless thickness in a list

        # definition of the interphase positions
        positions = 0
        for _interphase_position in range(len(battery_map)-1):
            positions = positions + material_dimensionless_length[_interphase_position]
            interphase_position.append(positions)

        dimensionless_length = 0
        for _dimensionless_length in range(len(material_dimensionless_length)):  # checking total dimensionless length = 1
            dimensionless_length = dimensionless_length + material_dimensionless_length[_dimensionless_length]
        
        if not nodes:
            # dx = dt*np.sqrt(2)*higher_velocity/(cfl)
            dx = dt*max_velocity/(cfl)
            nodes = int(dimensionless_length/dx)
        else:
            dx = dimensionless_length/(nodes-1)
        x = np.linspace(0, dimensionless_length, nodes)
        print('nodes',nodes)
        print('dimensionless length', dimensionless_length)
        print('dx', dx)


    else:
        # dimensionless length definition
        for _thicks in range(len(battery_map)):  # computes the dimensionless thickness
            _id = battery_map[_thicks]
            dimensional_thickness = _dict[_id]
            material_dimensional_length.append(dimensional_thickness)  # save each dimensionless thickness in a list

        positions = 0
        for _interphase_position in range(len(battery_map)-1):
            positions = positions + material_dimensional_length[_interphase_position]
            interphase_position.append(positions)

        if not nodes:
            
            # dx = dt*np.sqrt(2)*higher_velocity/(cfl)
            dx = dt*max_velocity/(cfl)
            nodes = int(length/dx)
        else:   
            dx = length/(nodes-1)
        x = np.linspace(0, length, nodes)
        print("nodes", nodes)
        print("length", length)
        print("dx", dx)

    for _gamma_phi in range(materials_number):
        materials_summary[_gamma_phi].gamma_phi_m(dt, dx)
        gamma = materials_summary[_gamma_phi].gamma
        phi = materials_summary[_gamma_phi].phi
        materials_gamma.append(gamma)
        materials_phi.append(phi)

    gamma_dict = dict(zip(indexes, materials_gamma))
    phi_dict = dict(zip(indexes, materials_phi))
    for _gamma_phi in range(len(battery_map)):
        _id = battery_map[_gamma_phi]
        gamma = gamma_dict[_id]
        phi = phi_dict[_id]
        gamma_map.append(gamma)
        phi_map.append(phi)
    
    return x, interphase_position, _e_modulus_dict, gamma_map, phi_map, materials_summary, nodes, dx, max_velocity

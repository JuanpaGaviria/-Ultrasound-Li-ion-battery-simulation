from typing import List


def battery_structure(geometric_unit: List[int], layer_number: int, case: bool):

    """
    Battery structure method allow to create the battery geometric.

    Params:
    geometric_unit: list of the composition wrappred
    layer_number: number of layers to create the geometry
    case: if False, the case is not considered. This material is considered to be in the 0th position
    """

    _layers_number = int(layer_number / 2)  # this is needed to add the second half of the layers

    battery_map = []  # List where the map is stored
    count = 0  # used at the buckle
    _count = 0  # used at the buckle
    for i in range(layer_number):
        battery_map.append(geometric_unit[count])  # adds a first material to the map list
        count = count+1  # jumps to the next material (group counter)
        _count = _count+1  # jumps to the next material (layers counter)
        if count == len(geometric_unit):
            count = 0  # returns to the first material
        if _count == (layer_number / 2):  # the center is reached
            count = len(geometric_unit)-1  # takes the last index
            for j in range(_layers_number):  # materials are added but in an opposite order for the second half
                battery_map.append(geometric_unit[count])
                count = count-1
                if count < 0:
                    count = len(geometric_unit)-1
            break
    
    if case:
        battery_map.insert(0,0)
        battery_map.append(0)

    return battery_map

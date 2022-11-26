def battery_structure(indexes, layer_number):  # method to construct the battery map

    _layers_number = int(layer_number / 2)  # this is needed to add the second half of the layers

    battery_map = []  # List where the map is stored
    count = 0  # used at the buckle
    _count = 0  # used at the buckle
    for i in range(layer_number):
        battery_map.append(indexes[count])  # adds a first material to the map list
        count = count+1  # jumps to the next material (group counter)
        _count = _count+1  # jumps to the next material (layers counter)
        if count == len(indexes):
            count = 0  # returns to the first material
        if _count == (layer_number / 2):  # the center is reached
            count = len(indexes)-1  # takes the last index
            for j in range(_layers_number):  # materials are added but in an opposite order for the second half - optimizar
                battery_map.append(indexes[count])
                count = count-1
                if count < 0:
                    count = len(indexes)-1
            break

    return battery_map
def battery_structure(indexes, geometry_unit):  # method to construct the battery map

    _geometry_unit = int(geometry_unit / 2)  # this is needed to add the second half of the layers

    battery_map = []  # List where the map is stored
    count = 0  # used at the buckle
    _count = 0  # used at the buckle
    for i in range(geometry_unit):
        battery_map.append(indexes[count])  # adds a first material to the map list
        count = count+1  # jumps to the next material (group counter)
        _count = _count+1  # jumps to the next material (layers counter)
        if count == len(indexes):
            count = 0  # returns to the first material
        if _count == (geometry_unit / 2)+1:  # the center is reached
            count = len(indexes)-1  # takes the last index
            for j in range(_geometry_unit):  # materials are added but in an opposite order for the second half
                battery_map.append(indexes[count])
                count = count-1
                if count < 0:
                    count = len(indexes)-1
            break
    
    # battery_map.insert(0,0)
    # battery_map.append(0)

    return battery_map

def courant(dx, dt, indexes, maerials_summary):

    courant_material=[]

    for i in range(len(maerials_summary)):
        courant_material.append(((maerials_summary[i].square_velocity)**(1/2)*dt)/dx)
        
    return courant_material
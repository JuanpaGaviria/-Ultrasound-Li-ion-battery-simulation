def courant(dx, dt, higher_velocity):

    CFL_value = (higher_velocity*dt)/dx
        
    return CFL_value
def courant(dx, dt,rescale_t,rescale_x,higher_velocity):

    CFL_value = (higher_velocity*dt)/dx

    if rescale_t:
        CFL_value = CFL_value/rescale_t
        
    return CFL_value
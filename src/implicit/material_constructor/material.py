class Material:
    # Constructor
    def __init__(self, density, e_modulus, state, bulk_modulus, thickness, _type):
        self.density = density
        self.e_modulus = e_modulus
        self.state = state
        self.bulk_modulus = bulk_modulus
        self.thickness = thickness
        self.type = _type
        self.gamma = None
        self.phi = None

    def gamma_phi_m(self, dt, dx, rescale_t, rescale_x, rescale_thickness):  # computing abbreviations
      
        if rescale_x or rescale_thickness:
            
            if rescale_thickness:
                 alpha =  self.thickness**2
            else:
                alpha =  rescale_x**2
        else:
            alpha = 1
        
        if rescale_t:
            beta = rescale_t**2
        else:
            beta = 1

        self.gamma = (self.density * alpha * dx**2) / (self.e_modulus * beta * dt**2)
        self.phi = self.gamma*12



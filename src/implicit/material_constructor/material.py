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
        if self.state == "liquid":
            self.square_velocity = self.bulk_modulus / self.density
        else:
            self.square_velocity = self.e_modulus / self.density

    def gamma_phi_m(self, dt, dx):  # computing abbreviations
        self.gamma = self.density * dx**2 / (self.e_modulus * dt**2)
        self.phi = self.gamma * 12

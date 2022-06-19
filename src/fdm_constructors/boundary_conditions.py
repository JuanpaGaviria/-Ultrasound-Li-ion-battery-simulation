class BCs:
    def __init__(self):
        self.u_left_value = None
        self.u_right_value = None

    #  Left boundary conditions
    def left_soft_bc(self, uj_1, uj_2):
        self.u_left_value = (4*uj_1-uj_2)/3

    def left_open_bc(self, uj_1, uj_2):
        pass

    def left_dirichlet_bc(self):
        self.u_left_value = 0

    #  Right boundary conditions
    def right_soft_bc(self, uj__1):
        self.u_right_value = uj__1

    def right_open_bc(self, uj__1, uj__2):
        pass

    def right_dirichlet_bc(self):
        pass

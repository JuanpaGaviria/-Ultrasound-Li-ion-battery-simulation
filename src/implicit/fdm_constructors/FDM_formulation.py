from abc import ABCMeta, abstractmethod


class ImplicitFormulation(metaclass=ABCMeta):

    @abstractmethod
    def node_0_dirichlet(self, left):
        pass

    @abstractmethod
    def node_0_neumann(self):
        pass

    @abstractmethod
    def time_0_node_1_dirichlet(self, gamma, u_left, initial_velocity, dt, uj_0):
        pass

    @abstractmethod
    def time_0_node_2_dirichlet(self, phi, u_left, initial_velocity, dt, uj_0):
        pass

    @abstractmethod
    def time_0_internal_node(self, phi, initial_velocity, dt, uj_0):
        pass

    @abstractmethod
    def time_0_node__1_interphase(self, gamma, initial_velocity, dt, uj_0):
        pass

    @abstractmethod
    def time_0_interphase(self, alpha):
        pass

    @abstractmethod
    def time_0_node_1_interphase(self, gamma, initial_velocity, dt, uj_0):
        pass

    @abstractmethod
    def time_0_penultimate_node(self, phi, initial_velocity, dt, u_right, uj_0):
        pass

    @abstractmethod
    def time_0_last_node(self, gamma, initial_velocity, dt, u_right, uj_0):
        pass

    @abstractmethod
    def node_1_dirichlet(self, gamma, uj_0, uj_1, u_left):
        pass

    @abstractmethod
    def node_1_neumann(self, gamma, uj_0, uj_1):
        pass

    @abstractmethod
    def node_2_dirichlet(self, phi, uj_0, uj_1, u_left):
        pass

    @abstractmethod
    def internal_node(self, phi, uj_0, uj_1):
        pass

    @abstractmethod
    def node__1_interphase(self, gamma, uj_0, uj_1):
        pass

    @abstractmethod
    def interphase(self, alpha):
        pass

    @abstractmethod
    def node_1_interphase(self, gamma, uj_0, uj_1):
        pass

    @abstractmethod
    def penultimate_node(self, phi, uj_0, uj_1, u_right):
        pass

    @abstractmethod
    def last_node(self, gamma, uj_0, uj_1, u_right):
        pass


class InputWave_5(ImplicitFormulation):

    def __init__(self):
        self.alpha = None
        self.a_i_i = None  # U^j_i
        self.a_i_i1 = None  # U^j_(i+1)
        self.a_i_i2 = None  # U^j_(i+2)
        self.a_i_i_1 = None  # U^j_(i-1)
        self.a_i_i_2 = None  # U^j_(i-2)
        self.b = None

    def alpha_m(self, e_modulus_1, e_modulus_2):
        self.alpha = e_modulus_2 / e_modulus_1

    def node_0_dirichlet(self, u_left):
        self.a_i_i = 1
        self.b = u_left

    def node_0_neumann(self):
        self.a_i_i = 1
        self.a_i_i1 = -1
        self.b = 0

    def time_0_node_1_dirichlet(self, gamma, u_left, initial_velocity, dt, uj_0):  # Node 1

        self.a_i_i = gamma + 2
        self.a_i_i1 = - 1
        self.b = (gamma*uj_0) - (gamma*initial_velocity*dt) + u_left

    def time_0_node_2_dirichlet(self, phi, u_left, initial_velocity, dt, uj_0):  # Node 2

        self.a_i_i_1 = 16
        self.a_i_i = -(30 + phi)
        self.a_i_i1 = 16
        self.a_i_i2 = -1
        self.b = (-initial_velocity*dt) - (phi*uj_0) + u_left

    def time_0_internal_node(self, phi, initial_velocity, dt, uj_0):  # Internal nodes

        self.a_i_i_2 = -1
        self.a_i_i_1 = 16
        self.a_i_i = -(30 + phi)
        self.a_i_i1 = 16
        self.a_i_i2 = -1
        self.b = (-initial_velocity*dt) - (phi*uj_0)

    def time_0_node__1_interphase(self, gamma, initial_velocity, dt, uj_0):  # Node before an interface

        self.a_i_i_1 = -1
        self.a_i_i = gamma + 2
        self.a_i_i1 = -1
        self.b = (gamma*uj_0) - (initial_velocity * dt)

    def time_0_interphase(self, alpha):  # Interface

        self.a_i_i_2 = 1
        self.a_i_i_1 = - 4
        self.a_i_i = 3 * (1 + alpha)
        self.a_i_i1 = - 4 * alpha
        self.a_i_i2 = alpha
        self.b = 0

    def time_0_node_1_interphase(self, gamma, initial_velocity, dt, uj_0):  # Node after interface

        self.a_i_i_1 = -1
        self.a_i_i = gamma + 2
        self.a_i_i1 = -1
        self.b = (gamma*uj_0) - (initial_velocity * dt)

    def time_0_penultimate_node(self, gamma, initial_velocity, dt, uj_0):  # Penultimate Node

        self.a_i_i_1 = -1
        self.a_i_i = gamma + 2
        self.a_i_i1 = -1
        self.b = (gamma*uj_0) - (initial_velocity*dt)

    def time_0_last_node(self):  # Last node

        self.a_i_i_1 = 1
        self.a_i_i = -1
        self.b = 0

    def node_1_dirichlet(self, gamma, uj_0, uj_1, u_left):  # first node

        self.a_i_i = (gamma + 2)
        self.a_i_i1 = -1
        self.b = (2*gamma*uj_0) - (gamma*uj_1) + u_left

    def node_1_neumann(self, gamma, uj_0, uj_1):
        
        self.a_i_i_1 = -1
        self.a_i_i = (gamma + 2)
        self.a_i_i1 = -1
        self.b = (2*gamma*uj_0) - (gamma*uj_1)

    def node_2_dirichlet(self, phi, uj_0, uj_1, u_left):  # second node

        self.a_i_i_1 = 16
        self.a_i_i = -(30+phi)
        self.a_i_i1 = 16
        self.a_i_i2 = -1
        self.b = (phi*uj_1) - (2*phi*uj_0) + u_left

    def internal_node(self, phi, uj_0, uj_1):  # Internal node
        self.a_i_i_2 = -1
        self.a_i_i_1 = 16
        self.a_i_i = -(30+phi)
        self.a_i_i1 = 16
        self.a_i_i2 = -1
        self.b = (phi*uj_1) - (2*phi*uj_0)

    def node__1_interphase(self,  gamma, uj_0, uj_1):  # Node before interface

        self.a_i_i_1 = -1
        self.a_i_i = (gamma+2)
        self.a_i_i1 = - 1
        self.b = (2*gamma*uj_0) - (gamma*uj_1)

    def interphase(self, alpha):  # Interface

        self.a_i_i_2 = 1
        self.a_i_i_1 = - 4
        self.a_i_i = 3 * (1 + alpha)
        self.a_i_i1 = - 4 * alpha
        self.a_i_i2 = alpha
        self.b = 0

    def node_1_interphase(self, gamma, uj_0, uj_1):  # Node after interface

        self.a_i_i_1 = -1
        self.a_i_i = (gamma+2)
        self.a_i_i1 = - 1
        self.b = (2*gamma*uj_0) - (gamma*uj_1)

    def penultimate_node(self, gamma, uj_0, uj_1):  # Penultimate node

        self.a_i_i_1 = -1
        self.a_i_i = (gamma+2)
        self.a_i_i1 = - 1
        self.b = (2*gamma*uj_0) - (gamma*uj_1)

    def last_node(self):  # last node

        self.a_i_i_1 = 1
        self.a_i_i = -1
        self.b = 0


class InputWave_3(ImplicitFormulation):
    
    def __init__(self):
        self.alpha = None
        self.a_i_i = None  # U^j_i
        self.a_i_i1 = None  # U^j_(i+1)
        self.a_i_i_1 = None  # U^j_(i-1)

        self.b = None

    def alpha_m(self, e_modulus_1, e_modulus_2):
        self.alpha = e_modulus_2 / e_modulus_1

    def node_0_dirichlet(self, u_left):
        self.a_i_i = 1
        self.b = u_left

    def node_0_neumann(self):
        self.a_i_i = 1
        self.a_i_i1 = -1
        self.b = 0

    def time_0_internal_node(self, gamma, initial_velocity, dt, uj_0):  # Internal nodes

        self.a_i_i_1 = -1
        self.a_i_i = (gamma+2)
        self.a_i_i1 = - 1
        self.b = (-gamma*initial_velocity*dt) + (gamma*uj_0)


    def time_0_interphase(self, alpha):  # Interface

        self.a_i_i_2 = 1
        self.a_i_i_1 = - 4
        self.a_i_i = 3 * (1 + alpha)
        self.a_i_i1 = - 4 * alpha
        self.a_i_i2 = alpha
        self.b = 0
    
    def time_0_last_node(self):  # Last node

        self.a_i_i_1 = 1
        self.a_i_i = -1
        self.b = 0

    def node_1_dirichlet(self, gamma, uj_0, uj_1, u_left):  # first node

        self.a_i_i = (gamma + 2)
        self.a_i_i1 = -1
        self.b = (2*gamma*uj_0) - (gamma*uj_1) + u_left

    def internal_node(self, gamma, uj_0, uj_1):
        
        self.a_i_i_1 = -1
        self.a_i_i = (gamma + 2)
        self.a_i_i1 = -1
        self.b = (2*gamma*uj_0) - (gamma*uj_1)

    def interphase(self, alpha):  # Interface

        self.a_i_i_2 = 1
        self.a_i_i_1 = - 4
        self.a_i_i = 3 * (1 + alpha)
        self.a_i_i1 = - 4 * alpha
        self.a_i_i2 = alpha
        self.b = 0

    def last_node(self):  # last node

        self.a_i_i_1 = 1
        self.a_i_i = -1
        self.b = 0

    def time_0_node_1_dirichlet(self, gamma, u_left, initial_velocity, dt, uj_0):  # Node 1

        self.a_i_i = gamma + 2
        self.a_i_i1 = - 1
        self.b = (gamma*uj_0) - (gamma*initial_velocity*dt) + u_left

    def time_0_node_2_dirichlet(self, phi, u_left, initial_velocity, dt, uj_0):  # Node 2

        pass   

    def time_0_node__1_interphase(self, gamma, initial_velocity, dt, uj_0):  # Node before an interface

        pass
    def time_0_node_1_interphase(self, gamma, initial_velocity, dt, uj_0):  # Node after interface

        pass

    def time_0_penultimate_node(self, gamma, initial_velocity, dt, uj_0):  # Penultimate Node

        pass

    def node_1_neumann(self, gamma, uj_0, uj_1):
        
        pass

    def node_2_dirichlet(self, phi, uj_0, uj_1, u_left):  # second node

        pass
        
    def node__1_interphase(self,  gamma, uj_0, uj_1):  # Node before interface

        pass

    def node_1_interphase(self, gamma, uj_0, uj_1):  # Node after interface

        pass

    def penultimate_node(self, gamma, uj_0, uj_1):  # Penultimate node

        pass

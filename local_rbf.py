import numpy as np
from numpy.linalg import inv
import matplotlib.pylab as plt
import winsound

#Defininf functions 
def phi_matrix_f(stencil_length, stencil, c):
    phi = np.zeros((stencil_length, stencil_length))
    for row in range(stencil_length):
        for col in range(stencil_length):
            r = np.linalg.norm(stencil[row]-stencil[col])
            phi[row, col] = np.sqrt(r**2 + c**2)
    return phi

def so_phi_f(stencil_length, stencil, c):
    so_phi = np.zeros(stencil_length)
    for col in range(stencil_length):
        r = np.linalg.norm(stencil[0]-stencil[col])
        so_phi[col] = c**2/((c**2+r**2)**(3/2))
    return so_phi

#Input variables
nodes = 100
vel=0.
distance = 1
dx = distance/(nodes-1)
_x = np.linspace(0, distance, nodes)
f = np.sin(np.pi * _x)
phi = np.zeros((nodes, nodes))
c = 10
nsteps = 200
dt = 1e-4
time = nsteps * dt
elastic_modulus = 1
density = 1
initial_velocity = 1
k = ((elastic_modulus*dt**2)/density)
_y = [ 0, 0.47675, -0.62681, 0.66253, -0.55683, 0.08213, -0.052714, 0.020251, -0.0069143, 0.0016148]
stencil_length = 3
r=elastic_modulus*dt**2/(density*dx**2)

c_matrix = np.zeros((nodes-2, stencil_length))

#Matrix definition and vectors
A=np.zeros((nodes-2,nodes-2))
B=np.zeros(nodes-2)
Uj0=np.zeros(nodes-2) #Ujpresent
Uj1=np.zeros(nodes-2) #Ujfutur
Uj_1=np.zeros(nodes-2) #Ujpast
H=np.zeros((nodes,nsteps+1)) #Matrix where the solution is stored after iteration

#Construction of matrix c (SO_PHI*INV(PHI))
for i in range(0, nodes-2):
    stencil = np.zeros(stencil_length)
    stencil[0] = _x[i]
    stencil[1] = _x[i + 1]
    stencil[2] = _x[i + 2]
    inverse_phi = np.linalg.inv(phi_matrix_f(stencil_length, stencil, c))
    so_phi_matrix = so_phi_f(stencil_length, stencil, c)
    c_matrix[i, :] = np.dot(so_phi_matrix, inverse_phi)

#Boundary conditions
Uleft=0
Uright=0

#Initial condition
x=np.linspace(0,distance,nodes-2) #x=xnodes[1:4:1] indexacion de arreglos (slicing)
Uj0=np.sin(np.pi*x)

#Saving initial condition in matrix H 
Uj0t=np.hstack([Uleft, Uj0, Uright])
H[:,0]=Uj0t

#Coeficiente de constantes
r=elastic_modulus*dt**2/(density*dx**2)

#Esquema implicito: Armado 
for j in range(0,nsteps):
    if j==0: 
        Uleft=0
        for i in range(0,nodes-1):
            if i==0:
                A[i,i]=1-r*c_matrix[0,1]
                A[i,i+1]=-r*c_matrix[0,2]
                B[i]=Uj0[i]+r*Uleft*c_matrix[0,0]+vel*dt
            if i>0 and i<nodes-3:
                A[i,i-1]=-r*c_matrix[0,0]
                A[i,i]=1-r*c_matrix[0,1]
                A[i,i+1]=-r*c_matrix[0,2]
                B[i]=Uj0[i]+vel*dt
            if i==nodes-3:
                A[i,i-1]=-r*c_matrix[0,0]
                A[i,i]=1-r*c_matrix[0,1]
                B[i]=Uj0[i]+vel*dt+r*Uright*c_matrix[0,2]
        Uj1=np.linalg.solve(A,B)
        Uj1t=np.hstack([Uleft, Uj1, Uright])
        H[:,j+1]=Uj1t[:]
        Uj_1=Uj0
        Uj0=Uj1
            
    if j>0: 
        for i in range(0,nodes-1):
            if i==0:
                A[i,i]=1-r*c_matrix[0,1]
                A[i,i+1]=-r*c_matrix[0,2]
                B[i]=2*Uj0[i]-Uj_1[i]+r*Uleft*c_matrix[0,0]
            if i>0 and i<nodes-3:
                A[i,i-1]=-r*c_matrix[0,0]
                A[i,i]=1-r*c_matrix[0,1]
                A[i,i+1]=-r*c_matrix[0,2]
                B[i]=2*Uj0[i]-Uj_1[i]
            if i==nodes-3:
                A[i,i-1]=-r*c_matrix[0,0]
                A[i,i]=1-r*c_matrix[0,1]
                B[i]=2*Uj0[i]- Uj_1[i] +r*Uright
        Uj1=np.linalg.solve(A,B)
        Uj1t=np.hstack([Uleft, Uj1, Uright])
        H[:,j+1]=Uj1t[:]
        Uj_1=Uj0
        Uj0=Uj1

for i in range(0,nsteps+1):
    plt.cla()# borra pantalla anterior del plot
    plt.xlim(0,1.)
    plt.ylim(-2,2.)
    plt.plot(_x,H[:,i],color='r')
    # titulo= 'propagation'
    # plt.title(titulo)
    plt.grid()
    plt.pause(0.00000000000000001)
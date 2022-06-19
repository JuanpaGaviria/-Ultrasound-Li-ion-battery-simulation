from platform import node
import numpy as np 
import matplotlib.pyplot as plt

#Read H file:
H = np.loadtxt('H.txt', delimiter=',')
#print(H)

node_zero = []
node_one = []

for i in range(H.shape[1]):
    
    u0 = H[0, i]
    u1 = H[1, i]
    
    node_zero.append(u0)
    node_one.append(u1)

def dudt(u0, u1, dt):
    
    dd = []
    
    for i in range(len(u0)):
    
        du_dt = (u1[i]-u0[i])/dt
        dd.append(du_dt)
    
    return dd

TOFd = dudt(node_zero, node_one, 0.05)
#print(TOFd)

sign_evaluation = []

for i in TOFd:
    
    if i > 0:
        sign_evaluation.append(1)
        
    else:
        sign_evaluation.append(-1)
        
dudt_change = []

for idx, i in enumerate(sign_evaluation):
    
    if idx == 0:
        pass
    else:
        #print(f' idx 1')
        if sign_evaluation[idx] != sign_evaluation[idx-1]:
            
            dudt_change.append(idx)
            
        else:
            
            pass

TOF = np.zeros(len(node_zero))

for idx in dudt_change:
    
    TOF[idx] = node_zero[idx]


plt.plot(TOF)
plt.show()

print(TOF)
            
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 15:20:41 2021

@author: EQ01
"""

import numpy as np

class Material():
    #constructor
    def __init__(self, density, e_modulus, state, bulk_modulus):
        self.state=state
        self.bulk_modulus=bulk_modulus
        self.density=density
        self.e_modulus=e_modulus
        self.thickness_summary=[] #Dimensional thickness for each material in the test
        if state == 'liquid':
            self.square_velocity=self.bulk_modulus/self.density
            print(self.square_velocity, self.state)
        else:
            self.square_velocity=self.e_modulus/self.density
            print(self.square_velocity, self.state)
    # Thickness method
    def length(self, thickness):#Length
        self.thickness=thickness
        self.thickness_summary.append(self.thickness)

#Left boundary conditions
    # This condition is for a non recessed wave, u is computed with the two right nodes
    def leftbc_open(self, courant, uj0i, uj01, uj02):
        self.uj1=(uj0i*((2+(3*courant)+courant**2)/2))-\
            (uj01*(2*courant+courant**2))+(uj02*(courant+courant**2)/2)
        
    def leftbc_soft(self, uj01, uj02):
        self.uj1=(4*uj01-uj02)/3
        
    def in_put(self, j):
        amplitud=1.5
        period=1/5
        self.uj1=amplitud*np.cos(-(2*np.pi*j)/period)
    
    def armonic(self, x):
        self.uj0=np.exp(-((x-0.5)/0.1)**2) #np.sin(np.pi*x[i]) 


#Rigth boundary conditions            
    def rightbc_open(self, uj0i, courant, uj0i_1,uj0i_2):
        self.uj1=uj0i*((2+(3*courant)+courant**2)/2)-(uj0i_1*(2*courant\
                            +courant**2))+(uj0i_2*(courant + courant**2)/2)
            
    def soft_reflection(self, uj0i_1, uj0i_2):
        self.uj1=(4*uj0i_1-uj0i_2)/3
        
    def non_transmission(self):
        self.uj1=0   
      
    #This is for the mesh central nodes.
    def central(self, dt, square_velocity, dx, uj0i, uj01, uj0i_1,v0):
        self.uj1=(((dt**2*square_velocity)/(2*dx**2))*(uj01-2*uj0i+uj0i_1))\
                +uj0i-(dt*v0)
        
    def central_future(self, dt,dx ,square_velocity, uj01, uj0i, uj0i_1, uj_1i):
        self.uj1=(((dt**2*square_velocity)/(dx**2))*(uj01-2*uj0i+uj0i_1))\
                +2*uj0i-uj_1i         
            
    def trans_interface(self, young_modulus_1, young_modulus1, uj01, uj0i_1,\
                        uj02, uj0i_2):
        self.uj1=(4*((young_modulus1*uj01)+(young_modulus_1*uj0i_1))-\
                    ((young_modulus1*uj02)+(young_modulus_1*uj0i_2)))/\
                    (3*(young_modulus_1+young_modulus1))
    
    def five_point_stencil(self, square_velocity, dx, dt, uj02, uj01, uj0i_1,\
                           uj0i_2, uj0i, uj_1i):
        self.uj1=square_velocity*dt**2*(-uj02+16*uj01-30*uj0i+16*uj0i_1-uj0i_2)\
                            /(12*dx**2)+(2*uj0i)-uj_1i

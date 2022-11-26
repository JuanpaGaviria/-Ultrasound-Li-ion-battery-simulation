import numpy as np
from src.explicit.statusbar.statusbar import status_bar

def fm(nodes, nsteps, dx, dt, materials_summary, courant_material, indexes,\
    dimensionless_position, x, _e_modulus_dict, battery_map):

    sb = status_bar(nsteps)
    materials_number = len(indexes)

    uj1=np.zeros(nodes)
    uj2=np.zeros(nodes)
    uj0=np.zeros(nodes)
    uj_1=np.zeros(nodes)
    uj_2=np.zeros(nodes)

    H=np.zeros((nodes,nsteps+1))

    v0=0

    for j in range(nsteps):

        if j==0: #first step in a first moment
            count=0#this refers to the position in terms of dimensionless length
            n=0#This refers to the node
            interphase_count = 0
            #Left boundary condition.
            if count==0:
                courant=courant_material[count]
                uj0i=uj0[n]
                uj01=uj0[n+1]
                uj02=uj0[n+2]
                materials_summary[count].in_put(j)
                # materials_summary[count].leftbc_open(courant, uj0i, uj01, uj02)
                uj1[count]=materials_summary[count].uj1
                H[:,j+1]=uj1  #save history

                n=n+1
                count=count+dx

                # print(count,round(dx,3))
            if count > 0 and n<nodes:
                for b in range(materials_number):
                    #method for central uj1

                    while count < dimensionless_position[b] and n < nodes-1:

                        #variables
                        square_velocity=materials_summary[b].square_velocity
                        # print(materials_summary[b].square_velocity)
                        uj0i=uj0[n]
                        uj01=uj0[n+1]
                        uj0i_1=uj0[n-1]
                        materials_summary[b].central(dt, square_velocity, dx, uj0i,\
                                                    uj01, uj0i_1,v0)
                        uj1[n]=materials_summary[b].uj1
                        H[:,j+1]=uj1  #save history

                        n=n+1
                        count=count+dx
                        #Interface
                        if count > dimensionless_position[b] and \
                            count < dimensionless_position[b]+dx:
                            #variables
                            # young_modulus_1=materials_summary[b].young_modulus
                            # young_modulus1=materials_summary[b+1].young_modulus
                            material_1 = battery_map[interphase_count]
                            young_modulus_1=_e_modulus_dict[material_1]
                            material_2 = battery_map[interphase_count+1]
                            young_modulus1=_e_modulus_dict[material_2]
                            uj01=uj0[n+1]
                            uj0i_1=uj0[n-1]
                            uj02=uj0[n+2]
                            uj0i_2=uj0[n-2]

                            materials_summary[b].trans_interface(young_modulus_1,young_modulus1, uj01, uj0i_1, uj02,\
                                                    uj0i_2)
                            uj1[n]=materials_summary[b].uj1
                            H[:,j+1]=uj1  #save history

                            count=count+dx
                            n=n+1
                            interphase_count += 1

                        #right boundary condition
                    if b == materials_number-1:
                        #variables
                        uj0i=uj0[n]
                        courant=courant_material[b]
                        uj0i_1=uj0[n-1]
                        uj0i_2=uj0[n-2]
                        # materials_summary[b].rightbc_open(uj0i, courant, uj0i_1, uj0i_2)
                        materials_summary[b].non_transmission()
                        uj1[n]=materials_summary[b].uj1
                        H[:,j+1]=uj1  #save history

        if j>0:
            count=0#this refers to the position in terms of dimensionless length
            n=0#This refers to the node
            #Left boundary condition. 
            if count==0:
                uj0i=uj0[n]
                courant=courant_material[n]
                uj01=uj0[n+1]
                uj02=uj0[n+2]
                # materials_summary[count].leftbc(courant, uj0i, uj01, uj02)
                # materials_summary[count].non_transmission()
                if j<17:
                    materials_summary[count].in_put(j)
                elif j==17 or (j>17 and j<60): 
                        #Open boundary:
                        materials_summary[count].leftbc_open(courant, uj0i, uj01, uj02)
                        #Non transmission boundary
                    # materials_summary[count].non_transmission()
                elif j>59:
                    materials_summary[count].leftbc_soft(uj01, uj02)
                uj1[count]=materials_summary[count].uj1
                H[:,j+1]=uj1  #save history

                count=count+dx
                n=n+1

            if count>0 and n < nodes-1:

                for b in range(materials_number):
                    #method for central uj1
                    while count < dimensionless_position[b] and n < nodes-1:
                        if n<2 or n<nodes-1:
                            #variables
                            square_velocity=materials_summary[b].square_velocity
                            uj01=uj0[n+1]
                            uj0i=uj0[n]
                            uj0i_1=uj0[n-1]
                            uj0i_2=uj0[n-2]
                            uj_1i=uj_1[n]

                            materials_summary[b].central_future(dt,dx ,\
                                            square_velocity, uj01, uj0i, uj0i_1, uj_1i)

                            uj1[n]=materials_summary[b].uj1
                            H[:,j+1]=uj1  #save history

                            # count=count+dx
                            # n=n+1
                            # print(j)

                        if n>1 and n<nodes-2:
                            square_velocity=materials_summary[b].square_velocity
                            uj01=uj0[n+1]
                            uj0i=uj0[n]
                            uj0i_1=uj0[n-1]
                            uj0i_2=uj0[n-2]
                            uj_1i=uj_1[n]
                            uj02=uj0[n+2]
                            # materials_summary[b].central_future(dt,dx ,\
                                            # square_velocity, uj01, uj0i, uj0i_1, uj_1i)
                            materials_summary[b].five_point_stencil(square_velocity,\
                                                dx, dt, uj02, uj01, uj0i_1, uj0i_2, uj0i, uj_1i)

                            uj1[n]=materials_summary[b].uj1
                            H[:,j+1]=uj1  #save history

                        count=count+dx
                        n=n+1
                        # print(j,n, count)

                        if count > dimensionless_position[b] and \
                            count < dimensionless_position[b]+dx and n < nodes-2:
                            #variables
                            material_1 = battery_map[interphase_count]
                            young_modulus_1=_e_modulus_dict[material_1]
                            material_2 = battery_map[interphase_count+1]
                            young_modulus1=_e_modulus_dict[material_2]
                            uj01=uj0[n+1]
                            uj0i_1=uj0[n-1]
                            uj02=uj0[n+2]
                            uj0i_2=uj0[n-2]
                            materials_summary[b].trans_interface(young_modulus_1,young_modulus1, uj01, uj0i_1, uj02, uj0i_2)
                            uj1[n]=materials_summary[b].uj1
                            H[:,j+1]=uj1  #save history

                            count=count+dx
                            n=n+1

                    if b == materials_number-1:
                        #variables
                        uj0i=uj0[n]
                        courant=courant_material[b]
                        uj0i_1=uj0[n-1]
                        uj0i_2=uj0[n-2]
                        # materials_summary[b].rightbc_open(uj0i, courant, uj0i_1, uj0i_2)
                        # materials_summary[b].soft_reflection(uj0i_1, uj0i_2)
                        materials_summary[b].non_transmission()
                        uj1[n]=materials_summary[b].uj1
                        H[:,j+1]=uj1  #save history

        uj_2[:]=uj_1
        uj_1[:]=uj0  #time update
        uj0[:]=uj1

        sb.update(j+1)

    return H

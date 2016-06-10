# -*- coding: utf-8 -*-
"""
Created on Wed Jun 08 11:48:46 2016

@author: lenovo
"""

#This is the 5th computationphysics homework
#Filename: the 5th homework
#---------------start---------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#--------------------------------------------------------------------
tao=1.0
N_A=[100.0]
N_B=[0.0]
t_list=[0.0]
dt=0.01
# constants that will be usd below
#----------------------------------------------------------------------

max_t=input('Please input your time parameter then press <enter>: ')
n=int(max_t/dt)

for i in range(n+1):
    a=N_A[-1]+(N_B[-1]/tao-N_A[-1]/tao)*dt
    b=N_B[-1]+(N_A[-1]/tao-N_B[-1]/tao)*dt
    c=(i+1)*dt
    N_A.append(a)
    N_B.append(b)
    t_list.append(c)
#above calculating the number of two types of nuclei
#-----------------------------------------------------------------------

plt.figure(figsize=(8,4))
plt.plot(t_list,N_A,label='NA(t)',color='red',linewidth=1)
plt.plot(t_list,N_B,'b--',label='NB(t)')
plt.xlabel('time(s)')
plt.ylabel('number')
plt.title('exercises 1.5 figure')
plt.xlim(0,max_t)
plt.legend()
plt.show()
# above plotting
#-------------------------------------------------------------------------

while abs(N_A[-1]-N_B[-1])>0.000001:
    max_t=max_t+1
    n=int(max_t/dt)

    for i in range(n+1):
        a=N_A[-1]+(N_B[-1]/tao-N_A[-1]/tao)*dt
        b=N_B[-1]+(N_A[-1]/tao-N_B[-1]/tao)*dt
        N_A.append(a)
        N_B.append(b)
else:
    print'steady number=',round(N_A[-1])
# above getting the number which in steady state    




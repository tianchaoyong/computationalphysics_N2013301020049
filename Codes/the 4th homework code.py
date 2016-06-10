# -*- coding: utf-8 -*-

#Filename:the 4th homework

import matplotlib.pyplot as plt
#--------------------------------------------------------------
a=10
b=1  # give constants
#--------------------------------------------------------------

dt=0.01
max_t=input('please give the times scale then press the key <enter> to start: ')
n=int(max_t/dt)

#--------------------------------------------------------------------------------
v_list=[0] # a list of storing velocity
t_list=[0] # a list of storing time


for i in range(n+1):
    v_i=v_list[-1]+(a-b*v_list[-1])*dt
    t_i=(i+1)*dt
    v_list.append(v_i)
    t_list.append(t_i)
# above getting the velocity and the time corresponding to velocity
#-----------------------------------------------------------------------------
    
plt.figure(figsize=(8,4))
plt.plot(t_list,v_list,color="red")
plt.xlabel("time(s)")
plt.ylabel("velocity")
plt.xlim(0,max_t)
plt.title('Exercises1.5-friction problem')
plt.legend()
plt.show()
#---------above plotting--------------------------------------------------------

print 'v(max_t)=',v_list[-1],'m/s'
# this is used to output the final velocity corresponding to inputed parametr
# -*- coding: utf-8 -*-

# filename: all

#----------------------------------------------------------------------------------
x1=[0]
x2=[0]      
x3=[0] 
x4=[10]         # axis x coordinate
y1=[0.001]
y2=[0.001]  
y3=[0.001]
y4=[0.001]     # axis y coordinate
v_x1=[25]
v_x2=[25]    
v_x3=[25]
v_x4=[25]      # axis x velocity
v_y1=[43.3]
v_y2=[43.3]  
v_y3=[43.3]
v_y4=[43.3]    # axis y velocity
dt=0.01
#----------------------------------------------------------------------------

while y1[-1]>0:
    vx1=v_x1[-1]
    vy1=v_y1[-1]-9.8*dt
    cx1=x1[-1]+v_x1[-1]*dt   
    cy1=y1[-1]+v_y1[-1]*dt
    x1.append(cx1)
    y1.append(cy1)
    v_x1.append(vx1)
    v_y1.append(vy1)   # body 1
while y2[-1]>0:
    vx2=v_x2[-1]-0.0042*50*v_x2[-1]*dt
    vy2=v_y2[-1]-9.8*dt-0.0042*50*v_y2[-1]*dt
    cx2=x2[-1]+v_x2[-1]*dt   
    cy2=y2[-1]+v_y2[-1]*dt
    x2.append(cx2)
    y2.append(cy2)
    v_x2.append(vx2)
    v_y2.append(vy2)   # body 2
while y3[-1]>0:
    vx3=v_x3[-1]-0.25*v_y3[-1]*dt
    vy3=v_y3[-1]-9.8*dt+0.25*v_x3[-1]*dt
    cx3=x3[-1]+v_x3[-1]*dt   
    cy3=y3[-1]+v_y3[-1]*dt
    x3.append(cx3)
    y3.append(cy3)
    v_x3.append(vx3)
    v_y3.append(vy3)    #body 3        
while y4[-1]>0:
    vx4=v_x4[-1]-0.0042*50*v_x4[-1]*dt-0.25*v_y4[-1]*dt
    vy4=v_y4[-1]-9.8*dt-0.0042*50*v_y4[-1]*dt+0.25*v_x4[-1]*dt
    cx4=x4[-1]+v_x4[-1]*dt   
    cy4=y4[-1]+v_y4[-1]*dt
    x4.append(cx4)
    y4.append(cy4)
    v_x4.append(vx4)
    v_y4.append(vy4)    #body 4    
#------------------------------------------------------------------------------------
    
if max(y1)>=max(y2):
    if max(y1)>=max(y3):
        if max(y1)>=max(y4):
            a=max(y1)
        else:
            a=max(y4)
    else:
        if max(y3)>=max(y4):
            a=max(y3)
        else:
            a=max(y4)
else:
    if max(y2)>=max(y3):
        if max(y2)>=max(y4):
            a=max(y2)
        else:
            a=max(y4)
    else:
        if max(y3)>=max(y4):
            a=max(y3)
        else:
            a=max(y4)        # to find the highest coordate
#=================================================================================
        
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8,4))
plt.plot(x1,y1,label='nothing',color='red',linewidth=1.5)
plt.plot(x2,y2,'b--',label='resistance')
plt.plot(x3,y3,color='black',label='spinning')
plt.plot(x4,y4,color='blue',label='all')
plt.xlabel('level x')
plt.ylabel('height y')
plt.title('all')
plt.ylim(0,a+10)
plt.legend()
plt.show()


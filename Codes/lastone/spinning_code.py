# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 16:21:49 2016

@author: lenovo
"""
# filename: spinning
x1=[0]
x2=[0]      
x3=[0]         # axis x coordinate
y1=[0.001]
y2=[0.001]  
y3=[0.001]     # axis y coordinate
v_x1=[25]
v_x2=[25]    
v_x3=[25]      # axis x velocity
v_y1=[43.3]
v_y2=[43.3]  
v_y3=[43.3]    # axis y velocity
dt=0.01


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
    
if max(y1)>=max(y2):
    if max(y1)>=max(y3):
        a=max(y1)
    else:
        a=max(y3)
else:
    if max(y2)>=max(y3):
        a=max(y2)
    else:
        a=max(y3)       # find the highest coordate
    
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8,4))
plt.plot(x1,y1,label='nothing',color='red',linewidth=1.5)
plt.plot(x2,y2,'b--',label='resistance')
plt.plot(x3,y3,color='black',label='spinning')
plt.xlabel('level x')
plt.ylabel('height y')
plt.title('spinning')
plt.ylim(0,a+10)
plt.legend()
plt.show()


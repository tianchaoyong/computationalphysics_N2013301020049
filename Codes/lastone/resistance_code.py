# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 23:19:10 2016

@author: lenovo
"""
# filename: resistance

x1=[0]
x2=[0]      # axis x coordinate
y1=[0.001]
y2=[0.001]  # axis y coordinate
v_x1=[25]
v_x2=[25]    # axis x velocity
v_y1=[43.3]
v_y2=[43.3]   # axis y velocity
dt=0.1


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
    
if max(y1)>=max(y2):
    a=max(y1)
else:
    a=max(y2)
    
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8,4))
plt.plot(x1,y1,label='no resistance',color='red',linewidth=1.5)
plt.plot(x2,y2,'b--',label='with resistance')
plt.xlabel('level x')
plt.ylabel('height y')
plt.title('resistance')
plt.ylim(0,a+10)
plt.legend()
plt.show()
    
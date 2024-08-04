# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:19:26 2024

@author: Ethan Hu
"""

import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
m=1
sm=0
snellRatio = 1/1.33
ax = plt.gca()
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
if m < sm:
    rayA = [-1, -m] #Vector representation of incident ray, make sure it's above the surface slope
else:
    rayA = [1, m]
rayB = [-sm, 1] #Vector representation of line perpendicular to slope
sinth = -np.cross(rayA,rayB)/(np.linalg.norm(rayA)*np.linalg.norm(rayB)) #sin of angle between these two lines

reverseRayB = np.array(rayB)*-1 #Reversed rayB
theta = np.arcsin(snellRatio*sinth)
R = np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])
rayC = R @ reverseRayB

plt.plot([0,1],[0,sm],'y-')
plt.plot([0,rayA[0]],[0,rayA[1]],'r-')
plt.plot([0,rayB[0]],[0,rayB[1]],'g-')
plt.plot([0,reverseRayB[0]],[0,reverseRayB[1]],'b-')
plt.plot([0,rayC[0]],[0,rayC[1]],'o-')
plt.text(-3, -2, 'incident angle: '+str(np.arcsin(sinth))+', exit angle: '+str(theta))
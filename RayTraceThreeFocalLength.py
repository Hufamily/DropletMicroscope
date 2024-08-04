# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 17:05:59 2024

@author: Ethan Hu
"""

import numpy as np
import matplotlib.pyplot as plt

M = 1
a=47.629573102085615

b=1654.948130028152
c=45.51591722970714
d=1963.0079226977857
a=a*M
b=b*M
c=c*M
d=d*M


Endpoints = np.array([1620,1690])*M

def ellipse(x, a, b, c, d):
    return -a/c*np.sqrt(c**2-((x-b))**2)+d

def dellipse(x,a,b,c,d):
    y=ellipse(x,a,b,c,d)
    return (-a**2)/(c**2)*(x-b)/(y-d)

def line(x,m,p,q):
    return m*(x-p)+q

def refract(iM, sM, n1, n2):
    snellRatio = n1/n2
    if iM < sM:
        rayA = [-1, -iM] #Vector representation of incident ray. Make sure slope is positive, if negative, manipulate -1
    else:
        rayA = [1, iM]
    rayB = [-sM, 1] #Vector representation of line perpendicular to slope
    sinth = -np.cross(rayA,rayB)/(np.linalg.norm(rayA)*np.linalg.norm(rayB)) #sin of angle between these two lines
    if np.abs(sinth*snellRatio) > 1:
        print('Total Internal Reflection')
        return 0
    reverseRayB = np.array(rayB)*-1 #Reversed rayB
    theta = np.arcsin(snellRatio*sinth)
    R = np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])
    rayC = R @ reverseRayB
    rM = rayC[1]/rayC[0]
    return rM

h = ellipse(Endpoints[0],a,b,c,d)
t = 64*M #Thickness of glass
my = (-199*t+h)

fig, ax = plt.subplots()

xj = b
#plt.yscale('log')
#plt.plot(xj,my,'bo')
ax.plot(Endpoints,[h,h],'y-')
ax.plot(Endpoints,[h+t,h+t],'y-')

xf = np.arange(int(min(Endpoints)+1),int(max(Endpoints)),0.01*M)
ax.plot(xf,ellipse(xf,a,b,c,d),'y-')
xf = np.arange(int(min(Endpoints)+1),int(max(Endpoints)),0.5*M)
for x in xf:
    m = 10000000000000000000000.0
    xp = x
    yp = my
    
    #First intersection
    k=1/(2*(c**2*m**2+a**2))
    s1 = 2*b*a**2+2*c**2*d*m+2*c**2*m**2*xp-2*c**2*m*yp
    s2 = np.sqrt((-2*a**2*b-2*c**2*d*m-2*c**2*m**2*xp+2*c**2*m*yp)**2-4*(a**2+c**2*m**2)*(a**2*b**2-a**2*c**2+c**2*d**2+2*c**2*d*m*xp-2*c**2*d*yp+c**2*m**2*xp**2-2*c**2*m*xp*yp+c**2*yp**2))
    if m>0:
        xo = k*(s1-s2)
    elif m<0:
        xo = k*(s1+s2)
    y = ellipse(xo, a,b,c,d)
    xp = xo
    yp = y
    ax.plot([xp,xo],[my,y], 'b-')
    n1 = 1
    n2 = 1.33
    if xo < max(Endpoints) and xo > min(Endpoints):
        print(m)
        m3 = dellipse(xo,a,b,c,d)
        print(m3)
        """
        m = 1/np.tan(np.arcsin(n1/n2*np.sin(np.arctan(1/m))))
        m = np.tan(np.arctan(m)+np.arctan(m3))
        """
        m = refract(m, m3, n1, n2)
        print(m)
        print('-')
    if m == 0:
        continue
    xoa = xo
    yb = y

    #Second intersection
    y=h
    xo = (y-yp+xp*m)/m
    ax.plot([xo, xoa],[y, yb],'b-')
    n1=1.33
    n2=1.57
    #m = 1/np.tan(np.arcsin(n1/n2*np.sin(np.arctan(1/m))))
    m = refract(m, 0, n1, n2)
    if m == 0:
        continue
    xp = xo
    yp = y

    xoa = xo
    yb = y
    
    #Third intersection
    y=h+t
    xo=(y-yp+xp*m)/m
    ax.plot([xo,xoa],[y,yb],'b-')
    n1 = 1.57
    n2 = 1
    #m = 1/np.tan(np.arcsin(n1/n2*np.sin(np.arctan(1/m))))
    m = refract(m, 0, n1, n2)
    if m == 0:
        continue
    xp = xo
    yp = y

    ax.plot(xf, line(xf,m,xp,yp),'m-')
    
ax.set_ylim(1800, 2200)

# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:16:55 2024

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
    return (2*a*(x-b))/(c*np.sqrt(c**2-(x-b)**2))

def line(x,m,p,q):
    return m*(x-p)+q

h = ellipse(Endpoints[0],a,b,c,d)
t = 64*M #Thickness of glass
my = (201*t+h)

plt.figure()

xj = b
#plt.yscale('log')
plt.plot(xj,my,'bo')
plt.plot(Endpoints,[h,h],'y-')
plt.plot(Endpoints,[h+t,h+t],'y-')

xf = np.arange(int(min(Endpoints)+1),int(max(Endpoints)),0.1*M)
plt.plot(xf,ellipse(xf,a,b,c,d),'y-')

for x in xf:
    m = -(my-h)/(x-xj)
    xp = xj
    yp = my
    
    #First intersection
    y=h+t
    xo=(y-yp+xp*m)/m
    plt.plot([xj,xo],[my,y], 'b-')
    n1 = 1
    n2 = 1.57
    m = 1/np.tan(np.arcsin(n1/n2*np.sin(np.arctan(1/m))))
    xp = xo
    yp = y
    
    xoa = xo
    yb = y
    
    #Second intersection
    y=h
    xo = (y-yp+xp*m)/m
    plt.plot([xo, xoa],[y, yb],'b-')
    n1=1.57
    n2=1.33
    m = 1/np.tan(np.arcsin(n1/n2*np.sin(np.arctan(1/m))))
    xp = xo
    yp = y

    xoa = xo
    yb = y
    
    #Third intersection
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
    plt.plot([xo,xoa],[y,yb],'b-')
    n1 = 1.33
    n2 = 1
    if xo < max(Endpoints) and xo > min(Endpoints):
        m3 = dellipse(xo,a,b,c,d)
        o = n1/n2*np.sin(1/np.arctan(m)+1/np.arctan(-1/m3))
        if o>1:
            o=o-2
        elif o<-1:
            o=o+2
        m=1/np.tan(1/np.arctan(-1/m3)-np.arcsin(o))

    plt.plot(xf, line(xf,m,xp,yp),'m-')

# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:05:20 2024

@author: Ethan Hu
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op
M = 1
a=21.98186321
b=195.02454635
c=21.98186321
d=258.73743641
a=a*M
b=b*M
c=c*M
d=d*M


Endpoints = np.array([174.96580789907276, 215.06403770408016])*M

pDiameter = max(Endpoints)-min(Endpoints)
if Endpoints[0] < b-c:
    Endpoints[0] = b-c+1
if Endpoints[1] > b+c:
    Endpoints[1] = b+c
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
        #print('Total Internal Reflection')
        return 0
    reverseRayB = np.array(rayB)*-1 #Reversed rayB
    theta = np.arcsin(snellRatio*sinth)
    R = np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])
    rayC = R @ reverseRayB
    rM = rayC[1]/rayC[0]
    return rM
tIR = []
def irefract(sM, n1, n2, x):
    snellRatio = n1/n2
    rayA = [0,1]
    rayB = [-sM, 1] #Vector representation of line perpendicular to slope
    sinth = -np.cross(rayA,rayB)/(np.linalg.norm(rayA)*np.linalg.norm(rayB)) #sin of angle between these two lines
    if np.abs(sinth*snellRatio) > 1:
        #print('Total Internal Reflection at '+str(x))
        tIR.append(x)
        return 0
    reverseRayB = np.array(rayB)*-1 #Reversed rayB
    theta = np.arcsin(snellRatio*sinth)
    R = np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])
    rayC = R @ reverseRayB
    rM = rayC[1]/rayC[0]
    return rM

h = ellipse(Endpoints[0],a,b,c,d)
t = 64*M #Thickness of glass
my = (d+h)

fig, ax = plt.subplots()
plt.xlabel('x (px)')
plt.ylabel('y (px)')
xj = b
#plt.yscale('log')
#plt.plot(xj,my,'bo')
ax.plot(Endpoints,[h,h],'y-')
ax.plot(Endpoints,[h+t,h+t],'y-')

xf = np.arange(int(min(Endpoints)+1),int(max(Endpoints)),0.005*M)

ax.plot(xf,ellipse(xf,a,b,c,d),'y-')

xf = np.arange(0, b-Endpoints[0], 0.1)

totalInternalReflection = []
focalLengths = []
"""
x1 =211.5-2
x2 =211.5+2
y1 =244.25-2
y2 =244.25+2

abracadabra = ax.inset_axes([0.68, 0.6, 0.3, 0.3], xlim=(x1, x2), ylim=(y1, y2))

xa = 195 -7
xb = 195 +7
ya = 218 -8
yb = 218 +8
alakazam = ax.inset_axes([0.02, 0.4, 0.3, 0.3], xlim=(xa, xb), ylim=(ya, yb))
"""
for x in xf:
    #Right Side
    xo = x+b
    y = ellipse(xo, a,b,c,d)
    xp = xo
    yp = y
    ax.plot([xp,xo],[my,y], 'b-')
    #abracadabra.plot([xp,xo],[my,y], 'b-')
    #alakazam.plot([xp,xo],[my,y], 'b-')
    n1 = 1.33
    n2 = 1
    if xo < max(Endpoints) and xo > min(Endpoints):
        m3 = dellipse(xo,a,b,c,d)
        #print(m3)
        m = irefract(m3, n1, n2, xo)
        #print(m)
        #print('-')
        if m != 0:
            ax.plot([xp,(h-d-yp)/m+xp],[yp,h-d])
            #abracadabra.plot([xp,(h-d-yp)/m+xp],[yp,h-d])
            #alakazam.plot([xp,(h-d-yp)/m+xp],[yp,h-d])
    else:
        m=0
        ax.plot([xp,xp],[yp,h-d])
        #abracadabra.plot([xp,xp],[yp,h-d])
        #alakazam.plot([xp,xp],[yp,h-d])
    
    m1 = m
    x1 = xp
    y1 = yp
    
    #Left Side
    xo = b-x
    y = ellipse(xo, a,b,c,d)
    xp = xo
    yp = y
    ax.plot([xp,xo],[my,y], 'b-')
    #abracadabra.plot([xp,xo],[my,y], 'b-')
    #alakazam.plot([xp,xo],[my,y], 'b-')
    n1 = 1.33
    n2 = 1
    if xo < max(Endpoints) and xo > min(Endpoints):
        m3 = dellipse(xo,a,b,c,d)
        #print(m3)
        m = irefract(m3, n1, n2, xo)
        #print(m)
        #print('-')
        if m != 0:
            ax.plot([xp,(h-d-yp)/m+xp],[yp,h-d])
            #abracadabra.plot([xp,(h-d-yp)/m+xp],[yp,h-d])
            #alakazam.plot([xp,(h-d-yp)/m+xp],[yp,h-d])
    else:
        m=0
        ax.plot([xp,xp],[yp,h-d])
        #abracadabra.plot([xp,xp],[yp,h-d])
        #alakazam.plot([xp,xp],[yp,h-d])

    m2 = m
    x2 = xp
    y2 = yp
    
    #Find Intersect
    
    #y-yo = m(x-xo)
    #(y-yo)/m + xo = x
    #(y - y1)/m1 + x1 = (y - y2)/m2 + x2
    #m2*y - m2*y1 + m1*m2*x1 = m1*y - m1*y2 + m1*m2*x2
    if m2 == 0 or m1 == 0 or x1 < Endpoints[0] or x1 > Endpoints[1] or x2 < Endpoints[0] or x2 > Endpoints[1]:
        continue
    else:
        y = (m2*y1-m1*m2*x1-m1*y2+m1*m2*x2)/(m2-m1)
    focalLengths.append(y)
#ax.set_ylim(1800, 2200)
focalLengths = focalLengths[1:]
focalLengths = focalLengths - h
focalLengths = focalLengths/(pDiameter)
print(min(focalLengths))
print(max(focalLengths))
tIR = tIR[1:]
print((max(tIR)-min(tIR))/pDiameter)
ax.set_xlim(96.725701978632106, 294.7747946786321)
ax.set_ylim(100,300)
#ax.indicate_inset_zoom(abracadabra, edgecolor="black")
#ax.indicate_inset_zoom(alakazam, edgecolor="black")
"""
#MagnificationDataReader
plt.close('all')
data = np.genfromtxt('Result1.csv', delimiter = ',')

data = data[1:]

num, area, x, y, bx, by, width, height = data.T
Mx = width/3
My = height/1
xo = 87.3
yo = 87.5
r = 63.6
#Clears out non droplet data
for i in num:
    if (x[np.where(num == i)]-xo)**2+(y[np.where(num == i)]-yo)**2 > 73.6**2:
        area = np.delete(area, np.where(num == i))
        x = np.delete(x, np.where(num == i))
        y = np.delete(y, np.where(num == i))
        bx = np.delete(bx, np.where(num == i))
        by = np.delete(by, np.where(num == i))
        width = np.delete(width, np.where(num == i))
        height = np.delete(height, np.where(num == i))
        Mx = np.delete(Mx, np.where(num==i))
        My = np.delete(My, np.where(num==i))
        num = np.delete(num, np.where(num == i))
x2 = x
y2 = y
Mx2 = Mx
My2 = My
num2 = num
for i in num2:
    if (x2[np.where(num2 == i)]-xo)**2+(y2[np.where(num2 == i)]-yo)**2 > r**2:
        x2 = np.delete(x2, np.where(num2 == i))
        y2 = np.delete(y2, np.where(num2 == i))
        Mx2 = np.delete(Mx2, np.where(num2==i))
        My2 = np.delete(My2, np.where(num2==i))
        num2 = np.delete(num2, np.where(num2 == i))
plt.figure()
plt.title('Magnification vs Distance from Center')
Magnification = Mx*My
Magnification2 = Mx2*My2
xo = 86.5
yo = 88.3
Distance = np.sqrt((x-xo)**2+(y-yo)**2)
Distance2 = np.sqrt((x2-xo)**2+(y2-yo)**2)
di = 0.007865
pxConversion = 82.5/(0.002384671479)
d = np.arange(0,80, 0.1)
#plt.plot(d,np.absolute(-0.008635372628/(0.008635372628-np.sqrt(do**2+(d/pxConversion)**2))), 'k-', label = 'Max Predicted Magnification')
#plt.plot(d,np.absolute(-0.002888187968/(0.002888187968-np.sqrt(do**2+(d/pxConversion)**2))), 'y-', label = 'Min Predicted Magnification')
for i in np.arange(len(focalLengths)):
    #plt.plot(d,np.absolute((focalLengths[i-1]*-0.001*4.51-np.sqrt(di**2+(d/pxConversion)**2))/(0.001*focalLengths[i-1]*4.51)), 'y-')
    plt.plot(d,np.absolute((focalLengths[i-1]*0.001*4.51))/(-0.001*focalLengths[i-1]*4.51-np.sqrt((0.00403)**2+0*(d/pxConversion)**2)), 'k-')
    #label = str(i)+' Predicted Magnification'

plt.plot(Distance, Magnification, 'ro', label = 'Data Points within Droplet')
plt.plot(Distance2, Magnification2, 'yo', label = 'Data Points accurately detected by ImageJ')
def func(x, a, b,c,d):
    return a*x**4+b*x**3+c*x**2+d*x+1
popt,pcov = op.curve_fit(func, Distance2,Magnification2, p0 = (1,1,1,1), sigma = None, absolute_sigma = False, method ='lm')
#popt, pcov = np.polyfit(Distance,Magnification,deg=4,cov=True)
err = np.sqrt(np.diag(pcov))
def func2(x, b,c,d):
    return b*x**3+c*x**2+d*x+1
popt2,pcov2 = op.curve_fit(func2, Distance2,Magnification2, p0 = (1,1,1), sigma = None, absolute_sigma = False, method ='lm')
err2 = np.sqrt(np.diag(pcov2))
#quad = np.poly1d(popt)
#a,b,c,d,e = np.round(popt,4)
a,b,c,d = np.round(popt,4)
a = np.round(popt[0], 9)
b2, c2, d2 = np.round(popt2, 4)
#s = 'Mx: '+str(a)+'$x^4$+'+str(b)+'$x^3+$'+str(c)+'$x^2+$'+str(d)+'$x+$'+str(e)
s = 'Mx: '+str(a)+'$x^4$+'+str(b)+'$x^3+$'+str(c)+'$x^2+$'+str(d)+'$x$+1'
s2 = 'Mx: '+str(b2)+'$x^3+$'+str(c2)+'$x^2+$'+str(d2)+'$x$+1'
t = np.arange(0, 80, 0.1)
plt.plot(t,func(t, *popt),'b-', label = s)
plt.plot(t,func2(t, *popt2), 'g-', label = s2)


plt.legend()
plt.ylabel('Magnification')
plt.xlabel('Distance (px)')
plt.yscale('log')
"""

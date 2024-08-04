# -*- coding: utf-8 -*-
"""
Created on Wed May  1 09:18:42 2024

@author: Ethan Hu
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import scipy.optimize as op
plt.close('all')
data = np.genfromtxt('Result1.csv', delimiter = ',')

data = data[1:]

num, area, x, y, bx, by, width, height = data.T
#1920 px * 1080 px
#29.4 cm * 16.6 cm
#Pixel Dimension
#0.015cm * 0.015cm
#In x direction, pixel should be 3 units
#In y direction, pixel should be 1 unit
#Mx = width/3
#My = height

Mx = width/3
My = height/1
xo = 87.3
yo = 87.5
r = 63.6
#Clears out non droplet data
for i in num:
    if (x[np.where(num == i)]-xo)**2+(y[np.where(num == i)]-yo)**2 > r**2:
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
        


#Displays the boxes made
fig, ax = plt.subplots()

im = plt.imread('Demo.TIF')
implot = plt.imshow(im)
plt.plot(x,y,'bo')
for j in num:
    i = np.where(num==j)
    #plt.plot([bx[i]-width/2, bx[i]-width/2,bx[i]+width/2, bx[i]+width/2],[by[i]-height/2, by[i]+height/2, by[i]-height/2, by[i]+height/2],'r-')
    rect = Rectangle((bx[i],by[i]),width[i],height[i],linewidth=1,edgecolor='r',facecolor='r')
    ax.add_patch(rect)
"""
circ = Circle((xo,yo),r, color = 'b')
ax.add_patch(circ)
"""
ang = np.arange(0,2*np.pi, 0.1)
plt.plot(xo+r*np.cos(ang), yo+r*np.sin(ang),'g-')
plt.xlabel( 'x (px)')
plt.ylabel('y (px)')
plt.show()


plt.figure()
plt.title('Vertical vs Horizontal Magnification')
plt.plot(Mx, My, 'ro')
plt.xlabel('Horizontal Magnification')
plt.ylabel('Vertical Magnification')

"""
plt.figure()
plt.title('Horizontal and Vertical Magnification vs Position')

plt.xlabel('Position (px)')
plt.ylabel('Magnification')

plt.plot(y, My, 'bo',)

plt.plot(x,Mx, 'ro')

t = np.arange(5, 170)

popt, pcov = np.polyfit(y,My,deg=2,cov=True)
err = np.sqrt(np.diag(pcov))

quad = np.poly1d(popt)
a,b,c = np.round(popt,4)
s = 'My: '+str(a)+'$x^2$+'+str(b)+'$x+$'+str(c)
plt.plot(t,quad(t),'b-', label = s)

popt, pcov = np.polyfit(x,Mx,deg=2,cov=True)
err = np.sqrt(np.diag(pcov))

quad = np.poly1d(popt)
a,b,c, = np.round(popt,4)
s = 'Mx: '+str(a)+'$x^2$+'+str(b)+'$x+$'+str(c)
plt.plot(t,quad(t),'r-', label = s)
plt.legend()
"""
plt.figure()
plt.title('Magnification vs Distance from Center')
Magnification = Mx*My
xo = 86.5
yo = 88.3
Distance = np.sqrt((x-xo)**2+(y-yo)**2)
plt.plot(Distance, Magnification, 'ro')

def func(x, a, b,c,d):
    return a*x**4+b*x**3+c*x**2+d*x+1
popt,pcov = op.curve_fit(func, Distance,Magnification, p0 = (1,1,1,1), sigma = None, absolute_sigma = False, method ='lm')
#popt, pcov = np.polyfit(Distance,Magnification,deg=4,cov=True)
err = np.sqrt(np.diag(pcov))
def func2(x, b,c,d):
    return b*x**3+c*x**2+d*x+1
popt2,pcov2 = op.curve_fit(func2, Distance,Magnification, p0 = (1,1,1), sigma = None, absolute_sigma = False, method ='lm')
err2 = np.sqrt(np.diag(pcov2))
#quad = np.poly1d(popt)
#a,b,c,d,e = np.round(popt,4)
a,b,c,d = np.round(popt,4)
a = np.round(popt[0], 9)
b2, c2, d2 = np.round(popt2, 4)
#s = 'Mx: '+str(a)+'$x^4$+'+str(b)+'$x^3+$'+str(c)+'$x^2+$'+str(d)+'$x+$'+str(e)
s = 'Mx: '+str(a)+'$x^4$+'+str(b)+'$x^3+$'+str(c)+'$x^2+$'+str(d)+'$x$+1'
s2 = 'Mx: '+str(b2)+'$x^3+$'+str(c2)+'$x^2+$'+str(d2)+'$x$+1'
t = np.arange(0, r, 0.1)
plt.plot(t,func(t, *popt),'b-', label = s)
plt.plot(t,func2(t, *popt2), 'g-', label = s2)

di = 0.007865
dierr = 0.000056
pxConversion = 82.5/(0.002384671479)
d = np.arange(0,70)
plt.plot(d,np.absolute((-0.008635372628+np.sqrt(di**2+0*(d/pxConversion)**2))/(0.008635372628)), 'k-', label = 'Max Predicted Magnification')
plt.plot(d,np.absolute((-0.002888187968+np.sqrt(di**2+0*(d/pxConversion)**2))/(0.002888187968)), 'y-', label = 'Min Predicted Magnification')



plt.legend()
plt.ylabel('Magnification')
plt.xlabel('Distance (px)')
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 16:03:19 2024

@author: Ethan Hu
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 09:56:26 2024

@author: Ethan Hu
"""
import numpy as np
import matplotlib.pyplot as plt

my, mx = [300, 180]
dx_image = np.zeros([my,mx])




#Input stuff from DropCurve
a=50
b=90
c=50
d=100
Endpoints = np.array([60,120])
#Endpoints = np.array([40,140])

def ellipse(x, a, b, c, d):
    return -a/c*np.sqrt(c**2-((x-b))**2)+d

def dellipse(x,a,b,c,d):
    return (2*a*(x-b))/(c*np.sqrt(c**2-(x-b)**2))

h = ellipse(Endpoints[0],a,b,c,d)
t = 2 #Thickness of glass

xf = np.arange(int(min(Endpoints)+1),int(max(Endpoints)))
for x in xf:
    dx_image[int(ellipse(x,a,b,c,d))][x] = dellipse(x,a,b,c,d)

#plt.imshow(dx_image)

rays = np.zeros(dx_image.shape)
plt.figure()
for x in range(mx):
    xpos = []
    ypos = []
    add = True
    xo = x
    dxdy = 0
    passF = False
    passS = False
    if int(xo)>=mx or int(xo)<0:
        add = False
    for y in range(my):
        if int(xo)>=mx or int(xo)<0:
            add = False
        if add:
            if dx_image[y,int(xo)] == 0:
                if y >= h+t and not passS:
                    passS = True
                    rays[y,int(xo)]+=1
                    n1=1.5
                    n2=1
                    if t==0:
                        n1 = 1.33
                    dxdy = -np.tan(2*np.pi-np.arcsin(n1/n2*np.sin(np.arctan(dxdy)-np.arctan(dx_image[y,int(xo)])))-np.arctan(dx_image[y,int(xo)]))
                    xo = xo+dxdy
                elif y>=h and not passF:
                    passF = True
                    rays[y,int(xo)]+=1
                    n1=1.33
                    n2=1.5
                    dxdy = -np.tan(2*np.pi-np.arcsin(n1/n2*np.sin(np.arctan(dxdy)-np.arctan(dx_image[y,int(xo)])))-np.arctan(dx_image[y,int(xo)]))
                    xo = xo+dxdy
                else:
                    rays[y,int(xo)]+=1
                    xo = xo+dxdy
            else:
                rays[y,int(xo)]+=1
                n1=1
                n2=1.33
                #dxdy = np.tan(2*np.pi-n1/n2*(np.arctan(dxdy)-np.arctan(dx_image[y,int(xo)]))-np.arctan(dx_image[y,int(xo)]))
                dxdy = np.tan(2*np.pi-np.arcsin(n1/n2*np.sin(np.arctan(dxdy)-np.arctan(dx_image[y,int(xo)])))-np.arctan(dx_image[y,int(xo)]))
                xo = xo+dxdy
            xpos.append(xo)
            ypos.append(y)
        
    plt.plot(xpos,ypos,'b-')
plt.figure()
plt.imshow(rays, cmap='inferno')
plt.plot(xf, ellipse(xf,a,b,c,d),'b-')
plt.plot(Endpoints,[h,h],'g-')
plt.plot(Endpoints,[h+t,h+t],'g-')
#Find ratio of focal point to radius
y = np.where(rays==np.max(rays))[0][0]
x = np.where(rays==np.max(rays))[1][0]
y0,x0 = h,b
r = np.sqrt((y-y0)**2+(x-x0)**2)/(2*(x-Endpoints[0]))
plt.plot([x,x0],[y,y0],'y-')
#np.savetxt("out.csv", dx_image, delimiter=",")

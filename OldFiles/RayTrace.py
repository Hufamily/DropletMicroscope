# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 09:56:26 2024

@author: Ethan Hu
"""
import numpy as np
import matplotlib.pyplot as plt
path = 'Nov15.bmp'
import PIL.Image as image

im =image.open(path)
drop=np.array(im) #Converts data into array
#plt.imshow(drop) #plt is Python library that does matlab stuff
#drop = drop[:, 2600:3500]

red = drop[:,:,0] #As drop is a bit map, where [red, green, blue], can filter to only red by only having first index
#plt.figure()
#plt.imshow(red, cmap='gray')

green = drop[:,:,1]
#plt.figure()
#plt.imshow(green, cmap='gray')

blue = drop[:,:,2]
#plt.figure()
#plt.imshow(blue, cmap='gray')


grey = (drop[:,:,0] + drop[:,:,1] + drop[:,:,2])/3.0
#plt.figure()
#plt.imshow(grey, cmap='gray')
"""
grey[:1800,:] = 0
grey[2150:,:] = 0
"""
M=3 #Magnifying each value
my, mx = grey.shape
my = my-100
my = my*M
mx = mx*M
dx_image = np.zeros([my,mx])




#Input stuff from DropCurve
a=66534.93775326238
b=90.03284158782034
c=1735.4689829512108
d=66597.66728280198
a=a*M
b=b*M
c=c*M
d=d*M
Endpoints = np.array([43.4318181818182, 134.4545454545455])*M


def ellipse(x, a, b, c, d):
    return -a/c*np.sqrt(c**2-((x-b))**2)+d

def dellipse(x,a,b,c,d):
    return (2*a*(x-b))/(c*np.sqrt(c**2-(x-b)**2))

h = ellipse(Endpoints[0],a,b,c,d)
t = 0*45*M #Thickness of glass

plt.figure()

xf = np.arange(int(min(Endpoints)+1),int(max(Endpoints)))
for x in xf:
    dx_image[int(ellipse(x,a,b,c,d))][x] = dellipse(x,a,b,c,d)
    plt.plot(x,int(ellipse(x,a,b,c,d)),'ro')
xf = np.arange(int(min(Endpoints)+1),int(max(Endpoints)),1*M)
#plt.imshow(dx_image)

rays = np.zeros(dx_image.shape)
intersectsx = []
intersectsy = []



for x in xf:
    xpos = []
    ypos = []
    add = True
    xo = b
    dxdy = (x-b)/(my-h)
    passF = False
    passS = False
    if int(xo)>=mx or int(xo)<0:
        add = False
    for yi in np.arange(my):
        y=my-yi-1
        if int(xo)>=mx or int(xo)<0:
            add = False
        if add:
            if dx_image[y,int(xo)] == 0:
                if y == h+t and not passS:
                    passS = True
                    rays[y,int(xo)]+=1
                    n1=1.5
                    n2=1
                    dxdy = -np.tan(2*np.pi-np.arcsin(n1/n2*np.sin(np.arctan(dxdy)-np.arctan(dx_image[y,int(xo)])))-np.arctan(dx_image[y,int(xo)]))
                    xo = xo-dxdy
                    plt.plot(xo,y,'go')
                elif y==h and not passF:
                    passF = True
                    rays[y,int(xo)]+=1
                    n1=1.33
                    n2=1.5
                    dxdy = -np.tan(2*np.pi-np.arcsin(n1/n2*np.sin(np.arctan(dxdy)-np.arctan(dx_image[y,int(xo)])))-np.arctan(dx_image[y,int(xo)]))
                    xo = xo-dxdy
                    plt.plot(xo,y,'yo')
                elif xo == max(Endpoints) and xo>= min(Endpoints) and y <= ellipse(xo, a,b,c,d):
                    rays[y,int(xo)]+=1
                    n1=1
                    n2=1.33
                    #dxdy = np.tan(2*np.pi-n1/n2*(np.arctan(dxdy)-np.arctan(dx_image[y,int(xo)]))-np.arctan(dx_image[y,int(xo)]))
                    dxdy = np.tan(2*np.pi-np.arcsin(n1/n2*np.sin(np.arctan(dxdy)-np.arctan(dx_image[y,int(xo)])))-np.arctan(dx_image[y,int(xo)]))
                    xo = xo-dxdy
                    plt.plot(xo,y,'mo')
                else:
                    rays[y,int(xo)]+=1
                    xo = xo-dxdy
                    #plt.plot(int(xo),y, 'ro')
            else:
                rays[y,int(xo)]+=1
                n1=1
                n2=1.33
                #dxdy = np.tan(2*np.pi-n1/n2*(np.arctan(dxdy)-np.arctan(dx_image[y,int(xo)]))-np.arctan(dx_image[y,int(xo)]))
                dxdy = np.tan(2*np.pi-np.arcsin(n1/n2*np.sin(np.arctan(dxdy)-np.arctan(dx_image[y,int(xo)])))-np.arctan(dx_image[y,int(xo)]))
                xo = xo-dxdy
                print('hit:'+str(int(xo)))
            xpos.append(xo)
            ypos.append(y)
        
    plt.plot(xpos,ypos,'bo')
plt.plot(xf, ellipse(xf,a,b,c,d),'r-')
plt.figure()
plt.imshow(rays, cmap='inferno')
plt.plot(xf, ellipse(xf,a,b,c,d),'b-')
plt.plot(Endpoints,[h,h],'g-')
plt.plot(Endpoints,[h+t,h+t],'g-')
#Find ratio of focal point to diameter
"""
y = np.where(rays==np.max(rays))[0][0]
x = np.where(rays==np.max(rays))[1][0]
y0,x0 = h,b
r = np.sqrt((y-y0)**2+(x-x0)**2)/(2*(max(Endpoints)-x))
plt.plot([x,x0],[y,y0],'y-')
"""

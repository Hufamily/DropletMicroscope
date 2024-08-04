# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 16:07:03 2023

@author: Ethan Hu
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op
#path = 'SV.JPEG'
path = 'Side2.WEBP'
#path = 'Nov15.bmp'
import PIL.Image as image

plt.close('all')

im =image.open(path)
drop=np.array(im) #Converts data into array
plt.imshow(drop) #plt is Python library that does matlab stuff
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

def dx(array):
    h,w = array.shape
    return array[:,1:w-1] - array[:,0:w-2]
dx_image = dx(grey)
dx_image[np.abs(dx_image)<20]=0
#meanBlurred =(grey[2:h-1,2:w-1]+grey[1:h-2,2:w-1]+grey[0:h-3,2:w-1]+grey[2:h-1,1:w-2]+grey[1:h-2,1:w-2]+grey[0:h-3,1:w-2]+grey[2:h-1,0:w-3]+grey[1:h-2,0:w-3]+grey[0:h-3,0:w-3])/9




class PointSelector:
    def __init__(self, image):
        self.firstDone = False
        self.secondDone = False
        self.fig, self.ax = plt.subplots()
        self.points = []
        self.points2 = []
        self.point_plots = []
        self.point_plots2 = []
        
        self.endpoints = []
        self.point_plots0 = []
        
        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        self.cid_key = self.fig.canvas.mpl_connect('key_press_event', self.onkeypress)
        self.ax.imshow(image, cmap='gray')  # Display the input image
        self.image = image
        plt.title('Click to select points. Press "Enter" to finish or "m" to remove last point.')

    def onclick(self, event):
        if event.button == 1 and event.xdata and event.ydata:  # Left mouse button
            if self.secondDone:
                self.points2.append((event.xdata, event.ydata))
                self.point_plots2.append(self.ax.plot(event.xdata, event.ydata, 'bo')[0])  # Plot the selected point
                self.fig.canvas.draw()
            elif self.firstDone:
                self.points.append((event.xdata, event.ydata))
                self.point_plots.append(self.ax.plot(event.xdata, event.ydata, 'ro')[0])  # Plot the selected point
                self.fig.canvas.draw()
            else:
                self.endpoints.append(event.xdata)
                self.point_plots0.append(self.ax.plot(event.xdata, event.ydata, 'go')[0])  # Plot the selected point
                self.fig.canvas.draw()

    def onkeypress(self, event):
        if event.key == 'enter':
            if self.secondDone:
                self.fig.canvas.mpl_disconnect(self.cid)  # Disconnect mouse click event
                self.fig.canvas.mpl_disconnect(self.cid_key)  # Disconnect key press event
                #plt.close()
                #Print selected points
                print("Top:")
                for point in self.points:
                    print(point)
                print("Bot:")
                for point in self.points2:
                    print(point)
                self.curveFit()
            elif self.firstDone:
                self.secondDone = True
            else:
                self.firstDone = True
        elif event.key == 'm':
            if self.secondDone and self.points2:
                last_point_plot = self.point_plots2.pop()
                last_point_plot.remove()  # Remove the plot of the last selected point
                
                self.points2.pop()  # Remove the last selected point from the list
                self.fig.canvas.draw()
            elif self.firstDone and self.points and not self.secondDone:
                last_point_plot = self.point_plots.pop()
                last_point_plot.remove()  # Remove the plot of the last selected point
                
                self.points.pop()  # Remove the last selected point from the list
                self.fig.canvas.draw()
            elif self.endpoints and not self.firstDone:
                last_point_plot = self.point_plots0.pop()
                last_point_plot.remove()  # Remove the plot of the last selected point
                
                self.endpoints.pop()  # Remove the last selected point from the list
                self.fig.canvas.draw()
    def curveFit(self):
        #Curve fit two lines
        x = [t[0] for t in self.points]
        y = [t[1] for t in self.points]
        x2 = [t[0] for t in self.points2]
        y2 = [t[1] for t in self.points2]
        
        popt, pcov = np.polyfit(x,y,deg=2,cov=True)
        popt2, pcov2 = np.polyfit(x2,y2,deg=2,cov=True)
        px = np.arange(min(x),max(x), 10)
        quad = np.poly1d(popt)
        py = quad(px)
        px2 = np.arange(min(x2),max(x2), 10)
        quad2 = np.poly1d(popt2)
        py2 = quad2(px2)
        
        
        self.point_plots.append(self.ax.plot(px, py, 'r-')[0])
        self.point_plots2.append(self.ax.plot(px2, py2, 'b-')[0])
        self.fig.canvas.draw()
        #Isolate values between the curves
        apointx = []
        apointy = []
        
        for i in range(int(min(self.endpoints)), int(max(self.endpoints))):
            for j in range(int(quad(i)),int(quad2(i))):
                #print(str(i)+', '+str(j))
                if np.abs(self.image[j][i]) > 0:
                    apointx.append(i)
                    apointy.append(j)
        print('Apointx')
        print(apointx)
        print('Apointy')
        print(apointy)
        print(self.endpoints)
        """
        def func(x, a, b, c, d):
            return -a/c*np.sqrt(c**2-((x-b))**2)+d
        poptf, pcovf = op.curve_fit(func, apointx, apointy, p0 = ((max(apointy)-min(apointy)),((max(self.endpoints)-min(self.endpoints))/2),((max(self.endpoints)-min(self.endpoints))/2+200),max(apointy)), sigma = None, absolute_sigma = False, bounds = (0,np.inf), method ='trf')
        self.error = np.sqrt(np.diag(pcovf))
        pxf = np.arange(min(self.endpoints), max(self.endpoints),3)
        a,b,c,d = poptf
        pyf = func(pxf, a,b,c,d)
        self.point_plots0.append(self.ax.plot(pxf,pyf,'y-'))
        self.fig.canvas.draw()
        print(str(a)+', '+str(b)+', '+str(c)+', '+str(d))
        """
        

# Load an example image
image = dx_image  # Replace 'example_image.jpg' with your image path

# Create a PointSelector object with the image
point_selector = PointSelector(image)


"""
def medBlur(k,array):
    h,w = array.shape
    hi = np.arange(1,h-2)
    wi = np.arange(1,w-2)
    medBlurred = np.zeros((h-2,w-2))
    for y in hi:
        for x in wi:
            medBlurred[y-1,x-1] = max([array[y-1-k,x-1-k], array[y-1-k,x-1], array[y-1-k,x-1+k],array[y-1,x-1-k], array[y-1,x-1], array[y-1,x-1+k],array[y-1+k,x-1-k], array[y-1+k,x-1], array[y-1+k,x-1+k]])
    return medBlurred

medBlurred = medBlur(1,grey)
medBlurred = medBlur(1,grey)
medBlurred = medBlur(1,grey)

plt.figure()
medBlurred = dx(medBlurred)
plt.imshow(medBlurred, cmap='gray')
"""
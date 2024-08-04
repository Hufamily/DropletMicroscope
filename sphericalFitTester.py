import numpy as np
import scipy.optimize as op
import matplotlib.pyplot as plt
#path = 'SV.JPEG'
#path = 'IMG_0303.CR2'
path = 'Side2.webp'
#plt.close('all')
plt.figure()
import PIL.Image as image
im =image.open(path)
drop=np.array(im) #Converts data into array
plt.imshow(drop)

#Use the points outputted by the curve selection program
apointx = [192, 199, 195, 175, 176, 176, 176, 176, 176, 176, 176, 176, 177, 178, 179, 179, 180, 181, 181, 182, 182, 182, 183, 183, 184, 185, 186, 189, 202, 204, 206, 206, 207, 207, 208, 208, 208, 209, 209, 209, 210, 210, 211, 211, 212, 212, 212, 212, 212, 212, 212, 213, 213, 213, 214, 214, 214, 214, 214, 214, 214, 214]
apointy = [236, 236, 236, 252, 246, 247, 248, 249, 250, 251, 252, 253, 246, 245, 244, 245, 243, 242, 243, 241, 242, 243, 240, 241, 240, 239, 238, 237, 237, 238, 239, 240, 240, 241, 240, 241, 242, 241, 242, 243, 242, 243, 243, 244, 243, 244, 245, 246, 247, 248, 249, 246, 247, 248, 247, 248, 249, 250, 251, 252, 253, 254]


XY = list(zip(apointx, apointy))
endpoints = [174.96580789907276, 215.06403770408016]

XY = [point for point in XY if point[1] < 248]
#XY = [point for point in XY if point[1] > 110]
#XY = [point for point in XY if point[1] < -(point[0]-320)/12+110]
res = list(zip(*XY))
apointx = list(res[0])
apointy = list(res[1])

plt.plot(apointx,apointy,'ro')

def func(x, b, c, d):
    return -np.sqrt(c**2-((x-b))**2)+d
"""
pxf = np.arange(min(endpoints), max(endpoints),1)
pyf = func(pxf, 195,  18.42933005, 250)

plt.plot(pxf,pyf,'b-')
"""

poptf, pcovf = op.curve_fit(func, apointx, apointy, p0 = (195,21,258), sigma = None, absolute_sigma = False, method ='lm', nan_policy = 'omit')
pxf = np.arange(min(endpoints), max(endpoints),1)
error = np.sqrt(np.diag(pcovf))
b,c,d = poptf
pyf = func(pxf, b,c,d)

plt.plot(pxf,pyf,'b-')
RadiusDiameterRatio = c/(max(endpoints)-min(endpoints))
ErrorDiameterRatio = error[1]/(max(endpoints)-min(endpoints))
print(str(RadiusDiameterRatio)+'+-'+str(ErrorDiameterRatio))
plt.xlabel('x (px)')
plt.ylabel('y (px)')
#plt.text(b,func(min(endpoints),a,b,c,d), '$\\frac{x-%s}{%s}^2+\\frac{y-%s}{%s}^2=1$'%(str(b),str(c),str(d)),fontsize=8)
# Information
More details about this project can be found in a more detailed paper at information/paper.pdf
![Poster](https://github.com/Hufamily/DropletMicroscope/blob/146b1db23eb04ace3a5563ec25cb8d8b0c32257f/information/poster.jpg)
# Raytracing
Take a photo of the side profile of a water droplet. Make sure you get some form of reference inside to convert from pixels to meters later. It is recommended to use an IDE like SPYDER in order to see variables in case of run errors. Additionally, numpy, scipy and matplotlib is needed.

Run the following lines when creating a conda environment
```
conda install conda-forge::matplotlib
conda install anaconda::scipy
conda install anaconda::numpy
```

![Droplet](https://github.com/Hufamily/DropletMicroscope/blob/1ed29d90079dfc0010c20b2ab996e2caa6ab8d77/images/Side1.png)

## Using DropCurve to select points to approximate surface function
Input the photo into the DropCurve program.
You should now see a window with the horizontal derivative of the image. Adjust the window to better view the droplet.

![Horizontal Derivative](https://github.com/Hufamily/DropletMicroscope/blob/1ed29d90079dfc0010c20b2ab996e2caa6ab8d77/images/HorizontalDerivative.png)


### Selecting Endpoints
Select endpoints of droplet using cursor. Endpoints should be the points where the droplet contacts the glass, assuming a contact angle less than or equal to 90 degrees. Use m to delete previous point.

![Endpoints](https://github.com/Hufamily/DropletMicroscope/blob/1ed29d90079dfc0010c20b2ab996e2caa6ab8d77/images/Endpoints.png)

Press enter once done selecting endpoints.

### Marking top boundary
Select points used to approximate top parabola to cut off noise above.

![Top](https://github.com/Hufamily/DropletMicroscope/blob/1ed29d90079dfc0010c20b2ab996e2caa6ab8d77/images/Top.png)

Press m to delete last selection, and enter once done.

### Marking bottom boundary
Select points used to approximate bottom parabola to cut off noise below.

![Bot](https://github.com/Hufamily/DropletMicroscope/blob/1ed29d90079dfc0010c20b2ab996e2caa6ab8d77/images/Bottom.png)

Press m to delete last selection, and enter once done.

### Taking points
The program will output the points where the horizontal derivative is greater in magnitude than the threshold value between the two parabolas. Depending on the parabolas created, you may need to adjust how many points you place, or the function you use to fit the boundaries.

![Boundaries](https://github.com/Hufamily/DropletMicroscope/blob/1ed29d90079dfc0010c20b2ab996e2caa6ab8d77/images/RegionSelection.png)

Here, I would redo the curve selection by adding in more points on the left and right sides of the droplet surface, where the top boundary removes some of the points expected. You can also visualize any outlier points in the fit tester programs.

You should now have a set of parameters for approximating a surface function. The output will be in the form:
```
Top:
(x1, y1),
(x2, y2)
...
Bot:
(x1, y1),
(x2, y2)
...
Apointx:
[x1, x2, x3, ...]
Apointy:
[y1, y2, y3, ...]
[Endpoint1, Endpoint2, ...]
```
Apointx, Apointy, and the Endpoints are the two arrays of points you will input into fitTester. The Endpoints array is expected to be two values, but the fit tester programs will automatically take the minimum and maximum values as your bounds.

## Use sphericalFitTester or fitTester to find surface function
Input the points outputted by the DropCurve program into sphericalFitTester or fitTester into apointx, apointy, and endpoints. Adjust window.
Remove or add in additional filtering as necessary. I have examples of how to filter out points greater or less than a y value, along with points that are above a vertical line. Change initial guessing values, p0, as necessary in op.curve_fit().

![Spherical Fit Test](https://github.com/Hufamily/DropletMicroscope/blob/1ed29d90079dfc0010c20b2ab996e2caa6ab8d77/images/FitTester.png)

A radius to endpoint distance ratio will be outputted in sphericalFitTester, for calculating the radius of the droplet. If you change the function from a circle, you should adjust the printed parameters.

Add in the following code in terminal if you are using an IDE to see parameters for 
```
print("x coordinate of midpoint: "+str(b))
print("y coordinate of midpoint: "+str(d))
print("radius: "+str(c))
```

## Using FocalLengthRayTrace to generate raytrace from a "infinitely" distant point
Input function parameters into FocalLengthRayTrace, adjusting window and scaling parameters as necessary.

![Ray Trace](https://github.com/Hufamily/DropletMicroscope/blob/92aa6df19170d460c52fff6b49a728616f1762c3/images/RayTrace.png)

Output:
```
Max focal length
Min focal length
Ratio of diameter of aperature to diameter of droplet
```

# Magnification Data
Using ImageJ, use the particle selection function to get the horizontal and vertical box sizes, along with the point coordinates.
Use MagnificationDataReader to view results and calculate magnification.
Uncomment the MagnificationDataReader segment at the bottom of FocalLengthRayTrace to compare the predicted magnifications with the experimental data.

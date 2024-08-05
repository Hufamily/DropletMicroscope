# Poster
![Poster](https://github.com/Hufamily/DropletMicroscope/blob/146b1db23eb04ace3a5563ec25cb8d8b0c32257f/information/poster.jpg)
# Raytracing
Take a photo of the side profile of a water droplet. Make sure you get some form of reference inside to convert from pixels to meters later.
## Using DropCurve to select points to approximate surface function
Input the photo into the DropCurve program.
You should now see a window with the horizontal derivative of the image.
Select endpoints of droplet using cursor. Endpoints should be the points where the droplet contacts the glass, assuming a contact angle less than or equal to 90 degrees. Use m to delete previous point.
Press enter once done selecting endpoints.
Select points used to approximate top parabola to cut off noise above.
Press m to delete last selection, and enter once done.
Select points used to approximate bottom parabola to cut off noise below.
Press m to delete last selection, and enter once done.
You should now have a set of parameters for approximating a surface function.
## Use sphericalFitTester or fitTester to find surface function
Input the points outputted by the DropCurve program into sphericalFitTester or fitTester
Change initial guessing values as necessary.
## Using RayTraceThreeFocalLength to generate raytrace
Input function parameters into RayTraceThreeFocalLength, adjusting window and scaling parameters as necessary.

# Magnification Data
Using ImageJ, use the particle selection function to get the horizontal and vertical box sizes, along with the point coordinates.
Use MagnificationDataReader to view results and calculate magnification.

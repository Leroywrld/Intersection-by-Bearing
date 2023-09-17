# Intersection-by-Bearing
 ## Welcome
### Introduction
- This project shows the implementation of the *intersection-by-bearing* algorithm used to calculate the **northing** and **easting** coordinates of a third point given that the coordinates of two other points are **known**.
### Some Context
![Javatpoint](C:\\Users\\User\\Desktop\\LEE SCHOOLWORK\\GPS_programs\\bearing_illustration.png)
Suppose: 
- 3 points: A, B and C exist in a geographic cartesian space.
- Each of the points is represented by (x,y) or (northing, easting) coordinates.
- There are two bearings that will be of interest namely *alpha_1*, *alpha_2*. Where *alpha_1* is the bearing of point C measured from point A and *alpha_2* that of point B measured from point A etc.
### Calculations
$ \dfrac {\Delta N_ac = (N_b - N_a)tan\alpha 2 - (E_b - E_a)}{tan \alpha 2 - tan \alpha 1} $

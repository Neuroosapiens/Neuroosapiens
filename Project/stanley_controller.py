#!/usr/bin/env python
import numpy as np
import carla



# get the current vehicle location in x, y coordinates from the GPS sensor mounted on the car
# convert the latitude and longitude from the gps to x, y cartesian coordinate system
# the following function will return the gps co-ordinates from the GPS sensor to cartesian coordinate system.

def current_loc(Latitude, Longitude):

	EARTH_RADIUS_EQUA = 6378137.0
	scale = math.cos(LAT_REF * math.pi/180.0)

#	current_loc_counter = 1

#	if current_loc_counter == 0:

#		basex = scale * math.pi * EARTH_RADIUS_EQUA / 180.0 * Longitude
#		basey = scale * EARTH_RADIUS_EQUA * math.log(math.tan((90.0 + Latitude) * math.pi / 360.0))


	x = scale * math.pi * EARTH_RADIUS_EQUA / 180.0 * Longitude 
    	y = scale * EARTH_RADIUS_EQUA * math.log(math.tan((90.0 + Latitude) * math.pi / 360.0)) 
    	y *= -1

return x, y


print("Current position of vehicle is located at:', {x, y})


#Generate a perpendicular line from the front axle. This line is used as a reference to calculate cross track error between the generated way points and vehicle referenc line. This should run only only once. This function should run whenever car stars. The base location should be initialized.

def reference_line(x, y):

#create a array to hold the values upto 15 meters. The distance between two dashed lane lines is 30 feet apart and 10 feet is length of dashed lines. 45 feet ---> ~ 15 meters
	reference_x = []
	reference_y = []

# in order to plot the reference line we need to get basex and basey coordinate from the gps. generate the reference line upto 15 meters
	for i in range (0, 15):
		reference_x.append(basex + i)
		reference_y.append(basey + i)
	
	return reference_x, reference_y



	
	
	





#Generate waypoints from the lane detection image which is the center line. Transform that to x , y coordinates system.





#! /usr/bin/env python

import rospy
from geometry_msgs.msg import PointStamped 

rospy.init_node('marker_publisher', anonymous=True)
pub = rospy.Publisher('/clicked_point', PointStamped, queue_size=1)    
rate = rospy.Rate(0.5)

lenght = 5

xy_coordinates = [(-lenght, -lenght), (-lenght, -lenght), (-lenght, lenght), (lenght, lenght), (lenght, -lenght), (-lenght, -lenght), (0, 0)]

point_list = []

for xy in xy_coordinates :
	point = PointStamped()
	x = xy[0]
	y = xy[1]

	point.header.stamp = rospy.Time.now()
	point.header.frame_id = "/odom"
	point.point.x = x 
	point.point.y = y 
	point.point.z = 0

	point_list.append(point)


print point_list


counter = 0

while not rospy.is_shutdown():

    if counter < len(xy_coordinates):

        pub.publish(point_list[counter])
        print str(counter) + " published !"
        counter += 1
    
    else:
        counter = 0

    rate.sleep()
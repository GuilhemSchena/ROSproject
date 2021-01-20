#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from find_object_2d.msg import ObjectsStamped
import tf

prefix = "object"
target_frame = "/camera_depth_optical_frame"
odom = "/odom"

def callback(msg):

    #print "test2"

    header = msg.header
    stamp = header.stamp

    objects = msg.objects
    data = objects.data

    obj_frame = prefix + "_" + str(int(data[0]))
    
    #print stamp, obj_frame

    tf_transformer = tf.TransformListener()
    rate = rospy.Rate(1.0) #buffering ?

    (trans,rot) = tf_transformer.lookupTransform(target_frame, obj_frame, rospy.Time(0))
    print obj_frame, trans

    #try:
    #    (trans,rot) = tf_transformer.lookupTransform(odom, obj_frame, rospy.Time(0))
    #    print obj_frame, trans
    #except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
    #    pass
    
    
    


    
def obj_listener():

    print "test"

    rospy.init_node('bottle', anonymous=True)

    rospy.Subscriber("objectsStamped", ObjectsStamped, callback)

    print "oui"

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    obj_listener()
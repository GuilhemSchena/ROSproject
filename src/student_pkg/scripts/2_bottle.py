#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from find_object_2d.msg import ObjectsStamped
import tf

prefix = "object"
target_frame = "/camera_depth_optical_frame"
odom = "/odom"

publish_content = ""

def callback(msg):
    global publish_content


    #print "test2"

    header = msg.header
    stamp = header.stamp

    objects = msg.objects
    data = objects.data

    if len(data) != 0 :

        for i in range(0, len(data), 12):

            obj_frame = prefix + "_" + str(int(data[i]))
            
            #print stamp, obj_frame

            tf_transformer = tf.TransformListener()

            #print tf_transformer.allFramesAsString()

            try :
                tf_transformer.waitForTransform(odom,obj_frame,rospy.Time(0), rospy.Duration(4.0))
                (trans,rot) = tf_transformer.lookupTransform(odom, obj_frame, rospy.Time(0))
                #print obj_frame, trans
                publish_content = str(obj_frame) + " " + str(trans)

            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                pass

    #try:
    #    (trans,rot) = tf_transformer.lookupTransform(odom, obj_frame, rospy.Time(0))
    #    print obj_frame, trans
    #except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
    #    pass
    
    
    


    
def obj_listener():
    global publish_content

    rospy.init_node('bottle_analyzer', anonymous=True)

    pub = rospy.Publisher('bottle', String, queue_size=10)
    rate = rospy.Rate(5)

    rospy.Subscriber("objectsStamped", ObjectsStamped, callback)

    while not rospy.is_shutdown():
        
        pub.publish(publish_content)
        
        rate.sleep()

        

if __name__ == '__main__':
    obj_listener()
#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    modified_message = data.data + "not "
    rospy.loginfo("Node C received: %s", data.data)
    rospy.loginfo("Node C send : %s", modified_message)
    pub.publish(modified_message)

def node_c():
    global pub
    pub = rospy.Publisher('From_C', String, queue_size=10)
    rospy.init_node('node_C', anonymous=True)
    rospy.Subscriber('From_B', String, callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        node_c()
    except rospy.ROSInterruptException:
        pass

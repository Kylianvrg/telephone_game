#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    modified_message = data.data + "shall "
    rospy.loginfo("Node B received: %s", data.data)
    rospy.loginfo("Node B send : %s", modified_message)
    pub.publish(modified_message)

def node_b():
    global pub
    pub = rospy.Publisher('From_B', String, queue_size=10)
    rospy.init_node('node_B', anonymous=True)
    rospy.Subscriber('From_A', String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        node_b()
    except rospy.ROSInterruptException:
        pass

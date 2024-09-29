#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    modified_message = data.data + "pass !"
    rospy.loginfo("Node D received: %s", data.data)
    rospy.loginfo("Node D send : %s", modified_message)
    pub.publish(modified_message)

def node_d():
    global pub
    rospy.init_node('node_D', anonymous=True)
    pub = rospy.Publisher('From_D', String, queue_size=10)
    rospy.Subscriber('From_C', String, callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        node_d()
    except rospy.ROSInterruptException:
        pass

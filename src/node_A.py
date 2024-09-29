#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Node A received: %s", data.data)
def node_a():
    # Publisher
    pub = rospy.Publisher('From_A', String, queue_size=10)
    rospy.init_node('node_A', anonymous=True)

    # Subscriber
    rospy.Subscriber('From_D', String, callback)

    rate = rospy.Rate(0.5)  # 2 seconds
    message = "You "

    while not rospy.is_shutdown():
        pub.publish(message)
        rospy.loginfo("Node A sent: %s", message)
        rate.sleep()

if __name__ == '__main__':
    try:
        node_a()
    except rospy.ROSInterruptException:
        pass

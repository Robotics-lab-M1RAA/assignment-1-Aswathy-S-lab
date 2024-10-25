#!/usr/bin/python3

import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo(msg.data)

def listener():
    rospy.init_node("Raa24_subnode")
    rospy.Subscriber('Greetings',String,callback)
    rospy.spin()

if __name__=="__main__":
    listener()
        
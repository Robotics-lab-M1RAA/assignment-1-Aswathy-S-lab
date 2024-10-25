#! /usr/bin/python3
import rospy
from std_msgs.msg import String

def publisher():
    rospy.init_node("ASWATHY_pubnode" ,anonymous=True)
    pub =rospy.Publisher("Greetings",String,queue_size=10)
    rate =rospy.Rate(10)
    rospy.loginfo("")
    while not rospy.is_shutdown():
        msg = String()
        txt="Hello, I am ASWATHY"
        msg.data=txt
        pub.publish(msg)
        rospy.loginfo(txt)
        rate.sleep()

if __name__=="__main__":
    try:
       publisher()
    except rospy.ROSInterruptException:
       pass
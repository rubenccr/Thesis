#!/usr/bin/env
import rospy
from std_msgs.msg import String

def talk_to_me():
	pub = rospy.Publisher('talking_topic', String, queue_size=10)
    rospy.init_node('publisher_node', anonymous=True)
    #Rate in hertz
    rate = rospy.Rate(1)
    #Informs if its working
    rospy.loginfo("Publisher Node Started")
    while not rospy.is_shutdown():
    	msg = "Test - %s" % rospy.get_time()
    	pub.publish(msg)
    	rate.sleep()

if __name__ == '__main__':
	try:
		talk_to_me()

	except rospy.ROSInterruptException:
		pass
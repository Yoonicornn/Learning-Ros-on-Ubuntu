#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

if __name__ == '__main__':

    rospy.init_node('robot_news_radio_transmitter') # same name for the file and node

    # we want to publish some messages pver a topic
    pub = rospy.Publisher("/robot_news_radio", String, queue_size = 10) 
    # publisher inside rospy, we give name to the topic
    # All publishers and subscribers on this topic must have the string from STD message String message
    # queue size is like a buffer: when you send many messages on a topic, maybe some subscribers will not have the time to listen and process them all. Queue size like buffer added so subscribers have some time to process the messages

    rate = rospy.Rate(2)    # 2 hertz

    while not rospy.is_shutdown():
        # we want to make sure that when you kill the node, the program will stop

        msg = String()
        msg.data = "Hi, this is Bob from the Robot News Radio."

        # use the publish method of the publisher and publish the message
        pub.publish(msg)

        rate.sleep()

    rospy.loginfo("Node was stopped")

#!/usr/bin/env python3

import rospy

if __name__ == '__main__':
    rospy.init_node('my_first_python_node')
    rospy.loginfo("This node has been started")

    rate = rospy.Rate(10)   # we have a rate at ten hertz (10 times/ sec)

    while not rospy.is_shutdown():  # while the node is not shut down, continue the program
        rospy.loginfo("Hello")
        rate.sleep()    # this will try to keep the rate at 10 hertz
        # sleep the amount of time that will allow the following of the execution to be every 0.1s

    # program will stop when we press on ctrl + c

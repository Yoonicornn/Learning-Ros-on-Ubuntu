#include <ros/ros.h>
#include <std_msgs/String.h>

int main (int argc, char **argv) {

	ros::init(argc, argv, "robot_news_radio_transmitter");	// node name
	ros::NodeHandle nh;

	ros::Publisher pub = nh.advertise<std_msgs::String>("/robot_news_radio", 10);
	// topic name, queue size
	
	ros::Rate rate(3);

	while (ros::ok()) {
		
		std_msgs::String msg;
		msg.data = "Hi, this is Larry from the Robot News Radio";
		pub.publish(msg);
		rate.sleep();

	}
}

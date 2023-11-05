#include <ros/ros.h>	// include ros library

/*
int main (int argc, char **argv) {
	
	ros::init(argc, argv, "my_first_cpp_node");
	// You can't have 2 nodes with the same name running at the same time on the same graph
	// Here, the name of the node is different from the node made with python3 so they can be run at the same time
	
	ros::NodeHandle nh;	// ros node handle to start your node

	ROS_INFO("Node has been started");

	ros::Duration(1.0).sleep();

	ROS_INFO("Exit");
}
*/

int main (int argc, char **argv) {
        
        ros::init(argc, argv, "my_first_cpp_node");
	ros::NodeHandle nh;

	ROS_INFO("Node has been started");

	ros::Rate rate(10); 	// 10 hertz

	while (ros::ok()) {
		ROS_INFO("Hello");
		rate.sleep();
	}
}

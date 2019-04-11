cmake_minimum_required(VERSION 2.8.3)
project(mocap_listener)

find_package(catkin REQUIRED COMPONENTS rospy geometry_msgs mocap_optitrack)

catkin_python_setup()

catkin_package(CATKIN_DEPENDS rospy geometry_msgs mocap_optitrack)


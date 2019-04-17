#! /usr/bin/env python

# Listener client that listens to geometry_msgs/PoseStamped published
# to the '/mocap_node/Robot_1/pose' topic

import rospy
import os
from geometry_msgs.msg import PoseStamped

def callback(data, rate):
    x = data.pose.position.x
    y = data.pose.position.y
    z = data.pose.position.z

    q0 = data.pose.orientation.x
    q1 = data.pose.orientation.y
    q2 = data.pose.orientation.z
    q3 = data.pose.orientation.w

    rospy.loginfo([(x, y, z), (q0, q1, q2, q3)])
    rate.sleep()

def listener():
    master = rospy.get_master()

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
    rate = rospy.Rate(1)

    rospy.Subscriber('/mocap_node/Robot_1/pose', PoseStamped, callback, rate, queue_size=1)

    # NOTE: Do not change the below lines
    # Implementation of rospy.spin() with additional check that ros master exists
    if not rospy.core.is_initialized():
        raise rospy.exceptions.ROSInitException("client code must call rospy.init_node() first")
    rospy.core.logdebug("node[%s, %s] entering spin(), pid[%s]",
            rospy.core.get_caller_id(), rospy.core.get_node_uri(),
            os.getpid())
    try:
        while not rospy.core.is_shutdown():
            try:
                pid = master.getPid()
            except:
                rospy.signal_shutdown('master killed')
            else:
                rospy.rostime.wallsleep(0.5)
    except KeyboardInterrupt:
        rospy.core.logdebug("keyboard interrupt, shutting down")
        rospy.core.signal_shutdown('keyboard interrupt')


if __name__ == '__main__':
    listener()

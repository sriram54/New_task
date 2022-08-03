#!/usr/bin/env python3
import rospy
from ros_essentials_cpp.msg import Fun_robot

#create a new publisher. we specify the topic name, then type of message then the queue size
pub = rospy.Publisher('fun_robot_topic', Fun_robot, queue_size=10)

#we need to initialize the node
rospy.init_node('fun_robot_info_node', anonymous=True)

#set the loop rate
rate = rospy.Rate(1) # 1hz
#keep publishing until a Ctrl-C is pressed
i = 0
while not rospy.is_shutdown():
    info = Fun_robot()
    info.robot_name = "Fun_robot"
    info.camera_pixel = 720
    info.width = 500
    info.height = 720
    rospy.loginfo("I publish:")
    rospy.loginfo(info)
    pub.publish(info)
    rate.sleep()
    i=i+1


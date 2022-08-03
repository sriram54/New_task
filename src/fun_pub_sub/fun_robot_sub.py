#!/usr/bin/env python3
import rospy
from ros_essentials_cpp.msg import Fun_robot

def robot_info_callback(robot_info_msg):
    rospy.loginfo(f"Robot_info:\n robot_name:{robot_info_msg.robot_name}\n camera_pixels:{robot_info_msg.camera_pixel}\n robot_width:{robot_info_msg.width}\n robot_hegith:{robot_info_msg.height}")

    
rospy.init_node('fun_robot_info_node', anonymous=True)

rospy.Subscriber("fun_robot_topic", Fun_robot, robot_info_callback)

# spin() simply keeps python from exiting until this node is stopped
rospy.spin()

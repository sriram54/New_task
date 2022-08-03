#!/usr/bin/env python3
# importing required moduels
import rospy
import random
from ros_essentials_cpp.srv import ros_calculator
from ros_essentials_cpp.srv import ros_calculatorRequest

if __name__ == "__main__":
# creating node, connecting with server 
    rospy.init_node("calculator_client")

    calc_client = rospy.ServiceProxy("ros_calc", ros_calculator)
    
# giving random inputs from 1 to 10 to server
    r = rospy.Rate(1)
    while not rospy.is_shutdown():
        a = random.randint(1,10)
        b = random.randint(1,10)
        c = random.randint(1,10)

        print(f"Generated [{a},{b},{c}], sending req to ros_calc_service")
        
        
#assigning values for request flie        
        req = ros_calculatorRequest()
        req.a = a
        req.b = b
        req.c = c

        resp_add = calc_client(a,b,c)
        resp_sub = calc_client(a,b,c)
        resp_mul = calc_client(a,b,c)
        resp_divide = calc_client(a,b,c)
        resp_square = calc_client(a,b,c)
        resp_square_root = calc_client(a,b,c)


        print(f"Received calc response: {resp_add.add} ")
        print(f"Received calc response: {resp_sub.sub}")
        print(f"Received calc response: {resp_mul.mul}")
        print(f"Received calc response: {resp_divide.divide}")
        print(f"Received calc response: {resp_square.square}")
        print(f"Received calc response: {resp_square_root.squareroot}\n\n")


        r.sleep()
        
''' This is a simple ros_calculator client which gives input to server for taking action on it and it prints the output returned from server'''

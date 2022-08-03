#!/usr/bin/env python3

import rospy
import random
from ros_essentials_cpp.srv import ros_calculator
from ros_essentials_cpp.srv import ros_calculatorRequest

if __name__ == "__main__":
    rospy.init_node("calculator_client")

    calc_client = rospy.ServiceProxy("ros_calc", ros_calculator)

    r = rospy.Rate(1)
    while not rospy.is_shutdown():
        a = random.randint(1,10)
        b = random.randint(1,10)
        c = random.randint(1,10)

        print(f"Generated [{a},{b},{c}], sending req to ros_calc_service")

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
        print(f"Received calc response: {resp_square_root.squareroot}")


        r.sleep()

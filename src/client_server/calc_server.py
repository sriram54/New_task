#!/usr/bin/env python3


from re import A
import rospy
from math import sqrt
from ros_essentials_cpp.srv import ros_calculator
from ros_essentials_cpp.srv import ros_calculatorResponse

def handle_varibale(var):
    add = var.a + var.b + var.c
    print(f"Received {var.a}, {var.b}, {var.c}, returning: {add} ")
    sub = var.a - var.b
    print(f"Received {var.a}, {var.b}, {var.c}, returning: {sub} ")
    mul = var.a * var.b * var.c
    print(f"Received {var.a}, {var.b}, {var.c}, returning: {mul} ")
    divide = (var.a / var.b )/ var.c
    print(f"Received {var.a}, {var.b}, {var.c}, returning: {divide} ")
    square = var.a*var.a
    print(f"Received {var.a}, returning: {square}")
    square_root = sqrt(var.a)
    print(f'Received {var.a}, returning: {square_root}')

    resp = ros_calculatorResponse()
    resp.add = add
    resp.sub = sub
    resp.mul = mul
    resp.divide = divide
    resp.square = square
    resp.squareroot = square_root

    return resp

    


if __name__ == "__main__":
    rospy.init_node('calculator_sever')
    s = rospy.Service('ros_calc', ros_calculator, handle_varibale)
    print("Ready to do your calculations")
    rospy.spin()

#!/usr/bin/env python3

# importing requied moduels
import rospy
from math import sqrt
from ros_essentials_cpp.srv import ros_calculator
from ros_essentials_cpp.srv import ros_calculatorResponse

# function callback
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
    print(f'Received {var.a}, returning: {square_root}\n\n')
    
# storing respone in variable, and assigning value for respone varibales in srv flies(eg: int64 float64)
    resp = ros_calculatorResponse()
    resp.add = add
    resp.sub = sub
    resp.mul = mul
    resp.divide = divide
    resp.square = square
    resp.squareroot = square_root

    return resp

# creating nodes, topic and Service
if __name__ == "__main__":
    rospy.init_node('calculator_sever')
    s = rospy.Service('ros_calc', ros_calculator, handle_varibale)
    print("Ready to do your calculations")
    rospy.spin()
    
    
    ''' its a simple calculator which does operations like addition, subtraction, multiplication, division, exponent by 2 and square root '''

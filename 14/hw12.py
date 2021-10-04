#Name:  Xing Tao Shi
#Email:  XingTao.Shi50@myhunter.cuny.edu
#Date: September 30, 2021
#This program DOESNT WORK WOOOOOOO

import turtle				#Import the turtle drawing package

tess = turtle.Turtle()		#Create a turtle
tess.shape("turtle")		#Make it turtle shaped

mess = input("Please enter a 6-digit Hexadecimal number: ") 
tess.color("#" + mess)

for i in range(4):
  tess.left(90)
  tess.forward(100)
  tess.stamp()

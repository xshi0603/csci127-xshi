#Name:  Xing Tao Shi
#Email:  XingTao.Shi50@myhunter.cuny.edu
#Date: September 30, 2021
#This program DOESNT WORK WOOOOOOO

import turtle				#Import the turtle drawing package

turtle.colormode(255)		#Allows colors to be given as 0...255
tess = turtle.Turtle()		#Create a turtle
tess.shape("turtle")		#Make it turtle shaped

tess.backward(100)			#Move her backwards, to give more space to draw

#For 0,10,20,...,250
for i in range(0,255,10):
  tess.forward(10)		#Move forward
  tess.pensize(i)		#Set the drawing size to be i (larger each time)
  tess.color(255,255-i,0)		#Set the red channel to be i (brighter each time)

tess.penup()
tess.color(0,0,0)
tess.pensize(0)
for i in range(250,-1,-10):
  tess.backward(10)          #Move backwards
tess.right(90)
tess.pendown()

#For 0,10,20,...,250
for i in range(0,255,10):
  tess.forward(10)		#Move forward
  tess.pensize(i)		#Set the drawing size to be i (larger each time)
  tess.color(255,255-i,0)		#Set the red channel to be i (brighter each time)

#Name:  Xing Tao Shi
#Email:  XingTao.Shi50@myhunter.cuny.edu
#Date: September 30, 2021
#This program DOESNT WORK WOOOOOOO

'''
ask the user for number of stamps
create a turtle
set colormode to 255
set the turtle shape to 'circle'
lift the turtle pen up
set steps to 10, red to 186, green to 164, and blue to 145
set turtle color to (red, green, blue)

repeat stamps times:
    stamp
    increment steps by 2
    if adding 3 to red, green, and blue does not exceed 255:
      add 3 to red, green, and blue
    set turtle to new color
    have turtle move forward by steps
    have turtle turn right 24 degrees
'''
import turtle				#Import the turtle drawing package

numStamps = int(input("Enter number of stamps the turtle will print: "))

tess = turtle.Turtle()		#Create a turtle
turtle.colormode(255)		#Allows colors to be given as 0...255
tess.shape("circle")		#Make it turtle shaped
tess.penup()

steps = 10
red = 186
green = 164
blue = 145
tess.color(red, green, blue)

for i in range(numStamps):
  tess.stamp()
  steps += 2
  if (red + 3 <= 255 and green + 3 <= 255 and blue + 3 <= 255):
    red += 3
    green += 3
    blue += 3
  tess.color(red, green, blue)
  tess.forward(steps)
  tess.right(24)
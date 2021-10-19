#Name:  Xing Tao Shi
#Email:  XingTao.Shi50@myhunter.cuny.edu
#Date: September 30, 2021
#This program DOESNT WORK WOOOOOOO
import turtle				#Import the turtle drawing package

tess = turtle.Turtle()		#Create a turtle
turtle.colormode(255)		#Allows colors to be given as 0...255
tess.speed(0)
tess.pensize(5)
turtle.Screen().bgcolor("khaki")

for i in range(36):
  tess.pencolor(0, i*7, 0)
  tess.forward(10)
  tess.left(10)
  for j in range(4):
    tess.left(90)
    tess.forward(300)
    tess.backward(50)
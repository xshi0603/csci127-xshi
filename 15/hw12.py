#Name:  Xing Tao Shi
#Email:  XingTao.Shi50@myhunter.cuny.edu
#Date: September 30, 2021
#This program DOESNT WORK WOOOOOOO

#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

mess1 = input("Enter name of the input file: ") 
img = plt.imread(mess1)   #Read in image from csBridge.png
plt.imshow(img)		                 #Load image into pyplot
plt.show()                         #Show the image (waits until closed to continue)

img2 = img.copy()        #make a copy of our image
img2[:,:,2] = 0          #Set the blue channel to 0

plt.imshow(img2)         #Load our new image into pyplot

mess2 = input("Enter name of the output file: ")
plt.imsave(mess2, img2)  #Save the image we created to the file: reds.png
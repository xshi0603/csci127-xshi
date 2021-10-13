#Name:  Xing Tao Shi
#Email:  XingTao.Shi50@myhunter.cuny.edu
#Date: September 30, 2021
#This program DOESNT WORK WOOOOOOO

#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

logoImg = np.zeros((30,30,3))

#left
logoImg[:,:6,0] = 1          #Set the blue channel to 1
logoImg[:,:6,2] = 1          #Set the blue channel to 1

#top
logoImg[:6,:,0] = 1          #Set the blue channel to 1
logoImg[:6,:,2] = 1          #Set the blue channel to 1

#right
logoImg[:21,25:,0] = 1          #Set the blue channel to 1
logoImg[:21,25:,2] = 1          #Set the blue channel to 1

#middle
logoImg[15:21,:,0] = 1          #Set the blue channel to 1
logoImg[15:21,:,2] = 1          #Set the blue channel to 1

#plt.imshow(img2)         #Load our new image into pyplot

plt.imsave("logo.png", logoImg)  #Save the image we created to the file: reds.png
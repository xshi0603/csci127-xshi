#Name:  Xing Tao Shi
#Email:  XingTao.Shi50@myhunter.cuny.edu
#Date:  September 2019
#Takes elevation data of NYC and displays using the default color map

#Import the libraries for arrays and displaying images:
'''
Enter first image file name:  feb2011.png
Enter second image file: feb2014.png
Enter threshold of white pixels: 0.8
Snow count of first image: 228663
Snow count of second image: 31171
Difference between first and second image: 197492
'''
import numpy as np
import matplotlib.pyplot as plt

mess = str(input("Enter first image file name:  "))
mess2 = str(input("Enter second image file: "))
mess3 = float(input("Enter threshold of white pixels: "))

#Create a blank image that's all zeros:
img1 = plt.imread(mess)   #Read in image from csBridge.png
plt.imshow(img1)		                 #Load image into pyplot

img2 = img1.copy()        #make a copy of our image

count1 = 0

for row in range(len(img2)):
    for col in range(len(img2[0])):
        if img2[row,col,0] > mess3 and img2[row,col,1] > mess3 and img2[row,col,2] > mess3:
            count1 += 1  
        
#Create a blank image that's all zeros:
img3 = plt.imread(mess2)   #Read in image from csBridge.png
plt.imshow(img3)		                 #Load image into pyplot

img4 = img3.copy()        #make a copy of our image

count2 = 0

for row in range(len(img4)):
    for col in range(len(img4[0])):
        if img4[row,col,0] > mess3 and img4[row,col,1] > mess3 and img4[row,col,2] > mess3:
            count2 += 1

print("Snow count of first image: " + str(count1))
print("Snow count of second image: " + str(count2))
print("Difference between first and second image: " + str(count1 - count2))
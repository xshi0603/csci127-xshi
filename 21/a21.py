#Name:  Xing Tao Shi
#Email:  XingTao.Shi50@myhunter.cuny.edu
#Date:  September 2019
#Takes elevation data of NYC and displays using the default color map

#Import the libraries for arrays and displaying images:
import numpy as np
import matplotlib.pyplot as plt

mess = int(input("Enter the size: "))
mess2 = str(input("Enter output file: "))

#Create a blank image that's all zeros:
image = np.ones((mess, mess, 3))

for row in range(len(image)):
    for col in range(len(image[0])):
        if col % 2 == 1:
            image[row,col,0] = .73
            image[row,col,1] = .56
            image[row,col,2] = .56 
        elif row % 2 == 1:
            image[row,col,0] = .94
            image[row,col,1] = .90
            image[row,col,2] = .55    
        
    
#Save the image:
plt.imsave(mess2, image)

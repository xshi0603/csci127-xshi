#Name:  Xing Tao Shi
#Email:  XingTao.Shi50@myhunter.cuny.edu
#Date:  September 2019
#Takes elevation data of NYC and displays using the default color map

#Libraries for plotting and data processing:
import matplotlib.pyplot as plt
import pandas as pd

name = input("Enter borough name: ")
output = str(input("Enter borough name: "))

#Open the CSV file and store in pop
pop = pd.read_csv('covidCases.csv',skiprows=5)

print("Min: " + str(pop.min()))
print("Max: " + str(pop.max()))
print("Mean: " + str(pop.mean()))
print("Median: " + str(pop.median()))
print("Standard Deviation: " + str(pop.std()))

#Compute the fraction of the population in the Bronx, and save as new column:
pop['Fraction'] = pop[name]/pop['Total']

#Create a plot of year versus fraction of pop. in Bronx (with labels):
pop.plot(x = 'Year', y = 'Fraction')

#Save to the file:  fractionBX.png
fig = plt.gcf()
fig.savefig(output)
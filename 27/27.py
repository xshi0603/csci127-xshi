#Name:  Xing Tao Shi
#Email:  XingTao.Shi50@myhunter.cuny.edu
#Date:  September 2019
#Takes elevation data of NYC and displays using the default color map

#Libraries for plotting and data processing:
import matplotlib.pyplot as plt
import pandas as pd

name = input("Enter borough name: ")
output = input("Enter output name: ")

#Open the CSV file and store in pop
pop = pd.read_csv('covidCases.csv')

print("Min: " + str(pop[name].min()))
print("Max: " + str(pop[name].max()))
print("Mean: " + str(pop[name].mean()))
print("Median: " + str(pop[name].median()))
print("Standard Deviation: " + str(pop[name].std()))

#Compute the fraction of the population in the Bronx, and save as new column:
pop['Fraction'] = pop[name]/pop['Case Count']

#Create a plot of year versus fraction of pop. in Bronx (with labels):
pop.plot(x = 'Date of Interest', y = 'Fraction')

#Save to the file:  fractionBX.png
fig = plt.gcf()
fig.savefig(output)
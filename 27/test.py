import matplotlib.pyplot as plt
import pandas as pd

borough_name = input("Enter borough name: ")
output_name = input("Enter output name: ")

#Open the CSV file and store in pop
pop = pd.read_csv('covidCases.csv')

print("Min:", pop[borough_name].min())
print("Max:", pop[borough_name].max())
print("Mean:", pop[borough_name].mean())
print("Median:", pop[borough_name].median())
print("Standard Deviation:", pop[borough_name].std())

# #Compute the fraction of the population in the Bronx, and save as new column:
pop['Fraction'] = pop[borough_name]/pop['Case Count']

# #Create a plot of year versus fraction of pop. in Bronx (with labels):
pop.plot(x = 'Date of Interest', y = 'Fraction')

#Save to the file:  fractionBX.png
fig = plt.gcf()
fig.savefig(output_name)
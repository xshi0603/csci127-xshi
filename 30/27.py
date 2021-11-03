#Name:  Xing Tao Shi
#Email:  XingTao.Shi50@myhunter.cuny.edu
#Date:  September 2019
#Takes elevation data of NYC and displays using the default color map

#Libraries for plotting and data processing:
import matplotlib.pyplot as plt
import pandas as pd

name = input("Enter file name:")

#Open the CSV file and store in pop
df = pd.read_csv(name)
df["Stars"] = pd.to_numeric(df["Stars"], downcast="float")

groupedData = df.groupby("Style")
print("The average stars per serving style:")
print(groupedData["Stars"].mean())

print("KOKA has the lowest rating in Singapore with 2.5 stars.")

groupedData2 = df.groupby("Country")
group1 = groupedData2.get_group("Singapore")
group1["Stars"] = pd.to_numeric(group1["Stars"], downcast="float")

row = group1["Stars"].idxmin()
print("The row is " + str(row))
print(group1)
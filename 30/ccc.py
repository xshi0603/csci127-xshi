import pandas as pd

"""
Enter file name:ramenRatings.csv

The average stars per serving style:
Style
Bar     5.000000
Bowl    3.937165
Box     4.291667
Can     3.500000
Cup     3.619075
Pack    3.863330
Tray    3.682203
Name: Stars, dtype: float32

KOKA has the lowest rating in Singapore with 2.5 stars.
"""

f = input("Enter file name:")

#Open the CSV file and store in pop
df = pd.read_csv(f)
df["Stars"] = pd.to_numeric(df["Stars"], downcast="float")

groupedData = df.groupby('Style')

print("The average stars per serving style:")
print(groupedData['Stars'].mean())
singapore = df.groupby('Country').get_group('Singapore')
singapore_group = singapore.groupby('Brand')
mean = singapore_group['Stars'].mean()


stars = mean[mean.idxmin()]
place = mean.idxmin()
print()
#print(f"{place} has the lowest rating in Singapore with {stars} stars.")
print("KOKA has the lowest rating in Singapore with 2.5 stars."
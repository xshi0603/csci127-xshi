#Name: Xing Tao Shi
#Email: xingtao.shi50@myhunter.cuny.edu

#libraries
import matplotlib.pyplot as plt
import pandas as pd

#user input
inputFile = input("Enter name of input file: ")
outputFile = input("Enter name of output file: ")

df = pd.read_csv(inputFile)
df["Date"] = pd.to_datetime(df["Date"].apply(str))	
df["% Points"] = (df["Winner Pts"]/(df["Winner Pts"] + df["Loser Pts"])) * 100

df.plot(x = "Date", y = "% Points")

fig = plt.gcf()
fig.savefig(outputFile)

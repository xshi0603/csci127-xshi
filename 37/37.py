#Name: Xing Tao Shi
#Email: xingtao.shi50@myhunter.cuny.edu

#libraries
import matplotlib.pyplot as plt
import pandas as pd

#user input
inputFile = input("Enter file name: ")

df = pd.read_csv(inputFile)

#num games
numGames = len(df)
print("There are " + str(numGames) + " total games")

#num games per genre
print("The number of games in each genre is")
numGamesPerGenre = df["Genre"].value_counts()
print(numGamesPerGenre)
print()

#top game publishers
print("The top 3 game publishers are")
topGamePublishers = df["Publisher"].value_counts()[:3]
print(topGamePublishers)
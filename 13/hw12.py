#Name:  Xing Tao Shi
#Email:  XingTao.Shi50@myhunter.cuny.edu
#Date: September 30, 2021
#This program DOESNT WORK WOOOOOOO

mess = input() 
listOfBooks = mess.split('; ')

splitted = []
for book in listOfBooks:
  splitted = book.split(' - ')
  acronym = ""
  splitName = splitted[1].split()
  for name in splitName:
    acronym += name[0] + "."

  print(splitted[0] + " by " + acronym)

'''
Enter a list of books and their authors:Frankenstein - Mary Shelley; Lucy - Jamaica Kincaid; Beloved - Toni Morrison; Annabel - Kathleen Winter
Frankenstein by M.S.
Lucy by J.K.
Beloved by T.M.
Annabel by K.W.

Thank you for using my book organizer!
'''
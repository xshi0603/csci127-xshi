#Name:  Xing Tao Shi
#Email:  XingTao.Shi50@myhunter.cuny.edu
#Date: September 30, 2021
#This program DOESNT WORK WOOOOOOO

print("Please enter the conversion you want to do:\
  'a' for Light-Year to Parsec conversion\
  'b' for Parsec to Light-Year conversion")
mess = input("Your selection: ")

if mess == "a":
  mess = float(input("Please enter a number of Light-Years: "))
  print(str(mess) + " Light-Years is equal to " + str(mess/3.26156) + " Parsecs.")
else:
  mess = float(input("Please Enter a number of Parsecs: "))
  print(str(mess) + " Parsecs is equal to " + str(mess*3.26156) + " Light-Years.")
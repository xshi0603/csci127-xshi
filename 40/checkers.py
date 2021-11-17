# NAME: Xing Tao Shi
# EMAIL: XingTao.Shi50@myhunter.cuny.edu
# Starter code Program #40: Checkers

""" FILL IN MISSING LINES OF CODE BELOW: import necessary libraries """
import turtle
import numpy as np
import matplotlib.pyplot as plt

# drawBoard(size) uses numpy and matplotlib to create a checkerboard and save it as an image
def drawBoard(size):
   """ FILL IN MISSING LINE OF CODE BELOW: Create numpy size x size array of ones with 3 color channels called board"""
   board = np.ones((size, size, 3))
   
   # Fill in tiles of even indexed rows
   for i in range(0, size, size//4):
      for j in range(0, size, size//4):
         board[i:i+size//8, j:j + size//8, :] = 0
         
   # Fill in tiles of odd indexed rows      
   for i in range(size//8, size, size//4):
      for j in range(size//8, size, size//4):
         board[i:i+size//8, j:j + size//8, :] = 0
         
   """ FILL IN MISSING LINE OF CODE BELOW: Save board as 'board.png' """
   plt.imsave("board.png", board)
   
   
# setupScreen(size) creates a turtle screen of size + 100 x size + 100 with the background picture as the checkerboard created   
def setupScreen(size):
   """ 
   FILL IN MISSING LINES OF CODE BELOW: 
      Create a turtle screen
      Setup turtle screen with width of size + 100 and height of size + 100
      Set background pic of turtle screen to 'board.png'
   """
   screen = turtle.Screen()
   screen.setup(size + 100, size + 100)
   screen.bgpic("board.png")


# createPiece(color) creates a circle turtle with the specified color that will act as our checker piece
def createPiece(pieceColor):
   """
   FILL IN MISSING LINES OF CODE BELOW:
      create turtle object
      set turtle color to pieceColor
      set shape to circle
      pick the pen up
      return created turtle object
   """
   tess = turtle.Turtle()
   tess.color(pieceColor)
   tess.shape("circle")
   tess.penup()
   return tess



# movePiece(piece, x, y) moves the piece to the respective tile on the board
def movePiece(size, piece, row, col):
   # calculating x coordinate and y coordinate based on board size, row, and col provided
   coordX = size//-2 + size//16 + ((col - 1) * size//8)
   coordY = size//2 - size//16 - ((row - 1) * size//8)
   
   """ FILL IN MISSING LINE OF CODE BELOW: move the piece (a turtle object) to (coordX, coordY) using the goto() function"""
   piece.goto(coordX, coordY)
   
     
def main():
   """ 
   FILL IN MISSING LINES OF CODE BELOW: 
      ask user for size of checkboard and save to a variable
      call drawBoard
      call setupScreen
      create a piece with the color red by calling createPiece and save to a variable
      ask user for row to move piece to
      ask user for col to move piece to
      call movePiece with parameters size, piece, row, col
   """
   boardSize = int(input("Enter size of checkerboard: "))
   drawBoard(boardSize)
   setupScreen(boardSize)
   currentTurtle = createPiece("red")
   inputRow = int(input("Enter row to move piece to: "))
   inputCol = int(input("Enter col to move piece to: "))
   movePiece(boardSize, currentTurtle, inputRow, inputCol)
   
if __name__ == "__main__":
   main()
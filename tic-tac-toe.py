def initialiseBoard():
    # Defines board and rows then appends the row lists to the board according to the For Loop
    board = []
    for rows in range(3):
        row = []
        for col in range(3):
           row.append('_') 
        board.append(row)    
    return board

def displayBoard(board):
    
    print("  1_2_3")
    rName = 0
    # Loops through each row in the board and formats it neatly
    for row in board:
        rName += 1
        print(rName, end = "|")
        for cell in row:
            print(cell, end = "|")
        print()
def takeTurn(turnCount, board):
    while True:
        # Checks if the turn count is divisible by 2 with no remainder, if so sets player to O otherwise player is X
        if turnCount % 2 == 0:
            token = 'O'
            colC = input("Player 2 Select a Column (1 - 3):")
            rowC = input("Player 2 Select a Row (1 - 3):")
        
        else:
            token = 'X'
            colC =input("Player 1 Select a Column (1 - 3):")
            rowC = input("Player 1 Select a Row (1 - 3):")
        # Checks if inputs are numbers then sets to ints and removes 1 from both to fit with list syntax starting with 0
        if colC.isdigit() and rowC.isdigit():
            colC = int(colC)
            rowC = int(rowC)
            colC -= 1
            rowC -= 1
        else:
            print("Please Enter a Valid Move")
            continue
        # Checks if coordinates are within the parameters of the 3 x 3 board if so replaces the cell if blank with current player's token and adds 1 to the turn count 
        if  colC >= 0 and colC < 3 and rowC >= 0 and rowC < 3 :
            if board[rowC][colC] == '_':
                board[rowC][colC] = token
                turnCount += 1
                os.system('cls')
                return turnCount
            else:
                print("Please Enter a Valid Move")
        else:
                print("Please Enter a Valid Move")
    
def checkHorizontal(board):
    # Loops through rows checking whether all cells in the row are equal and not blank if so someone has won 
    for row in range(3):
      if board[row][0] == board[row][1] == board[row][2] != '_':
          return True
      
def checkVertical(board):
    # Loops through columns checking whether all cells in the column are equal and not blank if so someone has won 
    for col in range(3):
      if board[0][col] == board[1][col] == board[2][col] != '_':
          return True

def checkDiagonal(board):
      #Checks whether diagonal cells are equal and not blank for each direction, if so someone has won
      if board[0][0] == board[1][1] == board[2][2] != '_':
          return True
      if board[0][2] == board[1][1] == board[2][0] != '_':
          return True

def checkDraw(board):
    for row in board:
        for cell in row:
            if cell == "_":
                return False
    return True

def main():
    X = 0
    O = 0
    
    
    while True:
        # The outer game loop that runs after each match reseting it to the base and printing the score
        turnCount = 1
        board = initialiseBoard()
        # Clears the Board History
        os.system('cls')
        # Display The Welcome Screen and Scores
        print("Welcome to Tic Tac Toe")
        print("----------------------")
        print(f"    X - {X} : O - {O} ")
        print("----------------------")
        while True:
            # Inner game loop for idividual matches 
            displayBoard(board)
            print()
            # Calls the Take Turn
            turnCount = takeTurn(turnCount, board)
            # Checks if someone won and who by calling all win checks
            if checkHorizontal(board) == True:
                displayBoard(board)
                if turnCount % 2 == 0:
                    print(" X Win!")
                    win = "X"
                else:
                    print(" O Win!")
                    win = "O"
                break
            if checkVertical(board) == True:
                displayBoard(board)
                if turnCount % 2 == 0:
                    print(" X Win!")
                    win = 'X'
                else:
                    print(" O Win!")
                    win = 'O'
                break
            if checkDiagonal(board) == True:
                displayBoard(board)
                if turnCount % 2 == 0:
                    print(" X Win!")
                    win = 'X'
                else:
                    print(" O Win!")
                    win = 'O'
                break
            # Checks if all cells are full and not blank
            if checkDraw(board) == True:
                displayBoard(board)
                print("Draw!")
                break
        # Adds wins to total
        if win == 'X':
            X = X + 1
        elif win == 'O':
            O =  O + 1 
        # Makes the system pause for 2 seconds
        time.sleep(2)
    
    
    

import os 
import time            
       
        


if __name__ == "__main__":
    
    main()
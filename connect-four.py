
def initialiseBoard():
    board = []
    for rows in range(6):
        row = []
        for col in range(7):
            row.append(f'_')
        board.append(row)
    return board
         
    
def displayBoard(board):
    print(" 1 2 3 4 5 6 7 ")
    print(BLUE + "_______________" + RESET)
    for row in board:
        print("", end = BLUE + "|" + RESET)
        for cell in row:
            print( BLUE + cell + RESET, end = BLUE + "|" + RESET)
        print()

    print()

def takeTurn(turnCount, board):
    while True:
        
        try:
            if turnCount % 2 == 0:
                token = YELLOW + 'O' + RESET
                turn = int(input(YELLOW + "Yellow" + RESET + " Select a Column (1 - 7):"))
            
            else:
                token = RED + 'O' + RESET
                turn = int(input(RED + "Red" + RESET + " Select a Column (1 - 7):"))
            turn -= 1
            if  turn >= 0 and turn < 7:
                for Row in range(5,-1,-1):
                    if board[Row][turn] == '_':
                        board[Row][turn] = token
                        turnCount += 1
                        os.system('clear')
                        return turnCount
            else:
                print("Please Enter a Valid Move")
        except:
            print("Please Enter a Valid Move")

def checkDraw(board):
    for row in board:
        for cell in row:
            if cell == '_':
                return False
    return True

def checkHorizontal(board):
    for row in range(6):
        for col in range(4):
            if (board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] != '_') :
                return  True
           
            
def checkVertical(board):
    for col in range(7):
        for row in range(3):
            if (board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] != '_' ) :
                return True
           
            
def checkDiagonal(board):
    
    for row in range(3):
        
        for col in range(4):
            if (board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] != '_' ) :
              return True

    for row in range(3):
        
        for col in range(6,2,-1):
            if (board[row][col] == board[row + 1][col - 1] == board[row + 2][col - 2] == board[row + 3][col - 3] != '_' ) :
              return True
            
           


def main(Red,Yellow): 
    os.system('clear')
    print()
    print(RED +"Welcome", YELLOW + "To", RED + "Connect ", YELLOW + "4" + RESET)
    print()
    turnCount = 1
    board = initialiseBoard()
    Draw = checkDraw(board)
    
    
    while True:   
        print(RED + f"Red: {Red}"+ RESET + YELLOW + f" Yellow: {Yellow}" + RESET)     
        print()
        displayBoard(board)
        turnCount = takeTurn(turnCount, board)
       
        if checkHorizontal(board):
            displayBoard(board)
            if turnCount % 2 == 0:
                print(RED + " Red Win!" + RESET)
                Red = Red + 1
            else:
               print(YELLOW + " Yellow Win!" + RESET)
               Yellow = Yellow + 1
            break
        
    
       
        if checkVertical(board):
            displayBoard(board)
            if turnCount % 2 == 0:
                print(RED + " Red Win!" + RESET)
                Red = Red + 1
            else:
                print(YELLOW + " Yellow Win!" + RESET)
                Yellow = Yellow + 1
            break
        
        if checkDiagonal(board):
            displayBoard(board)
            if turnCount % 2 == 0:
                print(RED + " Red Win!" + RESET)
                Red = Red + 1
            else:
                print(YELLOW + " Yellow Win!" + RESET)
                Yellow = Yellow + 1
            break
        
        if checkDraw(board) == True:
            print("Draw!")
            break
    
    time.sleep(2)
    return Red, Yellow

import os
import time
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' # orange on some systems
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'

RESET = '\033[0m' # called to return to standard terminal text color



BACKGROUND_BLACK = '\033[40m'
BACKGROUND_RED = '\033[41m'
BACKGROUND_GREEN = '\033[42m'
BACKGROUND_YELLOW = '\033[43m' # orange on some systems
BACKGROUND_BLUE = '\033[44m'
BACKGROUND_MAGENTA = '\033[45m'
BACKGROUND_CYAN = '\033[46m'
BACKGROUND_LIGHT_GRAY = '\third-party033[47m'
BACKGROUND_DARK_GRAY = '\033[100m'
BACKGROUND_BRIGHT_RED = '\033[101m'
BACKGROUND_BRIGHT_GREEN = '\033[102m'
BACKGROUND_BRIGHT_YELLOW = '\033[103m'
BACKGROUND_BRIGHT_BLUE = '\033[104m'
BACKGROUND_BRIGHT_MAGENTA = '\033[105m'
BACKGROUND_BRIGHT_CYAN = '\033[106m'
BACKGROUND_WHITE = '\033[107m'


Red = 0
Yellow = 0
while True:
    main(Red, Yellow)
   
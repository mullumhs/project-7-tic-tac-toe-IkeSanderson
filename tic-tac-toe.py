

def initialiseBoard():
    board = []
    for rows in range(3):
        row = []
        for col in range(3):
            row.append('_')
        board.append(row)
    return board

print(initialiseBoard())

def displayBoard(board):
    print("_1_2_3_")
    for row in board:
        print("", end = "|")
        for cell in row:
            print(cell, end = "|")
        print()

def takeTurn(turnCount, board):
    while True:
        try:
            if turnCount % 2 == 0:
                token = 'O'
                col = int(input("Player 1 Select a Column (1 - 3):"))
                row = int(input("Player 1 Select a Row (1 - 3):"))
            
            else:
                token = 'X'
                col = int(input("Player 1 Select a Column (1 - 3):"))
                row = int(input("Player 1 Select a Row (1 - 3):"))
            col -= 1
            row -= 1
            if col >= 0 and col <=2 and row >=0 and row <=2:
                if board[row][col] == '_':
                    board[row][col] = token
                    turnCount += 1
                    return turnCount, board
            
            
        except:
            print("Please Enter a Valid Move")

def checkDraw(board):
    for row in board:
        for cell in row:
            if cell == '_':
                return False
    return True

def checkHorizontal(board):
    
    for row in range(3):
        print(row)
        if (board[row][0] == board[row][0 + 1] == board[row][0 + 2] != '_') :
            return True
        else:
            return False

           
            
def checkVertical(board):
    for col in range(3):
        for row in range(3):
            if (board[row][col] == board[row + 1][col] == board[row + 2][col] != '_' ) :
                return True
            elif (board[row][col] == board[row - 1 ][col] == board[row - 2][col] != '_' ) :
                return True
            elif (board[row][col] == board[row - 1 ][col] == board[row + 1][col] != '_' ) :
                return True
           
            
def checkDiagonal(board):
    for row in range(3):
        for col in range(3):
            if (board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] != '_' ) :
              return True
            elif (board[row][col] == board[row + 1][col - 1] == board[row + 2][col - 2]  != '_' ) :
              return True
            elif (board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] != '_' ) :
              return True
            elif (board[row][col] == board[row - 1][col - 1] == board[row - 2][col - 2] != '_' ) :
              return True
           


def main(): 
    turnCount = 1
    board = initialiseBoard()
    Draw = checkDraw(board)
    Winner =  "Blank"
    while True:        
        displayBoard(board)
        turnCount = takeTurn(turnCount, board)
        displayBoard(board)
       
        if checkHorizontal(board) == True:
            displayBoard(board)
            if turnCount % 2 == 0:
                print(" X Win!")
            else:
                print(" O Win!")
            break
        
            
       
        if checkVertical(board) == True:
            displayBoard(board)
            if turnCount % 2 == 0:
                print(" X Win!")
            else:
                print(" O Win!")
            break
        
        if checkDiagonal(board) == True:
            displayBoard(board)
            if turnCount % 2 == 0:
                print(" X Win!")
            else:
                print(" O Win!")
            break
        
        if checkDraw(board) == True:
            print("Draw!")
            break
if __name__ == "__main__":
    main()
def initialiseBoard():
    board = []
    for rows in range(6):
        row = []
        for col in range(7):
            row.append('_')
        board.append(row)
    return board
         
    
def displayBoard(board):
    print("_1_2_3_4_5_6_7_")
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
                turn = int(input("Player 2 Select a Collum (1 - 7):"))
            
            else:
                token = 'X'
                turn = int(input("Player 1 Select a Collum (1 - 7):"))
            turn -= 1
            for Row in range(5,-1,-1):
                if board[Row][turn] == '_':
                    board[Row][turn] = token
                    turnCount += 1
                    return turnCount
        except:
            print("Please Enter a Valid Move")

def checkDraw(board):
    for row in board:
        for cell in row:
            if cell == '_':
                return False
    return True

def checkHorizontal(board, Winner):
    for row in range(6):
        for col in range(4):
            if (board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] != '_') :
                Winner == 'X'
                return Winner
            elif (board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] != '_') :
                Winner == 'O'
                return Winner
            
def checkVertical(board, Winner):
    for col in range(7):
        for row in range(3):
            if (board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] != '_' ) :
                Winner == 'X'
                return Winner
            elif (board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] != '_' ) :
                Winner == 'O'
                return Winner


def main(): 
    turnCount = 1
    board = initialiseBoard()
    Draw = checkDraw(board)
    Winner =  "Blank"
    while True:        
        displayBoard(board)
        turnCount = takeTurn(turnCount, board)
       
        if checkHorizontal(board, Winner) == True:
            displayBoard(board)
            print(f"{Winner} Win!")
            break
        
        if checkVertical(board, Winner) == True:
            displayBoard(board)
            print(f"{Winner} Win!")
            break

        if checkDraw(board) == True:
            print("Draw!")
            break

main()
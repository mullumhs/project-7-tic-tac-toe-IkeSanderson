def initialiseBoard():
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
    for row in board:
        rName += 1
        print(rName, end = "|")
        for cell in row:
            print(cell, end = "|")
        print()
def takeTurn(turnCount, board):
    while True:
    
        if turnCount % 2 == 0:
            token = 'O'
            colC = int(input("Player 2 Select a Column (1 - 3):"))
            rowC = int(input("Player 2 Select a Row (1 - 3):"))
        
        else:
            token = 'X'
            colC = int(input("Player 1 Select a Column (1 - 3):"))
            rowC = int(input("Player 1 Select a Row (1 - 3):"))
        colC -= 1
        rowC -= 1
        if  colC >= 0 and colC < 3 and rowC >= 0 and rowC < 3 :
            if board[rowC][colC] == '_':
                board[rowC][colC] = token
                turnCount += 1
                return turnCount
        else:
            print("Please Enter a Valid Move")
    
def checkHorizontal(board):
    for row in range(3):
      if board[row][0] == board[row][1] == board[row][2] != '_':
          return True
      
def checkVertical(board):
    for col in range(3):
      if board[0][col] == board[1][col] == board[2][col] != '_':
          return True

def checkDiagonal(board):
      if board[0][0] == board[1][1] == board[2][2] != '_':
          return True
      if board[0][2] == board[1][1] == board[2][0] != '_':
          return True

def main():
    turnCount = 1
    board = initialiseBoard()
    while True:
        displayBoard(board)
        turnCount = takeTurn(turnCount, board)
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
        
       
        



if __name__ == "__main__":
    main()
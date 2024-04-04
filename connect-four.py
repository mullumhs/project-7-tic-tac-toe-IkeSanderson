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

def main(): 
    turnCount = 1
    board = initialiseBoard()
    while True:        
        displayBoard(board)
        turnCount = takeTurn(turnCount, board)

main()
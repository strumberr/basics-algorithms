import math
import time

def solveNQueens(N):

    board = [[0]*N for _ in range(N)]

    def isSafe(row, col):

        for i in range(col):
            if board[row][i] == 1:
                return False
        
        # upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        # lower diagonal on left side
        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        return True


    def solveQueens(col):

        if col >= N:
            return True

        for i in range(N):

            if isSafe(i, col):

                board[i][col] = 1
                
                if solveQueens(col + 1) == True:
                    return True

                board[i][col] = 0
                
        return False
    
    
    if solveQueens(0) == False:

        print("no solution")

        return False
    
    else:

        for i in range(N):

            for j in range(N):

                print(board[i][j], end=" ")
            
            print()

        return True


N = 4

solveNQueens(N)


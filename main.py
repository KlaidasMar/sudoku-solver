import numpy as np

def solve(board):
    # Find an empty cell
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                # Try every number from 1 to 9
                for k in range(1, 10):
                    # Check if the number is valid
                    if is_valid(board, i, j, k):
                        # Set the cell to the number
                        board[i][j] = k
                        # Try to solve the rest of the board
                        if solve(board):
                            return True
                        # If it's not possible to solve the board, reset the cell
                        board[i][j] = 0
                # If none of the numbers are valid, return False
                return False
    # If the board is full, it's solved
    return True

def is_valid(board, row, col, num):
    # Check if the number is in the row
    for i in range(9):
        if board[row][i] == num:
            return False
    # Check if the number is in the column
    for i in range(9):
        if board[i][col] == num:
            return False
    # Check if the number is in the 3x3 box
    box_row = row // 3
    box_col = col // 3
    for i in range(3):
        for j in range(3):
            if board[box_row * 3 + i][box_col * 3 + j] == num:
                return False
    # The number is not in the row, column, or box, so it's valid
    return True

def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=' ')
        print()

# Example board
board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

if solve(board):
    print_board(board)
else:
    print("No solution found")

# 8-Queens Problem using Backtracking

N = 8  # size of the chessboard (8x8)

def print_board(board):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print()

# Function to check if a queen can be placed at board[row][col]
def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

# Recursive function to solve N-Queens
def solve_nqueens(board, row):
    # Base case: all queens are placed
    if row == N:
        print("Final 8-Queens Solution:")
        print_board(board)
        return True

    # Try placing a queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen
            if solve_nqueens(board, row + 1):  # Recurse to next row
                return True
            board[row][col] = 0  # Backtrack

    return False

# Driver code
if __name__ == "__main__":
    # Initialize 8x8 chessboard with 0s
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Place the first Queen at (0,0)
    board[0][0] = 1

    # Start solving from the 2nd row (index 1)
    if not solve_nqueens(board, 1):
        print("No solution found!")

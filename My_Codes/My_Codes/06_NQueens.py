# N-Queens problem solution with first queen placed using backtracking

N = 4  # Define the size of the board

def printSolution(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))
    print()

def isSafe(board, row, col):
    # Check the current column on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower-left diagonal
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col):
    # Base case: if all queens are placed
    if col >= N:
        return True

    # Try placing a queen in each row in the current column
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1  # Place queen

            # Recur for the next column
            if solveNQUtil(board, col + 1):
                return True

            # Backtrack if placing queen here doesn't lead to a solution
            board[i][col] = 0

    return False

def solveNQ(first_row, first_col):
    # Initialize board with zeros
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    # Place the first queen at the specified position
    board[first_row][first_col] = 1

    # Start placing remaining queens from the next column
    if solveNQUtil(board, first_col + 1):
        printSolution(board)
    else:
        print("Solution does not exist.")

# Example usage:
# Place the first queen at position (0, 0)
solveNQ(0, 0)

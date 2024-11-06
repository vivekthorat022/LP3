def is_safe_position(board, row, col):
    # Check if placing a queen at (row, col) is safe
    for previous_row in range(row):
        # Check if there's a queen in the same column
        if board[previous_row] == col or \
           abs(board[previous_row] - col) == row - previous_row:  # Check diagonals
            return False  # Conflict found, position is not safe
    return True  # No conflicts, position is safe

def place_queens(board, row):
    # Base case: if all queens are placed (row == 8)
    if row == 8:
        print_board(board)  # Print the current board configuration
        return True  # Indicate that a solution has been found

    found_solution = False  # Flag to track if a solution has been found
    # Try placing a queen in each column for the current row
    for col in range(8):
        if is_safe_position(board, row, col):  # Check if the position is safe
            board[row] = col  # Place queen in the current row at column 'col'
            # Recursively attempt to place queens in the next row
            found_solution = place_queens(board, row + 1) or found_solution
            
            # Backtrack: remove the queen from the current position (not strictly necessary)
            board[row] = -1  # Reset the position (optional since we overwrite)

    return found_solution  # Return whether a solution was found

def print_board(board):
    print("   0 1 2 3 4 5 6 7")  # Print column headers for clarity
    print("  -----------------")  # Print a separator line for better readability
    for r in range(8):  # Iterate through each row of the board
        line = f"{r} |"  # Print the row index as a header
        for c in range(8):  # Iterate through each column in the current row
            if board[r] == c:  # Check if there's a queen in this column of the current row
                line += " Q"  # If yes, append 'Q' to represent the queen
            else:
                line += " ."   # If no queen, append '.' to represent an empty space
        print(line)  # Print the constructed line for this row
    print()  # Print a blank line between solutions for better separation

def solve_eight_queens():
    board = [-1] * 8  # Initialize the board with -1 (indicating no queens placed)
    board[0] = 0  # Place the first queen at position (0,0)
    place_queens(board, 1)  # Start placing queens from row index 1

solve_eight_queens()  # Call the function to solve the problem and display solutions
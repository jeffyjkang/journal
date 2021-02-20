# Sudoku Solver
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# Empty cells are indicated by the character 0.
# Note:
# The given board contain only digits 1-9 and the character 0.
# You may assume that the given Sudoku puzzle will have a single unique solution.
# The given board size is always 9x9.

def sudoku_solver(board):
    # initialize list variable l that will keep track of row and col
    l = [0, 0]
    # base case, if no empty cell on board, return True
    if not find_empty(board, l):
        return True
    # assign row and col value from the l mutation from above function
    row = l[0]
    col = l[1]
    # loop through num values 1 - 9
    for num in range(1, 10):
        # if check location function returns True with num, it is a valid input
        if check_location(board, row, col, num):
            # assign value of board at [row][col] to num
            board[row][col] = num
            # return true if valid
            if sudoku_solver(board):
                return True
            # if not valid, reassign the value of board [row][col] to empty
            board[row][col] = 0
    # trigger backtracking
    return False

# helper function to find empty location on the board
def find_empty(board, l):
    # loop through row indices 0 - 8
    for row in range(9):
        # loop through col indices 0 - 8
        for col in range(9):
            # if board value at [row][col] is empty
            if board[row][col] == 0:
                # assign the passed in list variable's 0 index to 'row' index
                l[0] = row
                # assign the passed in list variable's 1 index to 'col' index
                l[1] = col
                # return True
                return True
    # if no empty location is found on the board, return False
    return False

# helper function to check if value is already used in row
def check_row(board, row, num):
    # loop through row's indices 0 - 8
    for i in range(9):
        # if board value at [row][i] is equal to num, return True
        if board[row][i] == num:
            return True
    # if num is not found in the row return False
    return False

# helper function to check if value is already used in col
def check_col(board, col, num):
    # loop through col's indices 0 - 8
    for i in range(9):
        # if board value at [i][col] is equal to num, return True
        if board[i][col] == num:
            return True
    # if num is not found in the col return False
    return False

# helper function to check if value is already used in box
def check_box(board, row, col, num):
    # loop through i 0 - 2
    for i in range(3):
        # loop through j 0 - 2
        for j in range(3):
            # if board value at [i + row][j + col] is equal to num, return True
            if board[i + row][j + col] == num:
                return True
    # if num is not found in the box return False
    return False

# helper function to check if valid number can be placed in a location
def check_location(board, row, col, num):
    return (
        not check_row(board, row, num) and
        not check_col(board, col, num) and
        not check_box(board, row - row % 3, col - col % 3, num)
        )

b = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0 ,0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if(sudoku_solver(b)):
    print(b)
else:
    print('No Solution')

TAGS = ['BACKTRACK', '2D_ARRAY', 'SEARCH']

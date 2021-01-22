# Valid Sudoku
# Determine if a 9x9 Sudoku board is valid.
# Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# A partially filled sudoku which is valid.
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
# Example 1:
# Input:
# [
#     ['5','3','.','.','7','.','.','.','.'],
#     ['6','.','.','1','9','5','.','.','.'],
#     ['.','9','8','.','.','.','.','6','.'],
#     ['8','.','.','.','6','.','.','.','3'],
#     ['4','.','.','8','.','3','.','.','1'],
#     ['7','.','.','.','2','.','.','.','6'],
#     ['.','6','.','.','.','.','2','8','.'],
#     ['.','.','.','4','1','9','.','.','5'],
#     ['.','.','.','.','8','.','.','7','9']
# ]
# Output: true
# Example 2:
# Input:
# [
#     ['8','3','.','.','7','.','.','.','.'],
#     ['6','.','.','1','9','5','.','.','.'],
#     ['.','9','8','.','.','.','.','6','.'],
#     ['8','.','.','.','6','.','.','.','3'],
#     ['4','.','.','8','.','3','.','.','1'],
#     ['7','.','.','.','2','.','.','.','6'],
#     ['.','6','.','.','.','.','2','8','.'],
#     ['.','.','.','4','1','9','.','.','5'],
#     ['.','.','.','.','8','.','.','7','9']
# ]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8.
# Since there are two 8's in the top left 3x3 sub-box, it is invalid.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
# The given board contain only digits 1-9 and the character '.'.
# The given board size is always 9x9.

def is_valid_sudoku(board):
    # for 2d array, nested loop, outer loop range 9
    for i in range(9):
        # initialize row, col and box as sets
        row = set()
        col = set()
        box = set()
        # 2d array, inner loop range 9
        for j in range(9):
            # if value of board [i][j] is in row set, return false
            if board[i][j] in row:
                return False
            # if value of board [i][j] is not '.' add value to row set
            if board[i][j] !='.':
                row.add(board[i][j])
            # if value of board [j][i] is in col set, return false
            if board[j][i] in col:
                return False
            # if value of board [j][i] is not '.' add value to col set
            if board[j][i] !='.':
                col.add(board[j][i])
            # assign box row index
            box_row = 3 * (i // 3) + (j // 3)
            # assign box column index
            box_col = 3 * (i % 3) + (j % 3)
            # if value of board at [box_row][box_col] in box set, return false
            if board[box_row][box_col] in box:
                return False
            # if value of board at [box_row][box_col] is not '.' add value to box set
            if board[box_row][box_col] !='.':
                box.add(board[box_row][box_col])
    # after completed nested loop, return true
    return True

b = [
    ['5','3','.','.','7','.','.','.','.'],
    ['6','.','.','1','9','5','.','.','.'],
    ['.','9','8','.','.','.','.','6','.'],
    ['8','.','.','.','6','.','.','.','3'],
    ['4','.','.','8','.','3','.','.','1'],
    ['7','.','.','.','2','.','.','.','6'],
    ['.','6','.','.','.','.','2','8','.'],
    ['.','.','.','4','1','9','.','.','5'],
    ['.','.','.','.','8','.','.','7','9']
]

print(is_valid_sudoku(b))

TAGS = ['2D_ARRAY', 'SEARCH', 'MATCHING']

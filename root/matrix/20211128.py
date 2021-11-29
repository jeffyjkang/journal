# Rotate Image
# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).
# Note: You have to rotate the image in-place,
# which means you have to modify the input 2D matrix directly.
# Do not allocate another 2D matrix and do the rotation.
# Example 1:
# Given input matrix =
# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ],
# rotate the input matrix in-place such that it becomes:
# [
#     [7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]
# ]
# Example 2:
# Given input matrix =
# [
#     [5, 1, 9, 11],
#     [2, 4, 8, 10],
#     [13, 3, 6, 7],
#     [15, 14, 12, 16]
# ],
# rotate the input matrix in-place such that it becomes:
# [
#     [15, 13, 2, 5],
#     [14, 3, 4, 1],
#     [12, 6, 8, 9],
#     [16, 7, 10, 11]
# ]

def rotate_image(matrix):
    # initialize matrix length
    length = len(matrix)
    # loop through half of the matrix, due to swaps
    for i in range(length // 2):
        # nested loop will iterate from i to length of matrix - outer loop index
        for j in range(i, length - i - 1):
            # initialize a temp variable to hold current value
            temp = matrix[i][j]
            # first col from bot to top replaces first row from left to right
            matrix[i][j] = matrix[length - j - 1][i]
            # last row from right to left replaces first col from bot to top
            matrix[length - j -1][i] = matrix[length - i - 1][length - j - 1]
            # last col from top to bot replaces last row from right to left
            matrix[length - i - 1][length - j - 1] = matrix[j][length - i - 1]
            # first row from left to right replaces last col from top to bot
            matrix[j][length - i - 1] = temp
            # will move inwards in next i iteration
    # return matrix in-place
    return matrix

mat = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]

print(rotate_image(mat))

TAGS = ['MATRIX', 'LOOPS']

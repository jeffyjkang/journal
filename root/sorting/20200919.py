# Reverse Integer
# Given a 32-bit signed integer, reverse digits of an integer.
# Example 1:
# Input: 123
# Output: 321
# Example 2:
# Input: -123
# Output: -321
# Example 3:
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [-231, 231 -1].
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

# for overflow purposes
import sys
# sys.maxsize, -sys.maxsize-1

def reverse_int(x):
    # initialize the output as 0
    output = 0
    # continue while x does not equal 0
    while x != 0:
        # append the last digit of x to the output
        output = (output * 10) + (x % 10)
        # remove the last digit of x and drop any decimal
        x = int(x / 10)
    # check if output overflows and return 0 if it does
    if output > sys.maxsize or output < -sys.maxsize - 1:
        return 0
    # return output
    return output

i = 120
print(reverse_int(i))

TAGS = ['SORTING', 'REVERSE', 'NUMBERS']

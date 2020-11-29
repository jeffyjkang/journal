# Divide Two Integers
# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
# Return the quotient after dividing dividend by divisor.
# The integer division should truncate towards zero.
# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:
# Input: dividend = 7, divisor = -3
# Output: -2
# Note:
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [-231, 231 - 1].
# For the purpose of this probelm, assume that your function returns 231 - 1 when the division result overflows.

# for overflow purposes
import sys
# sys.maxsize, -sys.maxsize - 1

def divide(dividend, divisor):
    # if divisor is 0 return infinity(maxsize)
    if divisor == 0: return sys.maxsize
    # set sign to -1 if dividend xor (exclusive or) divisor is less than 0, else 1
    sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
    # reassign dividend and divisor to their respective absolute value
    dividend = abs(dividend); divisor = abs(divisor)
    # initialize a quotient variable to 0
    quotient = 0
    # loop while dividend is greator or equal to divisor
    while dividend >= divisor:
        # decrement dividend by the divisor
        dividend -= divisor
        # increment the quotient variable by 1
        quotient += 1
    # return sign * quotient
    if sign * quotient > sys.maxsize: return sys.maxsize
    if sign * quotient < -sys.maxsize - 1: return -sys.maxsize - 1
    return sign * quotient

top = 10
bot = -3

print(divide(top, bot))

TAGS = ['MATH', 'DIVISION']

# String To Integer(atoi)
# Implement atoi which converts astring to an integer.
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
# Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprest them as numerical value.
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
# If no valid conversion could be performed, a zero value is returned.
# Note:
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [-231, 231 -1].
# If the numerical value is out of the range of representable values, INT_MAX (231-1) or INT_MIN (-231) is returned.
# Example 1:
# Input: '42'
# Output: 42
# Example 2:
# Input: '   -42'
# Output: 42
# Explanation:
# The first non-whitespace character is '-', which is the minus sign.
# Then take as many numerical digits as possible, which gets 42.
# Example 3:
# Input: '4193 with words'
# Output: 4193
# Explanation:
# Conversion stops at digit '3' as the next character is not a numerical digit.
# Example 4:
# Input: 'words and 987'
# Output: 0
# Explanation:
# The first non-whitespace character is 'w', which is not a numerical digit or a +/- sign.
# Therefore no valid conversion could be performed.
# Example 5:
# Input: '-91283472332'
# Output: -2147483648
# Explanation:
# The number ' -91283472332' is out of the range of a 32-bit signed integer.
# Therefore INT_MIN (-231) is returned.

# for overflow purposes
import sys
# sys.maxsize, -sys.maxsize-1

def atoi(string):
    # edge case string length is 0
    if len(string) == 0:
        return 0
    # initialize answer to 0
    answer = 0
    # remove leading and trailing whitespace
    string = string.strip()
    # initialize is_negative to false
    is_negative = False
    # check for '-' or '+' at the begining of the string
    if string[0] == '-':
        # if starting char is '-', set is_negative to True, set string to the substring from index of 1
        is_negative = True
        string = string[1:]
    elif string[0] == '+':
        # if starting char is '+' set string to the substring from index of 1
        string = string[1:]
    # loop through string
    for s in string:
        # if s in string is a digit, modify answer's next ten's place, else break from the loop
        if s.isdigit():
            answer = answer * 10 + int(s)
        else:
            break
    # if is_negative is true, answer should be negative
    if is_negative: answer = answer * -1
    # if answer is greater than maxsize, return maxsize
    if answer > sys.maxsize: return sys.maxsize
    # if answer is less than minsize(-maxsize) return -maxsize
    if answer < -sys.maxsize -1: return -sys.maxsize -1
    # else return answer
    return answer

string = 'words and 987'
print(atoi(string))

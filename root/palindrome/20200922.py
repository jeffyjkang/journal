# Palindrome Number
# Determine whether an integer is a palindrome.
# An integer is a palindrome when it read the same backward as forward.
# Example 1:
# Input: 121
# Output: True
# Example 2:
# Input: -121
# Output: False
# Explanation: From left to right, it reads -121.
# From right to left, it becomes 121-.
# Therefore it is not a palindrome.
# Example 3:
# Input: 10
# Output: False
# Explanation: Reads 01 from right to left.
# Therefore it is not a palindrome.
# Follow up:
# Could you solve it without converting the integer to a string?

def is_palindrome(x):
    # edge case, if x is negative or when x ends in a 0 and is not 0 itself
    if x < 0 or (x % 10 == 0 and x != 0): return False
    # initialize reverted number to 0
    reverted_number = 0
    # loop while x is greater than reverted number
    while x > reverted_number:
        # reassign reverted number to the corresponding place value of x starting from the one's place backwards
        reverted_number = int((reverted_number * 10) + (x % 10))
        # reassign x by removing the one's place in each iteration
        x = int(x / 10)
    # if the starting number's overall length is odd we can ignore reverted number's last digit, return the boolean value of x is equal to reverted number
    return x == reverted_number or x == int(reverted_number / 10)

num = 12321
print(is_palindrome(num))

TAGS = ['PALINDROME', 'NUMBERS']

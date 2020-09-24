# Longest Palindromic Substring
# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.
# Example 1:
# Input: 'babad'
# Output: 'bab'
# Note: 'aba' is also a valid answer.
# Example 2:
# Input: 'cbbd'
# Output: 'bb'

def longest_palindrome(s):
    # edge case, return '' when string is empty
    if s == '':
        return ''
    # initialize start and end to 0
    start = 0; end = 0
    # loop through the length of the string
    for i in range(len(s)):
        # assign len_1 to the result of calling expand_around_center passing in the string, index and index; optimizes for odd length palindrome
        len_1 = expand_around_center(s, i, i)
        # assign len_2 to the result of calling expand_around_center passing in the string, index and index + 1; optimizes for even length palindrome
        len_2 = expand_around_center(s, i, i + 1)
        # assign len_max to the max between len_1 and len_2
        len_max = max(len_1, len_2)
        # if we have found a new max length
        if len_max > end - start:
            # assign start index to current index - half the length of the palindrome
            start = i - int((len_max - 1) / 2)
            # assign end index to current index + half the length of the palindrome
            end = i + int(len_max / 2)
    # return the substring from start to end + 1
    return s[start : end + 1]

def expand_around_center(s, left, right):
    # L and R will track left and right indexes respectively
    L = left; R = right
    # continue while L is greater than or equal to 0, R is less than the length of the string, and the value at index L is equal to the value at index R
    while (L >= 0 and R < len(s)) and s[L] == s[R]:
        # decrement L index, increment R index
        L -= 1; R += 1
    # return the length of the palindrome: R - L - 1
    return R - L - 1

string = 'badaadaxyz'
print(longest_palindrome(string))

TAGS = ['PALINDROME', 'SUBSTRING']

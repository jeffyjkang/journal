# Implement strStr()
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Example 1:
# Input: haystack = 'hello', needle = 'll'
# Output: 2
# Example 2:
# Input: haystack = 'aaaaa', needle = 'bba'
# Output: -1
# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0. This is consistent to C's strstr() and Java's indexOf().

def str_Str(h, n):
    # edge case when needle is empty string, return 0
    if len(n) == 0:
        return 0
    # loop from 0 to the length of haystack minus length of needle + 1, (+ 1 is necessary for when haystack and needle are same)
    for i in range(len(h) - len(n) + 1):
        # if the value of haystack from index i to i + the length of needle is needle
        if h[i: i + len(n)] == n:
            # return the index, match found
            return i
    # if the loop completes and no index is found, return -1
    return -1

haystack = 'hello'
needle = 'll'

print(str_Str(haystack, needle))

TAGS = ['SEARCH']
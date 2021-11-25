# Wildcard Matching
# Given an input string (s) and a pattern (p),
# Implement wildcard pattern matching with support for '?' and '*'.
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
# Note:
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like ? or *.
# Example 1:
# Input:
# s = 'aa'
# p = 'a'
# Output: false
# Explanation: 'a' does not match the entire string 'aa'.
# Example 2:
# Input:
# s = 'aa'
# p = '*'
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:
# Input:
# s = 'cb'
# p = '?a'
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
# Example 4:
# Input:
# s = 'adceb'
# p = '*a*b'
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring 'dce'.
# Example 5:
# Input:
# s = 'acdcb'
# p = 'a*c?b'
# Output: false

def wildcard_matching(s, p):
    # if both string and pattern are empty, matches, return true
    if not s and not p:
        return True
    # if only one string or pattern are empty, no match, return false
    if not s or not p:
        return False
    # assign string length and pattern length
    s_len = len(s); p_len = len(p);
    # initialize lookup table to false values, which will be updated
    lookup = [[False for i in range(p_len + 1)] for j in range(s_len + 1)]
    # initialize lookup start as true
    lookup[0][0] = True
    # loop through from 1 to length of pattern + 1
    for i in range(1, p_len + 1):
        # if value at pattern is * match including empty string
        if p[i - 1] == '*':
            lookup[0][i] = lookup[0][i - 1]
    # loop through from 1 to length of string + 1
    for i in range(1, s_len + 1):
        # nested loop from 1 to length of pattern + 1
        for j in range(1, p_len + 1):
            # if pattern is * ignore and move on to next character
            # or * character matches with ith character
            if p[j - 1] == '*':
                lookup[i][j] = lookup[i][j - 1] or lookup[i - 1][j]
            # if pattern is ? or characters match
            elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1]
            # characters do not match
            else:
                lookup[i][j] = False
    # return
    return lookup[s_len][p_len]          

string = 'adceb'
pattern = '*a*b'

print(wildcard_matching(string, pattern))

TAGS = ['2D_ARRAY', 'SEARCH', 'MATCHING']

# Regular Expression Matching
# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not plural).
# Note:
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.
# Example 1:
# Input:
# s = 'aa'
# p = 'a'
# Output: False
# Explanation: 'a' does not match the entire string 'aa'.
# Example 2:
# Input:
# s = 'aa'
# p = 'a*'
# Output: True
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes 'aa'.
# Example 3:
# Input:
# s = 'ab'
# p = '.*'
# Output: True
# Explanation: '.*' means zero or more (*) of any character (.).
# Example 4:
# Input:
# s = 'aab'
# p = 'c*a*b'
# Output: True
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches 'aab'.
# Example 5:
# Input:
# s = 'mississippi'
# p = 'mis*is*p*.'
# Output: False

def is_match(text, pattern):
    # base case if pattern is empty return opposite of text
    if not pattern: return not text
    # assign first match to the boolean value of bool(text) and resulting comparison of value of pattern at index of 0 and value of text at index of 0
    # or if the value at pattern at index of 0 is '.'
    first_match = text and pattern[0] == text[0] or pattern[0] == '.'
    # if the length of current pattern is greater than or equal to 2 and the value of pattern at index of 1 is '*'
    if len(pattern) >= 2 and pattern[1] == '*':
        # if there is a substring after the '*', recursively call is_match with arguments text and the substring of pattern from index 2
        # else if first_match resolves to true, recursively call is_match with arguments of the substring of text from index 1 and pattern, else return False
        return is_match(text, pattern[2:]) or first_match and is_match(text[1:], pattern)
    # else if first_match resolves to true, recursively call is_match with arguments substring text from index 1 and substring pattern from index 1, else return False
    else:
        return first_match and is_match(text[1:], pattern[1:])

# t = 'aa'
# p = 'a'
# t = 'aa'
# p = 'a*'
# t = 'ab'
# p = '.*'
# t = 'aab'
# p = 'c*a*b'
t = 'mississippi'
p = 'mis*is*p*.'

print(is_match(t, p))

TAGS = ['REGEX', 'RECURSSION']

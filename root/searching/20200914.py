# Longest Substring Without Repeating Characters
# Given a string, find th length of the longest substring without repeating characters.
# Example 1:
# Input: 'abcabcbb'
# Output: 3
# Explanation: The answer is 'abc', with the length of 3.
# Example 2:
# Input: 'bbbbb'
# Output: 1
# Explanation: The answer is 'b', with the length of 1.
# Example 3:
# Input: 'pwwkew'
# Output:  3
# Explanation: The answer is 'wke', with the length of 3.
# Note that the answer must be a substring, 'pwke' is a subsequence not a substring.

def get_longest(string):
    # initialize a variable to hold the answer
    answer = 0
    # initialize a variable to hold the start of the non repeating string
    i = 0
    # create a dictionary to hold key value pairs of letter and most recent index
    curI = {}
    # loop through the string
    for j in range(len(string)):
        # if current letter is already in the dictionary:
        if string[j] in curI:
            # assign i to the greater of i or last index of current letter, this is in consideration of contiguous letters
            i = max(curI[string[j]], i)
        # update the answer to the difference between i and j, plus 1 for initial letter, if answer is less
        answer = max(answer, j - i + 1)
        # assign current letter as key and current index plus 1 in consideration of initial letter
        curI[string[j]] = j + 1
    # return answer
    return print(answer)

fullstring = 'pwewkeweesowie'
get_longest(fullstring)

TAGS = ['SEARCH', 'SUBSTRING']

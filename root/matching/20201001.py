# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: ["flower", "flow", "flight"]
# Output: "fl"
# Example 2:
# Input: ["dog", "racecar", "car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note: All given inputs are in lowercase letters a-z.

def longest_common_prefix(strings):
    # edge case if strings list is empty, return empty string
    if len(strings) == 0: return ''
    # initialize longest common prefix to the value of strings at index 0
    l_c_p = strings[0]
    # loop through the indices of each string beginning with index 1
    for i in range(1, len(strings)):
        # initialize current match to an empty string
        current_match = ''
        # if the newly assigned l_c_p is an empty string, break, no need to check further
        if len(l_c_p) == 0:
            break
        # loop through each character index of the current string
        for j in range(len(strings[i])):
            # if the current character index is less than the length of l_c_p and the values at specified index are the same
            if j < len(l_c_p) and l_c_p[j] == strings[i][j]:
                # reassign the current match to the current match substring and the value of l_c_p at index j
                current_match += l_c_p[j]
            # else break
            else:
                break
        # reassign l_c_p to the current match substring
        l_c_p = current_match
    # return the longest common prefix
    return l_c_p

s = ['flower', 'flow', 'flight']
# s = ['dog', 'racecar', 'car']

print(longest_common_prefix(s))

TAGS = ['SUBSTRING', 'HORIZONTAL_SCANNING', 'MATCHING']

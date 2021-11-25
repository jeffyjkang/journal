# Permutations
# Given a collection of distinct integers,
# return all possible permutations.
# Example:
# Input: [1, 2, 3]
# Output:
# [
#   [1, 2, 3],
#   [1, 3, 2],
#   [2, 1, 3],
#   [2, 3, 1],
#   [3, 1, 2],
#   [3, 2, 1]
# ]

def permutations(lst):
    # edged case for length of 0
    if len(lst) == 0:
        return []
    # base case for length of 1
    if len(lst) == 1:
        return [lst]
    # initialize an empty list to store current permutation
    l = []
    # loop through list
    for i in range(len(lst)):
        # grab values from i to end of list and assign in to remaining list
        rem_lst = lst[:i] + lst[i + 1 :]
        # recursively call permutations with the remaining list
        for j in permutations(rem_lst):
            # append  value to each iteration
            l.append([lst[i]] + j)
    # return results list
    return l

print(permutations([1, 2, 3]))

TAGS = ['RECURSION', 'PERMUTATIONS']

# Permutations II
# Given a collection of numbers that might contain duplicates,
# return all possible unique permutations.
# Example:
# Input: [1, 1, 2]
# Output:
# [
#     [1, 1, 2],
#     [1, 2, 1],
#     [2, 1, 1]
# ]

def backtrack(res, lst, perm, vis):
    # base case, if length of permutations is length of list
    # and the permutation is not in the results list
    if len(perm) == len(lst) and perm not in res:
        # append the permutation to the results and return
        res.append(list(perm))
        return
    # loop through the list
    for i in range(len(lst)):
        if i in vis:
            continue
        # append value of list at index of i to permutation list
        perm.append(lst[i])
        # add i to visited set
        vis.add(i)
        # recursively call backtrack, pass in results, the list, the current permutation, and visited
        backtrack(res, lst, perm, vis)
        # pop the value from permutation
        perm.pop()
        # remove i to visited set
        vis.remove(i)

def permutations_ii(arr):
    # initialize empty list for results
    results = []
    # initialize empty set for visited
    visited = set()
    # backtrack helper function
    backtrack(results, arr, [], visited)
    # return results
    return results

print(permutations_ii([1, 1, 2]))

TAGS = ['RECURSION', 'PERMUTATIONS', 'BACKTRACK']

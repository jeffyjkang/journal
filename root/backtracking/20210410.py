# Combination Sum
# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sums to target.
# The same repeated number may be chosen from candidates unlimited number of times.
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
# Input: candidates = [2, 3, 6, 7], target = 7,
# A solution set is:
# [
#     [7],
#     [2, 2, 3]
# ]
# Example 2:
# Input: candidates = [2, 3, 5], target = 8,
# A solution set is:
# [
#     [2, 2, 2, 2],
#     [2, 3, 3],
#     [3, 5]
# ]

def combination_sum(candidates, target):
    # initialize results array and temp array to empty lists
    res = []; temp = []
    # reassign candidates to a sorted list with unique elements
    candidates = sorted(list(set(candidates)))
    # call helper function passing in res, temp, the candidates array, target and index = 0
    find_numbers(res, temp, candidates, target, 0)
    # after the recursion of find_numbers complete return results
    return res

# helper function for recursion
def find_numbers(res, temp, candidates, target, index):
    # base case, if target equals 0, append the deep copy of temp to the results array and return
    if target == 0:
        res.append(list(temp))
        return
    # iterate from index to remaining indices of candidates
    for i in range(index, len(candidates)):
        # if the result of target - candidates at index of i is greater or equal to 0:
        if target - candidates[i] >= 0:
            # append the value of candidates at index of i to the temp array
            temp.append(candidates[i])
            # recursively call find_numbers passing in res, temp, candidates, the difference of target and the value of candidates at index i and i
            find_numbers(res, temp, candidates, target - candidates[i], i)
            # remove the value of candidates at index of i from the temp array (backtracking)
            temp.remove(candidates[i])

candidates = [2, 3, 5]
target = 8

print(combination_sum(candidates, target))

TAGS = ['SEARCH', 'RECURSION', 'BACKTRACK']

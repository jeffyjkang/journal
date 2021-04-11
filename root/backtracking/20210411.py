# Combination Sum II
# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sums to target.
# Each number in candidates may only be used once in the combination.
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
# Input: candidates = [10, 1, 2, 7, 6, 1, 5], target = 8,
# A solution set is:
# [
#     [1, 7],
#     [1, 2, 5],
#     [2, 6],
#     [1, 1, 6]
# ]
# Example 2:
# Input: candidates = [2, 5, 2, 1, 2], target = 5,
# A solution set is:
# [
#     [1, 2, 2],
#     [5]
# ]

def combination_sum_ii(candidates, target):
    # initialize results array and temp array to empty lists
    res = []; temp = []
    # reassign candidates to its sorted version
    candidates = sorted(candidates)
    # call helper function passing in res, temp, the candidates array, target and index = 0
    find_numbers(res, temp, candidates, target, 0)
    # after the recursion of find_numbers complete return results
    return res


def find_numbers(res, temp, candidates, target, index):
    # base case, if target equals 0, append the deep copy of temp to the results array
    if target == 0:
        res.append(list(temp))
    # assign prev value to 0
    prev = 0
    # iterate while index is less than the length of candidates and the value of candidates at index is less than or equal to target
    while index < len(candidates) and candidates[index] <= target:
        # if prev value does not equal value of candidates at index, continue
        if prev != candidates[index]:
            # append the value of candidates at index to the temp array
            temp.append(candidates[index])
            # recursively call find_numbers passing in res, temp, candidates, the difference of target and value of candidates and index, and index + 1
            find_numbers(res, temp, candidates, target - candidates[index], index + 1)
            # remove the value of candidates at index from temp array (backtracking)
            temp.remove(candidates[index])
            # reassign previous value to the value of candidates at index
            prev = candidates[index]
        # increment index by 1
        index += 1


candidates = [2, 5, 2, 1, 2]
target = 5

print(combination_sum_ii(candidates, target))

TAGS = ['SEARCH', 'RECURSION', 'BACKTRACK']

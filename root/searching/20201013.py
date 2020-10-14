# Four Sum
# Given an array nums of n integers and an integer target,
# are there three elements a, b, c, and d in nums such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.
# Note:
# The solution set must not contain duplicate quadruplets.
# Example:
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# A solution set is:
# [
#     [-1, 0, 0, 1],
#     [-2, -1, 1, 2],
#     [-2, 0, 0, 2]
# ]

def four_sum(nums, target):
    # edge case, if the length of nums is less than 4, return None
    if len(nums) < 4: return None
    # sort the nums list (python: timsort)
    nums.sort()
    # initialize result list to an empty list
    result_list = []
    # loop through each index until the fourth to last
    for i in range(len(nums) - 3):
        # if i index is greater than 0 and the value is the same as the previous, skip iteration, this prevents duplicates on the 0th indices
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # loop through each index from after i until the third to last
        for j in range(i+1, len(nums) - 2):
            # again skip iteration to prevent duplicates, however check if j index is greater than i index plus 1 and the value is the same as the previous
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            # assign new target variable to the difference of target and the values at indices i and j
            new_target = target - nums[i] - nums[j]
            # assign left pointer to index j plus 1
            l = j + 1
            # assign right pointer to the last index
            r = len(nums) - 1
            # loop while left pointer is less than right pointer
            while l < r:
                # if left pointer is greater than j pointer plus 1, and the values of left pointer and left pointer minus 1 are equal
                if l > j + 1 and nums[l] == nums[l - 1]:
                    # increment left pointer and skip iteration to prevent duplicates
                    l += 1
                    continue
                # if right pointer is less than last index, and the values of right pointer and right pointer plus 1 are equal
                if r < len(nums) - 1 and nums[r] == nums[r + 1]:
                    # decrement right pointer and skip iteration to prevent duplicates
                    r -= 1
                    continue
                # initialize sum to the values of nums at index left pointer and right pointer
                sum = nums[l] + nums[r]
                # if sum is less than new_target, increment l by 1
                if sum < new_target: l += 1
                # else if sum is greater than new_target, decrement r by 1
                elif sum > new_target: r -= 1
                # else if sum equals new_target, append the list of values to the result list, increment l, and decrement r each by 1
                else:
                    result_list.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    r -= 1
    # return the result list
    return result_list


n = [1, 0, -1, 0, -2, 2]
t = 0

print(four_sum(n, t))

TAGS = ['SEARCH', 'SUM']

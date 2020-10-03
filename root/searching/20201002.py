# Three Sum
# Given an array of nums of n integers.
# Are there elements a, b, c in nums such that a + b + c = 0 ?
# Find all unique triplets in the array which gives the sum of zero.
# Note:
# The solution set must not contain duplicate triplets.
# Example:
# Given array nums = [-1, 0, 1, 2, -1, -4],
# A solution set is:
# [
#     [-1, 0, 1],
#     [-1, -1, 2]
# ]

def three_sum(nums):
    # edge case, if the length of nums is less than 3, return an empty list
    if len(nums) < 3: return []
    # sort the nums list (python: timsort)
    nums.sort()
    # initialize result list to an empty list
    result_list = []
    # loop through each index until the third to last
    for i in range(len(nums) - 2):
        # if index is greater than 0 and the value is the same as the previous, skip iteration, this prevents duplicates on the 0th indices
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # assign left pointer to index plus 1
        l = i + 1
        # assign right pointer to the last index
        r = len(nums) - 1
        # loop while left pointer is less than right pointer
        while l < r:
            # initialize sum to values of nums at index i, l, and r
            sum = nums[i] + nums[l] + nums[r]
            # if the sum is less than target, increase l index by 1
            if sum < 0:
                l += 1
            # else if sum is greater than target, decrease r index by 1
            elif sum > 0:
                r -= 1
            # else if l < r and sum is correct
            else:
                # append the current list of numbers to the result list, and make sure there are no duplicates
                result_list.append([nums[i], nums[l], nums[r]])
                # loop while l is less than length of nums minus 1 and the value of nums at l is equal to the value of nums at l plus 1
                while l < len(nums) - 1 and nums[l] == nums[l + 1]:
                    # increment the l index by 1
                    l += 1
                # loop while r is greater than 0 and the value of nums at index r is equal to the value of nums at index r minus 1
                while r > 0 and nums[r] == nums[r - 1]:
                    # decrement the r index by 1
                    r -= 1
                # increment l, decrement r
                l += 1
                r -= 1
    # return the result list
    return result_list

n = [-1, 0, 1, 2, -1, -4]
# n = [1, 1, 0, 0, 0, 1, 1]
# t = 0
# print(three_sum(n, t))
print(three_sum(n))

TAGS = ['SEARCH', 'SUM']

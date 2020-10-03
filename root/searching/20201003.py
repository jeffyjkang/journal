# Three Sum Closest
# Given an array nums of n integers and an integer target,
# find three integers in nums such that the sum is closest to target.
# Return the sum of three integers.
# You may assume that each input would have exactly one solution.
# Example:
# Given array nums = [-1, 2, 1, -4] and target = 1.
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

def three_sum_closest(nums, target):
    # edge case, if the length of nums is less than 3, return None
    if len(nums) < 3: return None
    # sort the nums list (python: timsort)
    nums.sort()
    # initialize closest variable to the sum of the values of the first 3 indices of nums
    closest = sum(nums[:3])
    # loop through each index until the third to last
    for i in range(len(nums) - 2):
        # assign left pointer to index plus 1
        l = i + 1
        # assign right pointer to the last index
        r = len(nums) - 1
        # loop while left pointer is less than right pointer
        while l < r:
            # initialize sum to values of nums at index i, l, and r
            cur_sum = nums[i] + nums[l] + nums[r]
            # if the absolute value from the difference of target and current sum is less than the absolute value from the difference of target and closest
            if abs(target - cur_sum) < abs(target - closest):
                # reassign closest to the current sum
                closest = cur_sum
                # if closest equals target, return closest
                if closest == target: return closest
            # if current sum is greater than target, decrement the r pointer index
            if cur_sum > target:
                r -= 1
            # if the current sum is less than the target, increment the l pointer index
            else:
                l += 1
    # return closest integer variable
    return closest

n = [-1, 2, 1, -4]
t = 1
print(three_sum_closest(n, t))

TAGS = ['SEARCH', 'SUM']
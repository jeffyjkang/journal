# Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# because nums[0] + nums[1] = 2 + 7 = 9
# return [0, 1]

def two_sum(nums, target):
    # create a dict to hold potential compliments and their indices
    possibilities = {}
    # loop through the indices of the numbers
    for i in range(len(nums)):
        # define the complement as the difference between the target value and the current value in the loop
        compliment = target - nums[i]
        # if the compliment key is in the possibilities dict, return the key of the compliment, which would be compliment's index and the current index of the loop
        if compliment in possibilities:
            return print([possibilities[compliment], i])
        # add key value pair into possibilities dict with the complement as the key and index as the value
        possibilities[nums[i]] = i
    # if no two numbers sum to the target value, log it
    return print("No two sum solution.")

nums = [2, 7, 11, 15]
target = 9
two_sum(nums,target)

# Remove Duplicates From Sorted Array
# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# Example 1:
# Given nums = [1, 1, 2],
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the returned length.
# Example 2:
# Given nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
# It doesn't matter what values are set beyond the returned length.
# Clarification:
# Confused why the returned value is an integer but your answer is an array?
# Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
# Internally you can think of this:
# nums is passed by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums):
# any modification to nums in your function would be known by the caller.
# using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }

def remove_duplicates(nums):
    # edge case, return 0 if the length of the list is 0
    if len(nums) == 0: return 0
    # initialize i index to 0
    i = 0
    # loop through nums indices, indicated by j index
    for j in range(1, len(nums)):
        # if the value of nums at index of i is not equal to the value of nums at index of j
        if nums[i] != nums[j]:
            # increment i by 1, assign the value of nums at index of i to the value of nums at index of j which is the current iteration
            i += 1
            nums[i] = nums[j]
    print(nums)
    # return i plus 1 for the length
    return i + 1

n = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

print(remove_duplicates(n))

TAGS = ['REMOVE', 'SEARCH']

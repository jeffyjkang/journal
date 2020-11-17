# Remove Element
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
# Example 1:
# Given nums = [3, 2, 2, 3], val = 3,
# Your function should return length = 2, with the first two elements of nums being 2.
# It doesn't matter what you leave beyond the returned length.
# Example 2:
# Given nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2,
# Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
# Note that the order of those five elements can be arbitrary.
# It doesn't matter what values are set beyond the returned length.
# Clarification:
# Confused why the returned value is an integer but your answer is an array?
# Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
# Internally you can think of this:
# nums is passed in by reference. (i.e., without making a copy)
# int len = removeElement(nums, val);
# any modification to nums in your function would be known by the caller.
# using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }

def remove_element(nums, el):
    # initialize i index to 0 and n index to the length of nums
    i = 0; n = len(nums)
    # loop while i is less than n
    while i < n:
        # if the value of nums at index i is equal to the element
        if nums[i] == el:
            # reassign the value to the value at n - 1
            nums[i] = nums[n-1]
            # decrement the n pointer
            n -= 1
        # else if the value of nums at index i does not equal the element, increment the i pointer
        else:
            i += 1
    # return the value of n
    return n
    # if there is a likelyhood that there are more elements to remove, less costly version;
    # skips action if the value at current iteration is equal to the element
    # i = 0
    # for j in range(0, len(nums)):
    #     if nums[j] != el:
    #         nums[i] = nums[j]
    #         i += 1
    # return i

n = [0, 1, 2, 2, 3, 0, 4, 2]
e = 2

print(remove_element(n, e))

TAGS = ['REMOVE', 'SEARCH']

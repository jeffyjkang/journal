# Find First And Last Position Of Element In Sorted Array
# Given an array of integers nums sorted in ascending order,
# find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].
# Example 1:
# Input: nums = [5, 7, 7, 8, 8, 10], target = 8
# Output: [3, 4]
# Example 2:
# Input: nums = [5, 7, 7, 8, 8, 10], target = 6
# Output: [-1, -1]

def find_first_last(n, t):
    # assign first_index and last_index to the return of find_first and find_last respectively,
    # pass in the numbers list, 0 for low, length of list -1 for high, target, and length of list
    first_index = find_first(n, 0, len(n) - 1, t, len(n))
    last_index = find_last(n, 0, len(n) - 1, t, len(n))
    # return the indices
    return [first_index, last_index]

# helper function to find first index
def find_first(list, low, high, target, length):
    # iterate if low is less than or equal to high
    if low <= high:
        # assign mid to the sum of low and the floored quotient of (the difference of high and low and 2)
        mid = low + (high - low) // 2
        # base case, if mid is 0 or target is greater than the value of list at index mid - 1,
        # and target is found, return mid
        if (mid == 0 or target > list[mid - 1]) and list[mid] == target:
            return mid
        # if target is not found but is greater than the value at mid:
        elif target > list[mid]:
            # recursively call find_first, with mid + 1 as low
            return find_first(list, mid + 1, high, target, length)
        # else, if target is not found and is less than the value at mid:
        else:
            # recursively call find_first with mid - 1 as high
            return find_first(list, low, mid - 1, target, length)
    # if iterations pass and target is not found, return -1
    return -1

# helper function to find last index
def find_last(list, low, high, target, length):
    # iterate if low is less than or equal to high
    if low <= high:
        # assign mid to the sum of low and the floored quotient of (the difference of high and low and 2)
        mid = low + (high - low) // 2
        # base case, if mid is length of list - 1 or target is less than the value of list at index mid + 1,
        # and target is found return mid
        if (mid == length - 1 or target < list[mid + 1]) and list[mid] == target:
            return mid
        # if target is not found but is less than the value at mid:
        elif target < list[mid]:
            # recursively call find_last, with mid - 1 as high
            return find_last(list, low, mid - 1, target, length)
        # else, if target is not found and is greater than value at mid
        else:
            # recursively call find_last, with mid + 1 as low
            return find_last(list, mid + 1, high, target, length)
    # if iterations pass and target is not found, return -1
    return -1


nums = [5, 7, 7, 8, 8, 10]
target = 8

print(find_first_last(nums, target))

TAGS = ['BINARY_SEARCH']

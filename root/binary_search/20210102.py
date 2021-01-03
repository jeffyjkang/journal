# Search In Rotated Sorted Array
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0, 1, 2, 4, 5 ,6, 7] might become [4, 5, 6, 7, 0, 1, 2]).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# Your algorithm's runtime complexity must be in the order of O(log n).
# Example 1:
# Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
# Output: -1

def search(n, t):
    # initialize lo and hi pointers to index 0, and length of n - 1
    lo = 0; hi = len(n) - 1
    # loop while lo is less than or equal to hi, lo and hi will be modified through a binary search pattern
    while lo <= hi:
        # assign a mid pointer to the floored quotient of (the sum of lo and the difference of hi and lo), and 2
        mid = lo + (hi - lo) // 2
        # if the target is found via the value of n at index mid, return the index
        if n[mid] == t:
            return mid
        # if the value of n at index lo is less than or equal to the value of n at index mid, sub-array is sorted:
        if n[lo] <= n[mid]:
            # if target is less than the value of n at index mid and target is greater than or equal to the value of n at index lo,
            # target is inside the sub-array, reassign hi to mid - 1
            if t < n[mid] and t >= n[lo]:
                hi = mid - 1
            # else, target is not inside the sub-array, reassign lo ot mid + 1
            else:
                lo = mid + 1
        # if the value of n at index mid is less than or equal to the value of n at index hi, sub-array is sorted:
        if n[mid] <= n[hi]:
            # if target is greater than the value of n at index mid and target is less than or equal to the value of n at index hi,
            # target is inside the sub-array, reassign lo to mid + 1
            if t > n[mid] and t <= n[hi]:
                lo = mid + 1
            # else, target is not inside the sub-array, reassign hi to mid - 1
            else:
                hi = mid -1
    # if not returned by end of loop, target not found, return -1
    return -1

nums = [4, 5, 6, 7, 0, 1, 2]
target = 4

print(search(nums, target))

TAGS = ['BINARY_SEARCH', 'SEARCH']

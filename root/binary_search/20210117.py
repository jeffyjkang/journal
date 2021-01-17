# Search Insert Position
# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.
# Example 1:
# Input: [1, 3, 5, 6], 5
# Output: 2
# Example 2:
# Input: [1, 3, 5, 6], 2
# Output: 1
# Example 3:
# Input: [1, 3, 5, 6], 7
# Output: 4
# Example 4:
# Input: [1, 3, 5, 6], 0
# Output: 0

def find_index(arr, t):
    # initialize left pointer to 0
    left = 0
    # initialize right pointer to the last index of the array
    right = len(arr) - 1
    # loop while left pointer is less than or equal to right pointer
    while left <= right:
        # assign mid pointer to the floor of the quotient of (sum left and right) and 2
        mid = (left + right) // 2
        # if the array at index mid equals target return mid
        if arr[mid] == t:
            return mid
        # if array at mid is less than target, reassign left to mid + 1
        elif arr[mid] < t:
            left = mid + 1
        # if array at mid is greater than target, reassign right to mid - 1
        else:
            right = mid - 1
    # if target is not found after iterations, return right + 1 or insert position
    return right + 1

array = [1, 3, 5, 6]
target = 0

print(find_index(array, target))

TAGS = ['BINARY_SEARCH', 'SEARCH']

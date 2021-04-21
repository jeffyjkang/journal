# First Missing Positive
# Given an unsorted integer array, find the smallest missing positive integer.
# Example 1:
# Input: [1, 2, 0]
# Output: 3
# Example 2:
# Input: [3, 4, -1, 1]
# Output: 2
# Example 3:
# Input: [7, 8, 9, 11, 12]
# Output: 1
# Note:
# Your algorithm should run in O(n) time and uses constant extra space.

def first_missing_positive(n):
    # initialize a check variable to 0
    check = 0
    # loop through numbers array and check if element 1 exists
    for i in range(len(n)):
        # if element 1 exists, reassign check to 1 and break
        if n[i] == 1:
            check = 1
            break
    # if check remains 0 after the first loop completes, return 1, element 1 was not found
    if check == 0:
        return(1)
    # loop through numbers array again
    for i in range(len(n)):
        # if the value of element at index is less than 0 or greater than the size of the array
        if n[i] <= 0 or n[i] > len(n):
            # assign the value of element at index to 1
            n[i] = 1
    # loop through numbers array again
    for i in range(len(n)):
        # for every ith number increase the value of n at index n[i] - 1 by the length of the numbers array
        n[(n[i] - 1) % len(n)] += len(n)
    # loop through the numbers array a final time
    for i in range(len(n)):
        # if the value of element at index is less than the size of the array
        if n[i] <= len(n):
            # return i + 1
            return i + 1
    # after the loops, and no min value is found, return size of array + 1
    return len(n) + 1

# numbers = [7, 8, 9, 11, 12]
# numbers = [1, 2, 3]
numbers = [3, 4, -1, 1]

print(first_missing_positive(numbers))

TAGS = ['SEARCH']

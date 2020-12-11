# Next Permutation
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such an arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place and use only constant extra memory.
# Here are some examples. Inputs are in the left-handed column and its corresponding outputs are in the right-hand column.
# 1, 2, 3 -> 1, 3, 2
# 3, 2, 1 -> 1, 2, 3
# 1, 1, 5 -> 1, 5, 1

def next_permutation(n):
    # initialize a false flag to false
    found = False
    # initialize index to length of the numbers list minus 2 (starting at the 2nd to last index in the list to compare)
    i = len(n) - 2
    # loop while i is greater than or equal to 0
    while i >= 0:
        # if the value of n at index i is less than the value of n at index i + 1, a rearrangement is possible
        if n[i] < n[i+1]:
            # set the flag to true and break the loop
            found = True
            break
        # decrement i by 1
        i -= 1
    # if no rearrangement is possible, sort the list in ascending order
    if not found:
        n.sort()
    else:
        # assign max index by calling the helper function passing in i + 1, the list and the value at index i
        # the helper function will return the next greater value after index i, starting the iterations at i + 1
        max_index = find_max_index(i + 1, n, n[i])
        # swap the value at max index with the value at i
        n[i], n[max_index] = n[max_index], n[i]
        # reassign the list from index i+1 to the list from index i+1 but in reverse
        n[i+1:] = n[i+1:][::-1]
    # return the next permutated list
    return n

# helper function
def find_max_index(index, numbers, val):
    # loop from indices i + 1 to the last index in the numbers list
    for i in range(index, len(numbers)):
        # if the value at i is greater than the passed in value, reassign index to i
        if numbers[i] > val:
            index = i
    # return index of next greater value
    return index

nums = [1, 4, 2, 6, 5, 2]

print(next_permutation(nums))

TAGS = ['PERMUTATIONS', 'SEARCH']

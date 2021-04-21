# Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.
# Example:
# Input: [0, 1, 0,  2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6

def trapping_rain_water(n):
    # initialize left pointer to 0, right pointer to last index of array
    left = 0; right = len(n) - 1
    # initialize a max left and max right value to 0
    l_max = 0; r_max = 0
    # initialize results to 0
    res = 0
    # iterate while left pointer is less than or equal to right pointer
    while left <= right:
        # if max right value is less than or equal to max left value:
        if r_max <= l_max:
            # increase result value by the difference of max right and value of n at index right, if positive
            res += max(0, r_max - n[right])
            # update max right to value of n at index right, if bigger
            r_max = max(r_max, n[right])
            # decrement right pointer
            right -= 1
        # if max right value is greater than max left value:
        else:
            # increase results value by the difference of max left and value of n at index left, if positive
            res += max(0, l_max - n[left])
            # update max left to value of n at index left, if bigger
            l_max = max(l_max, n[left])
            # increment left pointer
            left += 1
    # return result
    return res

numbers = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trapping_rain_water(numbers))

TAGS = ['POINTERS', 'LOOPS']

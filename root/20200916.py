# Median Of Two Sorted Arrays
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log(m+n)).
# You may assume nums1 and nums2 cannot be both empty.
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# The median is (2+3)/2 = 2.5

def find_median(sort_1, sort_2):
    # assign m and n to length of sorted lists as per instructions
    m = len(sort_1)
    n = len(sort_2)
    # ensure length of first sorted list is less than or equal to second sorted list
    if m > n:
        temp = sort_1; sort_1 = sort_2; sort_2 = temp
        tmp = m; m = n; n = tmp
    # assign index min to 0, index max to length of shortest list, index mid to the mid point of the sum of both lists
    i_min = 0; i_max = m; i_mid = int((m + n + 1) / 2)
    # continue looping until condition is met, or index of min reaches index of max
    while i_min <= i_max:
        # assign i to the floor of halfway between the min index and max index
        i = int((i_min + i_max) / 2)
        # assign j to the difference between the middle index and i
        j = i_mid - i
        # if i is less than the max index and the value at list 2 at index j - 1 is greater than the value at list 1 at index i:
        if i < i_max and sort_2[j-1] > sort_1[i]:
            # reassign the min index to i + 1
            i_min = i + 1
        # else if i is greater than the min index and the value at list 1 at index i - 1 is greater than the value at list 2 at index j:
        elif i > i_min and sort_1[i-1] > sort_2[j]:
            # reassign the max index to i - 1
            i_max = i - 1
        else:
            # initialize a max left value
            max_left = 0
            # if i equals 0, assign max left to the value at list 2 at index j - 1
            if i == 0:
                max_left = sort_2[j-1]
            # else if j equals 0 assign max left to the value at list 1 at index i - 1
            elif j == 0:
                max_left = sort_1[i-1]
            # else assign max left to the max between the value at list 1 at index i - 1 and the value at list 2 at index j - 1
            else:
                max_left = max(sort_1[i-1], sort_2[j-1])
            # if the length of both list 1 and list 2 is odd, return the value at max left
            if ((m + n) % 2 == 1):
                return max_left
            # initialize a min right value
            min_right = 0
            # if i equals m, assign min right to the value at list 2 at index j
            if i == m:
                min_right = sort_2[j]
            # else if j equals n, assign min right to the value at list 1 at index i
            elif j == n:
                min_right = sort_1[i]
            # else assign min right to the min between the value at list 2 at index j and the value at list 1 at index i
            else:
                min_right = min(sort_2[j], sort_1[i])
            # this return hits when the sum of the length of list 1 and list 2 is even, return the quotient of the sum of max left, max right and 2
            return ((max_left + min_right) / 2.0)

nums1 = [1, 2, 3, 4, 5]
nums2 = [5, 6, 7, 8]
print(find_median(nums1, nums2))

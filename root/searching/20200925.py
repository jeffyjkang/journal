# Container With Most Water
# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# Note: You may not slant the container and n is at least 2.
# The above vertical lines are represented by array [1, 8, 6, 2, 5, 4, 8, 3, 7].
# In this case, the max area of water (blue section) the container can contain is 49.
# Example:
# Input: [1, 8, 6, 2, 5, 4, 8, 3 , 7]
# Output: 49

def get_max_area(heights):
    # initialize max area to 0
    max_area = 0
    # initialize left index to 0
    l = 0
    # initialize right index to last index of the heights list
    r = len(heights) - 1
    # loop through as long as left index is less than right index
    while l < r :
        # reassign max area if the product of r - l  and the min between the value of heights at index l and the value of heights at index r is greater than current max area
        max_area = max(max_area, min(heights[l], heights[r]) * (r - l))
        # if the value of heights at index l is less than the value of heights at index r increase left index by 1, else decrease right index by 1
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    # return max area
    return max_area

h = [1, 8, 6, 2, 5, 4, 8, 3 , 7]

print(get_max_area(h))

TAGS = ['SEARCH', 'AREA']
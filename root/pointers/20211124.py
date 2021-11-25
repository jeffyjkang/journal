# Jump Game II
# Given an array of non-negative integers,
# you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# Example:
# Input: [2, 3, 1, 1, 4]
# Output: 2
# Explanation: The minimum number of jumps to each the last index is 2.
# Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Note: You can assume that you can always reach the last index.

def jump_game(lst):
    # initialize jumps counter to 0
    jumps = 0
    # initialize 2 pointers, max_steps and landing
    max_steps = 0; landing = 0;
    # loop through indices of list
    for i in range(len(lst)):
        # assign max_steps to either existing max_steps or the value of current index + index
        max_steps = max(max_steps, lst[i] + i)
        # if current index is landing and we have not reached the end of the list
        if i == landing and i != len(lst) - 1:
            # increment the jumps counter, reassign landing to max_steps
            jumps += 1
            landing = max_steps
    # return jumps counter at end of loop
    return jumps

jump_arr = [2, 3, 1, 1, 4]

print(jump_game(jump_arr))

TAGS = ['POINTERS', 'LOOPS']

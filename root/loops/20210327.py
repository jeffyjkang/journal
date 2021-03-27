# Count And Say
# The count-and-say sequence is the sequence of integers with the first five terms as following:
# 1. 1
# 2. 11
# 3. 21
# 4. 1211
# 5. 111221
# 1 is read off as 'one 1' or 11.
# 11 is read off as 'two 1s' or 21.
# 21 is read off as 'one 2, then one 1' or 1211.
# Given an integer n where 1 <= n <= 30, generate the nth term of the count-and-say sequence.
# Note: Each term of the sequence of integers will be represented as a string.
# Example 1:
# Input: 1
# Output: '1'
# Example 2:
# Input: 4
# Output: '1211'

def count_and_say(n):
    # if n is equal to 1 return '1'
    if n == 1:
        return '1'
    # initialize previous string variable to '1'
    prev_string = '1'
    # loop from 1 to n
    for _ in range(1, n):
        # initialize temp to an empty string
        temp = ''
        # initialize count to 1
        count = 1
        # loop from 1 to length of prev_string, first pass will skip
        for j in range(1, len(prev_string)):
            # if value of prev_string at index j is equal to value of prev_string at index j - 1, increment count
            if prev_string[j] == prev_string[j-1]:
                count += 1
            # if value of prev_string at index j is not equal to value of prev_string at index j - 1,
            else:
                # update temp string to temp, count and prev_string at previous index
                temp = temp + str(count) + str(prev_string[j-1])
                # reset count to 1
                count = 1
        # update temp string to temp, count and prev_string at last char
        temp = temp + str(count) + str(prev_string[-1])
        # reassign prev_string to temp
        prev_string = temp
    # return prev_string
    return prev_string

print(count_and_say(6))

TAGS = ['LOOPS', 'SEQUENCE']

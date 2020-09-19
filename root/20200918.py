# Zigzag Conversion
# The string 'PAYPALISHIRING' is written in a zigzag pattern on a given number of rows like this:
# P A H N
# APLSIIG
# Y I R
# And then read line by line: 'PAHNAPLSIIGYIR'
# Write the code that will take a string and make this conversion given a number of rows:
# convert(s, num_rows):
# Example 1:
# Input: s = 'PAYPALISHIRING', numRows = 3
# Output: 'PAHNAPLSIIGYIR'
# Example 2:
# Input: s = 'PAYPALISHIRING', numRows = 4
# Output: 'PINALSIGYAHRPI'
# Explanation:
# P  I  N
# A LS IG
# YA HR
# P  I

def zigzag_converter(s, num_rows):
    # create a string buffer that holds an array of empty strings with length num_rows
    string_buffer = ['' for x in range(num_rows)]
    # initialize index to 0
    i = 0
    # loop through the string
    while i < len(s):
        # loop through the row, this loop is for the vertical part of the zigzag
        for j in range(num_rows):
            # while i is still less than the length of the string
            if i < len(s):
                # assign the string buffer at index of j to the value of the string at index of i
                string_buffer[j] += s[i]
                # increment i
                i += 1
        # loop through the row, in reverse, starting from the second to last index, this loop is for the diagonal part of the zigzag
        for j in range(num_rows - 2, 0, -1):
            # while i is still less than the length of the string
            if i < len(s):
                # assign the string buffer at index of j to the value of the string at index of i
                string_buffer[j] += s[i]
                # increment i
                i += 1
    # loop through number of rows minus the 0 index
    for k in range(1, num_rows):
        # append the string buffer at index of k to the string buffer at index of 0
        string_buffer[0] += string_buffer[k]
    # return the fully appended string
    return string_buffer[0]

string = 'PAYPALISHIRING'
row_count = 4

print(zigzag_converter(string, row_count))

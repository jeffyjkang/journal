# Longest Valid Parentheses
# Given a string containing just the characters '(' and ')' find the length of the longest valid (well-formed) parentheses substring.
# Example 1:
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"

def longest_valid_parentheses(s):
    # initialize stack with arbitrary placeholder value of -1
    stack = [-1]
    # initialize answer to 0
    answer = 0
    # loop through the indices of s
    for i in range(len(s)):
        # if the value of string at index i is an open paretheses:
        if s[i] == '(':
            # append the index to the stack
            stack.append(i)
        # else (the value of string at index i is a closing parentheses):
        else:
            # if the length of the stack is not 0, pop the previous opening bracket's index, (or -1)
            if len(stack) != 0:
                stack.pop()
            # if the length of the stack is still not 0:
            if len(stack) != 0:
                # reassign answer to the max of current answer or the difference of index and the value of stack at the last index
                answer = max(answer, i - stack[len(stack) - 1])
            # if the length of the stack is 0, or stack is empty:
            else:
                # append current index as base for next valid substring if it exists
                stack.append(i)
    return answer

string = '))()(())())('

print(longest_valid_parentheses(string))

TAGS = ['STACK']

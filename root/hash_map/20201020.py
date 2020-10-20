# Valid Parentheses
# Given a string containing just the characters '(', ')', '{', '}', '[', and ']',
# determine if the input string is valid.
# An input string is valid if:
# * Open brackets must be closed by the same type of brackets.
# * Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
# Example 1:
# Input: '()'
# Output: True
# Example 2:
# Input: '()[]{}'
# Output: True
# Example 3:
# Input: '(]'
# Output: False
# Example 4:
# Input: '([)]'
# Output: False
# Example 5:
# Input: '{[]}'
# Output: True

def is_valid_parentheses(string):
    # create a hash map or dict with closing brackets as keys and opening brackets as values
    map = { ')' : '(', '}' : '{', ']' : '[' }
    # initialize an empty list to mimic a stack
    stack = []
    # loop through the values of the string
    for s in string:
        # if the character is in the hash map, (character is a closing bracket)
        if s in map:
            # assign popped value to the popped value of the stack if the stack is not empty, else assign it a dummy value of #
            popped_value = stack.pop() if stack else '#'
            # if the popped value is not the respective hash map's key's value, return false
            if map[s] != popped_value:
                return False
        # if the character is not in the hash map, it is either (, {, or [, append the character to the stack
        else:
            stack.append(s)
    # return true if stack is empty, false if stack is not empty
    return not stack

# s = '{}()[]'
# s = '(]'
# s = '([)]'
s = '{[]}'

print(is_valid_parentheses(s))

TAGS = ['HASH_MAP', 'STACK']
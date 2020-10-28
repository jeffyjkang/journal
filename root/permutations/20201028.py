# Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# For example, given n = 3, a solution set is:
# [
#     "((()))",
#     "(()())",
#     "(())()",
#     "()(())",
#     "()()()"
# ]

def generate_perentheses(pair_count):
    # initialize result's list to an empty list
    result = []
    # invoke back_track, passing in the result list, empty string, 0, 0 and pair_count
    back_track(result, '', 0, 0, pair_count)
    # return the result list
    return result

# helper function
def back_track(res, cur, l, r, p_c):
    # base case, if the length of the current string is double the pair count
    if len(cur) == 2 * p_c:
        # append the current string to the result list
        res.append(cur)
        # break, and return
        return
    # if left pointer is less than pair count
    if l < p_c:
        # recursively call back_track, add '(' to current string, increment left pointer by 1
        back_track(res, cur + '(', l + 1, r, p_c)
    # if right pointer is less than left pointer
    if r < l:
        # recursively call back_track, add ')' to current string, increment right pointer by 1
        back_track(res, cur + ')', l, r + 1, p_c)

n = 3

print(generate_perentheses(n))

TAGS = ['PERMUTATIONS', 'RECURSION']

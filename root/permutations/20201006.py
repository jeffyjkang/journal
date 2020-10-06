# LETTER COMBINATIONS OF A PHONE NUMBER
# Given a string containing digits from 2 - 9 inclusive,
# return all possible letter combinations that the number could represent.
# A mapping of digit to letters (just like on the telephone) is given below.
# Note that 1 does not map to any letters.
# "abc" = 2, "def" = 3, "ghi" = 4, "jkl" = 5, "mno" = 6, "pqrs" = 7, "tuv" = 8, "wxyz" = 9
# Example:
# Input: "23"
# Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.

def letter_combinations(digits):
    # edge case, if the digits string is empty, return an empty list
    if len(digits) == 0: return []
    # initialize a dictionary, map the numbers to their corresponding letters
    phone_dict = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
    # initialize an empty list to hold all possible permutation results
    permutation_results = []
    # invoke helper function, pass in digits string, phone number dictionary, and permutation results list as the arguments
    back_track(digits, phone_dict, permutation_results)
    # return final permutation results
    return permutation_results

# helper function
def back_track(digits, phone_dict, permutation_results, current_string = '', current_level = 0):
    # base case, if current level and the length of the digits string are equal
    if current_level == len(digits):
        # append the current string to the permutation results
        permutation_results.append(current_string)
        # return and exit
        return
    # loop through each char value at phone_dict of key digits at index of current level
    for i in phone_dict[int(digits[current_level])]:
        # recursively call back_track, passing in digits string, phone_dict, permutation results, while appending i to the current string and incrementing current level by 1
        back_track(digits, phone_dict, permutation_results, current_string + i, current_level + 1)


d = "23"

print(letter_combinations(d))

TAGS = ['PERMUTATIONS', 'CONVERSION', 'PHONE_MAP', 'RECURSION']

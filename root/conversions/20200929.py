# Roman To Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol  Value
# I       1
# V       5
# X       10
# L       50
# C       100
# D       500
# M       1000
# For example, two is written as II in Roman numeral, just two one's added together.
# Twelve is written as, XII, which is simply X + II.
# The number twenty seven is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII.
# Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
# I can be placed before V(5) and X(10) to make 4 and 9.
# X can be placed before L(50) and C(100) to make 40 and 90.
# C can be placed before D(500) and M(1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.
# Example 1:
# Input: "III"
# Output: 3
# Example 2:
# Input: "IV"
# Output: 4
# Example 3:
# Input: "IX"
# Output: 9
# Example 4:
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V = 5, III = 3
# Example 5:
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4

def rom_to_int(rom):
    # create a dict where key is the roman numeral and value is the integer value
    ri_map = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    # initialize the return integer value to 0
    int_val = 0
    # initialize index to 0
    i = 0
    # loop while index is less than the length of the roman numeral argument
    while i < len(rom):
        # if index plus 1 is less than the length of the roman numeral argument and the values of the two indexes are in the dict
        if i + 1 < len(rom) and rom[i : i + 2] in ri_map:
            # add the value from the dict provided by the key from the indexes to the return integer
            int_val += ri_map[rom[i : i + 2]]
            # increment the index by 2
            i += 2
        # if previous condition is not met
        else:
            # add the value from the dict provided by the key from index to the return argument
            int_val += ri_map[rom[i]]
            # increment the index by 1
            i += 1
    # return the integer value
    return int_val

# roman = 'LVIII'
roman = 'MCMXCIV'

print(rom_to_int(roman))

TAGS = ["CONVERSION", "ROMAN_NUMERALS"]

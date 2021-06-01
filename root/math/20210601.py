# Multiply Strings
# Given two non-negative integers num1 and num2 represented as strings,
# return the product of num1 and num2, also represented as a string.
# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# Note:
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the nubmer 0 itself.

def multiplyStrings(num1, num2):
    # edge case if either num1 or num2 equals '0' return '0'
    if num1 == '0' or num2 == '0': return '0'
    # reverse the order of num1 and num2, for easy multiplication of each digit
    num1, num2 = num1[::-1], num2[::-1]
    # initialize result array to be length of the sum of num1 string and num2 string
    resArr = [0] * (len(num1) + len(num2))
    # loop through each index of num1 string
    for i in range(len(num1)):
        # loop through each index of num2 string
        for j in range(len(num2)):
            # reassign the value of resArr at the 1's place to the product of num1[1] and num2[j]
            resArr[i + j] += int(num1[i]) * int(num2[j])
            # assign the carry value by dividing resArr[i + j] by 10 and round the number down to the nearest int
            resArr[i + j + 1] += resArr[i + j] // 10
            # reassign value at resArr[i + j] to have only one digit by the modulo operator
            resArr[i + j] %= 10
    # after the iterations, initialize the result string
    res = ''
    # if the last element of resArr is a 0, remove
    if resArr[-1] == 0:
        resArr.pop()
    # loop through resArr in reverse
    for num in resArr[::-1]:
        # append the value of the converted num to the result string
        res += str(num)
    # return result
    return res

number1 = '123'
number2 = '456'

print(multiplyStrings(number1, number2))

TAGS = ['MATH', 'STRINGS']

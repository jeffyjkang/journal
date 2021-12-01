# Pow(x, n)
# Implement pow(x, n), which calculates x raised to the power n (xn).
# Example 1:
# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:
# Input: 2.10000, 3
# Output: 9.26100
# Example 3:
# Input: 2.00000, -2
# Output: 0.25000
# Note: -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [-231, 231 - 1]

def raise_pow(x, n):
    # base case, if n is equal to 0 return 1
    if (n == 0):
        return 1
    # recursively call raise_pow with the base and cast the quotient of n and 2 to an integer; assign to temp
    temp = raise_pow(x, int(n / 2))
    # if n is even in the stack, return the product of temp and temp
    if (n % 2 == 0):
        return temp * temp
    # if n is odd in the stack
    else:
        # if n is positive, return the product of the base, temp and temp
        if n > 0:
            return x * temp * temp
        # if n is negative, return the quotient of (product of temp and temp) and the base
        else:
            return temp * temp / x

print(raise_pow(2.00000, -2))

TAGS = ['MATH', 'RECURSION']

"""
Define a function that takes in two numbers a and b and returns the last decimal digit of a^b. Note that a and b may be very large!

For example, the last decimal digit of 9^7 is 9, since 9^7 = 4782969. The last decimal digit of (2^200)^(2^300), which has over 10^92 decimal digits, is 6.

The inputs to your function will always be non-negative integers.
Examples

last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6
"""

def last_digit(n1, n2):
    result = pow(n1, n2, 10)
    result_str = str(result)
    return int(result_str[-1])

def last_Digit(n1, n2):
    return pow( n1, n2, 10 )

rules = {
    0: [0,0,0,0],
    1: [1,1,1,1],
    2: [2,4,8,6],
    3: [3,9,7,1],
    4: [4,6,4,6],
    5: [5,5,5,5],
    6: [6,6,6,6],
    7: [7,9,3,1],
    8: [8,4,2,6],
    9: [9,1,9,1],
}
def Last_digit(n1, n2):
    ruler = rules[int(str(n1)[-1])]
    return 1 if n2 == 0 else ruler[(n2 % 4) - 1]

# import math

# # Function to find b % a
# def Modulo(a, b) :
#     # Initialize result
#     mod = 0

#     # calculating mod of b with a to make
#     # b like 0 <= b < a
#     for i in range(0, len(b)) :
#         mod = (mod * 10 + (int)(b[i])) % a

#     return mod # return modulo


# function to find last digit of a ^ b
# def LastDigit(a, b) :
#     len_a = len(a)
#     len_b = len(b)

#     # if a and b both are 0
#     if (len_a == 1 and len_b == 1 and b[0] == '0' and a[0] == '0') :
#         return 1

#     # if exponent is 0
#     if (len_b == 1 and b[0]=='0') :
#         return 1

#     # if base is 0
#     if (len_a == 1 and a[0] == '0') :
#         return 0

#     # if exponent is divisible by 4 that means last
#     # digit will be pow(a, 4) % 10.
#     # if exponent is not divisible by 4 that means last
#     # digit will be pow(a, b % 4) % 10
#     if((Modulo(4, b) == 0)) :
#         exp = 4
#     else :
#         exp = Modulo(4, b)

#     # Find last digit in 'a' and compute its exponent
#     res = math.pow((int)(a[len_a - 1]), exp)

#     # Return last digit of result
#     return res % 10

print(last_digit(9, 7))
print(last_digit(2 ** 200, 2 ** 300))
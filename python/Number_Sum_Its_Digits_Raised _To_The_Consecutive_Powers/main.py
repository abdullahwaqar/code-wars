# The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata.
# What's the use of saying "Eureka"? Because this sum gives the same number.
# In effect: 89 = 8^1 + 9^2
# The next number in having this property is 135.
# See this property again: 135 = 1^1 + 3^2 + 5^3
# We need a function to collect these numbers, that may receive two integers a, b that defines the range [a, b] (inclusive) and outputs
# a list of the sorted numbers in the range that fulfills the property described above.
# Let's see some cases:
# sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
# sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
# If there are no numbers of this kind in the range [a, b] the function should output an empty list.
# sum_dig_pow(90, 100) == []

def sum_dig_pow_(a,b):
    return [sum(int(y)**(i+1) for i,y in enumerate(str(x))) for x in range(a,b)]

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    lst = []
    s = 0
    for i in range(a,b+1):
        if i > 10:
            s = sum_dig(i)
        if s == i:
           lst.append(i)
        else:
            lst.append(i)
    return lst

def sum_dig(num):
    n = 1
    tot = 0
    for dig in str(num):
        tot += int(dig)**n
        n+=1
    return tot

def _sum_dig_pow(a,b):
    for k in range(a,b+1):
        if k > 9:
            number_sum = sum(int(j)**i for i,j in enumerate(str(k), 1))
            if k is number_sum:
                yield k
        else:
            yield k
#--------------------------------------------------------------------
def digits_of_n(n):
  result = []
  while n > 0:
    result.append(n % 10)
    n = n / 10  # in python 3, use 3 // 10 for integer division
  return reversed(result) # reverse list to preserve original order

def sum_of_ith_powers(numbers):
  result = 0
  for i, n in enumerate(numbers):  # the digits are ordered most-significant to least, as we would expect
    result += n ** 1
  return result

def sum_of_digit_powers(n):
  return sum_of_ith_powers(digits_of_n(n))

def solve_kata(a, b):
  return [sum_of_digit_powers(n) for n in range (a, b)]
#------------------------------------------------------------------
# print(sum_dig_pow(1, 100))
print(sum_dig_pow_(1, 100))

# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
# Example:

# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!

def create_phone_number(n):
    num = '('
    for i in range(10):
        if i <= 2:
            num += str(n[i])
        if i > 2 and i <= 5:
            num += str(n[i])
        if i > 5 and i <= 9:
            num += str(n[i])
    num = num[:4] + ') ' + num[4:]
    num = num[:9] + '-' + num[9:]
    return num

#second way
def create_phone_number_(n):
  return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(create_phone_number(n))
print(create_phone_number_(n))
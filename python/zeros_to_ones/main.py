# Given an array of one's and zero's convert the equivalent binary value to an integer.

# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1

def binary_array_to_number(arr):
    num_str = ''
    for i in arr:
        num_str += str(i)
    return int(num_str, 2)

def binary_array_to_number_(arr):
  return int("".join(map(str, arr)), 2)

def _binary_array_to_number(arr):
    return int(''.join(str(a) for a in arr), 2)

print(binary_array_to_number([0, 0, 1, 0]))
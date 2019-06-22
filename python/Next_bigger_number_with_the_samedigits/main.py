"""
You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

12 ==> 21
513 ==> 531
2017 ==> 2071

If no bigger number can be composed using those digits, return -1:

9 ==> -1
111 ==> -1
531 ==> -1
"""

import random

def next_bigger_(n):
    tmp_num = list(str(n))
    counter = True
    while counter:
        temp_holder = ''.join(tmp_num)
        if n < int(temp_holder):
            counter = False
            return int(temp_holder)
        else:
            random.shuffle(tmp_num)

def _next_bigger(n):
    number = map(int, str(n))
    tmp_holder = []

    # Base case when the digits are in descending order return -1
    for i in range(len(number) - 1, 0, -1):
        if number[i] > number[i - 1]:
            print(tmp_holder)
            tmp_holder.append(number[i])
            number.pop(i)

    # If list contains only 1 element return -1
    if len(tmp_holder) == 0:
        return -1

    ret = number + tmp_holder
    del tmp_holder, number
    return int(''.join(map(str, ret)))

import itertools
def next_bigger(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1

# print(next_bigger(2017))
print(next_bigger(12))
next_bigger(1)
# print(next_bigger(111))
# print(next_bigger(531))
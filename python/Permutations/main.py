"""
In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Examples:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

The order of the permutations doesn't matter.
"""

def permutations(string):
    ret_buffer = []
    for i in range(0, len(string)):
        for letter in string:
            if not letter == string[i]:
                ret_buffer.append(string[i] + letter)
    return ret_buffer

print(permutations('aabb'))
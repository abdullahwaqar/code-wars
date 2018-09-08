# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

# Examples:

# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

import re

def solution_(s):
    return re.findall(".{2}", s + "_")

def _solution(s):
    return [s[x:x+2] if x < len(s) - 1 else s[-1] + "_" for x in range(0, len(s), 2)]

def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result

print(solution_('abcd'))
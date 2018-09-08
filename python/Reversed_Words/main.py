# Complete the solution so that it reverses all of the words within the string passed in.

# Example:

# reverseWords("The greatest victory is that which requires no battle")
# // should return "battle no requires which that is victory greatest The"


def reverseWords(s):
    if s == "":
        return s
    else:
        return reverseWords(s[1:]) + s[0]


print(reverseWords('!dlrow olleh'))
def alphabet_pos(text):
    num_push = ""
    for letter in text:
        if ord(letter) == 32:
            pass
        elif ord(letter) < 97 and ord(letter) != 46 and ord(letter) != 39:
            num_push +=  str(ord(letter) - 64)
            num_push += " "
        elif ord(letter) > 96:
            num_push += str(ord(letter) - 96)
            num_push += " "
        elif ord(letter) == 46:
            pass
        elif ord(letter) == 39:
            pass
    return num_push[:-1]

def alphabet_position(text):
    for letter in text:
        for num in range(65, 97):
            if ord(letter) == num:
                print("bu")


print(alphabet_pos("he sunset sets at twelve o' clock."))
# alphabet_position('Omer')

# print(range(1,10))
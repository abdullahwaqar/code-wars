# An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a given series of numbers. You are provided with consecutive elements of an Arithmetic Progression. There is however one hitch: exactly one term from the original series is missing from the set of numbers which have been given to you. The rest of the given series is the same as the original AP. Find the missing term.
# You have to write the function findMissing(list), list will always be at least 3 numbers. The missing term will never be the first or last one.
# Example
# find_missing([1, 3, 5, 9, 11]) == 7
# ```
# PS: This is a sample question of the facebook engineer challenge on interviewstreet. I found it quite fun to solve on paper using math, derive the algo that way. Have fun!


def find_missing(sequence):
    mean_diff = []
    num = 0
    for n in range(0, len(sequence) - 1):
        mean_diff.append(sequence[n + 1] - sequence[n])

    for n in range(0, len(sequence) - 1):
        if (sequence[n + 1] - sequence[n]) != mean_diff[0]:
            num = sequence[n]
            break
    return num + mean_diff[0]

print(find_missing([1, 3, 5, 9, 11]))
print(find_missing([1, 3, 4, 5, 6, 7, 8, 9]))
print(find_missing([1, 3, 5, 7, 11, 13]))

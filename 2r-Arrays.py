# Note that the reading section uses Python 2 but
# the coding section requires Python 3.6

# reverse an array inline
A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
A.reverse()  # note that it doesn't return anything
print(A)

# let's try again
A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # reset A


def reverse(A):
    # complement is the last index number
    c = len(A) - 1
    # iterate the first half and exchange them with their complement parts
    for i in range(len(A) // 2):
        A[i], A[c] = A[c], A[i]
        c -= 1

    return A


print(reverse(A))

# you can also zip them but too lengthy and hard to read
# for i, j in zip(range(len(A) // 2), range(len(A)-1, (len(A)-1) // 2, -1)):
# so you can improve on the generator part
# note that [::-1] doesn't create duplicates for generators
# for i, j in zip(range(len(A) // 2), range(len(A) // 2, len(A))[::-1]):
A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # reset A


def reverse_zip(A):
    for i, c in zip(range(len(A) // 2), range(len(A) // 2, len(A))[::-1]):
        A[i], A[c] = A[c], A[i]

    return A


print(reverse_zip(A))

# =============================================================================
A = 'How about a string?'


def reverse_and_able_on_string(A):
    return A[::-1]


print(A)  # note that A doesn't change, so [::-1] duplicates a new string/array
print(reverse_and_able_on_string(A))


# another slower way
def reverse_string_slower(A):
    return ''.join(reversed(A))


# there is no such thing as inline string reversal
# because in Python, strings are immutable

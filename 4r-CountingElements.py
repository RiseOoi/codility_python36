# using an array's element as index of another array
A = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9]

count = [0] * 10

for i in A:
    count[i] += 1

print(count)

# using dictionary / hashtable
count = {}

for i in A:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count)

# alternatively, you can generate the dict to avoid cpu branch misprediction
num_dict = dict.fromkeys([x for x in range(10)], 0)
print("Newly generated num_dict:", num_dict)

for i in A:
    num_dict[i] += 1

print(num_dict)


# since we have quickly generated num_dict, let's try the alphabet version too
# quick alphabet characters dictionary generation
# alpha_dict = dict.fromkeys(string.ascii_lowercase, 0)
import string
ALPHA_DICK = dict.fromkeys(string.ascii_uppercase, 0)
ALPHA_DICK['D'] += 9000.0001
print(ALPHA_DICK)


# Problem: You are given an integer m (1 <= m <= 1 000 000) and two non-empty,
# zero-indexed arrays A and B of n integers, a_0, a_1, . . . , a_n−1 and
# b_0, b_1, . . . , b_n−1 respectively (0 <= a_i, b_i <= m).
# The goal is to check whether there is a swap operation which can be performed
# on these arrays in such a way that the sum of elements in array A
# equals the sum of elements in array B after the swap.
# By swap operation we mean picking one element from array A and
# one element from array B and exchanging them.

# Well, above is a very straightforward problem too
# Since we can only swap exactly ONE element from each arrays,
# that means to make them equal after swapping,
# the absolute differences of the two swapping elements
# must equal to the half of absolute differences of the sum of two arrays
# that is, swap_A - swap_B == abs(sum(A) - sum(B)) // 2
# assuming swap_A > swap_B

# note that the implementation below doesn't need to know the upper bound
# it also doesn't need to know A's length,
# doesn't need A and B to be same length
# and more importantly, allows swap_B < swap_A
# in fact, codility's official solution is incomplete and incorrect
def swappable_to_get_equal_sum_or_not(A, B):
    half_diff = abs(sum(A) - sum(B)) // 2
    print(sum(A), sum(B))
    # if half_diff is 0, means the difference is 1
    # since the arrays contain only integer, there is no swap solution
    if not half_diff:
        return False

    # since we only need to swap one element, set is a good hashtable to use
    set_A = set(A)
    print(set_A)

    for b in B:
        complement = b - half_diff

        # below is to allow swap_B <= swap_A
        if complement < 0:
            complement = b + half_diff

        # check if the complement of b ever existed in A
        if complement in set_A:
            return True

    return False


A = [0, 0, 1, 2, 3, 4, 5, 5, 5, 5, 6, 8]
B = [7, 8, 9, 10]
print(swappable_to_get_equal_sum_or_not(A, B))  # both works
print(swappable_to_get_equal_sum_or_not(B, A))  # both works

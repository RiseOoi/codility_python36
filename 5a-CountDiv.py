# Write a function:

# def solution(A, B, K)

# that, given three integers A, B and K,
# returns the number of integers within the range [A..B]
# that are divisible by K, i.e.:

# { i : A ≤ i ≤ B, i mod K = 0 }

# For example, for A = 6, B = 11 and K = 2, your function should return 3,
# because there are three numbers divisible by 2 within the range [6..11],
# namely 6, 8 and 10.

# Assume that:

# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.

# Complexity:

# expected worst-case time complexity is O(1);
# expected worst-case space complexity is O(1).

# A, B: 0..2M
# K: 1..2M
# Inclusive


# a variant of 3b
# essentially it's divisible_range = end_divisible - begin_divisible
# since it's inclusive, -1 or whatever between 0 and k-1 to begin_divisible
# hopefully no additional comments needed

def solution(A, B, K):
    return B // K - (A - 1) // K


print(solution(6, 11, 2))

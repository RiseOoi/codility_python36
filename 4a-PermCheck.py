# A non-empty array A consisting of N integers is given.

# A permutation is a sequence containing each element
# from 1 to N once, and only once.

# For example, array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2

# is a permutation, but array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3

# is not a permutation, because value 2 is missing.

# The goal is to check whether array A is a permutation.

# Write a function:

# def solution(A)

# that, given an array A, returns 1 if array A is a permutation
# and 0 if it is not.

# For example, given array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2

# the function should return 1.

# Given array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3

# the function should return 0.

# Assume that:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [1..1,000,000,000].

# Complexity:

# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N),
# beyond input storage (not counting the storage required for input arguments).

# This is just a variation of 3r and 3a.
# so just use maths and solve it straightaway


# believe it or not, the solution below achieves 100%
# it even passes anti-sum test.
def solution(A):
    N = len(A)
    N = (N + 1) * N // 2
    sum_A = sum(set(A))  # set(A) is the secret sauce
    if sum_A == N:
        return 1
    else:
        return 0


print(solution([2, 3, 1, 5]))
print(solution([2, 3, 1, 4, 5]))
print(solution([2, 3, 1, 4]))

# anti sum tests
a = [1, 4, 1]
b = [2, 2, 2]
c = [9, 5, 7, 3, 2, 7, 3, 1, 10, 8]
d = [5, 3, 1, 1]
print(solution(a))
print(solution(b))
print(solution(c))
print(solution(d))

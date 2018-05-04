# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer
# (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Assume that:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

# Complexity:

# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N),
# beyond input storage (not counting the storage required for input arguments).


# also just a variation of 3r, 3a, 4a, and 4b
# hopefully no additional comments are needed
def solution(A):
    set_A = set(A)
    for i in range(1, len(A) + 2):
        if i not in set_A:
            return i

# in case you wondering why len(A) + 2
# since elements of A starts from 1, and Python's end range is exclusive,
# we need len(A) + 2 for end range
# eg. [1, 2, 3], we loop from 1 to 4, that is, range(1, 5)


print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-1, -3]))

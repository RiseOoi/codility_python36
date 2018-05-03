# A non-empty array A consisting of N integers is given.
# The array contains an odd number of elements,
# and each element of the array can be paired with another element
# that has the same value, except for one element that is left unpaired.

# For example, in array A such that:

#   A[0] = 9  A[1] = 3  A[2] = 9
#   A[3] = 3  A[4] = 9  A[5] = 7
#   A[6] = 9

# the elements at indexes 0 and 2 have value 9,
# the elements at indexes 1 and 3 have value 3,
# the elements at indexes 4 and 6 have value 9,
# the element at index 5 has value 7 and is unpaired.

# Write a function:

# def solution(A)

# that, given an array A consisting of N integers
# fulfilling the above conditions, returns the value of the unpaired element.

# For example, given array A such that:

#   A[0] = 9  A[1] = 3  A[2] = 9
#   A[3] = 3  A[4] = 9  A[5] = 7
#   A[6] = 9

# the function should return 7, as explained in the example above.

# Assume that:

# N is an odd integer within the range [1..1,000,000];
# each element of array A is an integer within the range [1..1,000,000,000];
# all but one of the values in A occur an even number of times.

# Complexity:

# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(1),
# beyond input storage (not counting the storage required for input arguments).


# additional memory requirement
# this solution obtains 100% on codility, but worst case space complexity is
# actually O(N//2) because the first half may don't have complements at all
# so the removal from set is not quick enough
def solution_set(A):
    hset = set()
    for x in A:
        if x in hset:
            hset.remove(x)
        else:
            hset.add(x)

    return hset.pop()


# here's a true O(1) space solution
# since we assume everyone has complements but only one element
# we can exploit this knowledge using the XOR property
# why this works? because if there must exist a complement, they got killed off
# eg. 9's binary form is 1001, since there must be even number of 9s,
# 1001 XOR 1001 is 0000, so they will cancel each other out in ret
def solution(A):
    ret = 0
    # print(f"you can try printing the binary representation: {ret:b}")
    # btw you can use bin(ret) to show binary representation too
    for a in A:
        ret ^= a
        # print(f"{a:b}, {ret:b}")  # uncomment to print

    return ret


print(solution_set([9, 3, 9, 3, 9, 7, 9]))
print(solution([9, 3, 9, 3, 9, 7, 9]))

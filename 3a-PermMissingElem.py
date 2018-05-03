# An array A consisting of N different integers is given.
# The array contains integers in the range [1..(N + 1)],
# which means that exactly one element is missing.

# Your goal is to find that missing element.

# Write a function:

# def solution(A)

# that, given an array A, returns the value of the missing element.

# For example, given array A such that:

#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5

# the function should return 4, as it is the missing element.

# Assume that:

# N is an integer within the range [0..100,000];
# the elements of A are all distinct;
# each element of array A is an integer within the range [1..(N + 1)].

# Complexity:

# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(1),
# beyond input storage (not counting the storage required for input arguments).


# Exactly one missing, so using math is good enough
# Subtracts the sum of array from the expected total of 1 + 2 + ... + N
def solution(A):
    N = len(A) + 1  # add one more because of the "missing" element
    N = (N + 1) * N // 2  # see 3r if you do not understand this line
    return N - sum(A)


print(solution([2, 3, 1, 5]))
# for some types of problems you may need skipping
# use N = sum(range(1, len(A) + 2, skip_sequence)) if needs skipping

# some internet friends noted about integer overflow for other prog languages
# Well, in many languages there is a size limit of integer
# Eg, 64-bit integer uses the most significant bit (MSB) or left-most bit
# to determine whether the integer is negative or positive
# So in modern 64-bit computers, you only get 63 bits to store an integer
# that is, -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
# or from -(2^63) to (2^63)-1 if signed.
# if you use unsigned integer, than since there's only positive number
# the unsigned 64-bit integer can go up to (2^64)-1

# so for very large N, if you try to so sum(A),
# it can no longer stores in 64-bit integer
# Python does not have this problem
# try the following code
print(2**10000)  # it works
# So we do not need another solution, above is the perfect solution.


# So if Python does not automatically converts the data type for us,
# what should we do? well, remember 2b? The one using XOR?
# finding a number that never existed when other pairs died is exactly the same
# as to finding a number that only existed one time when other pairs died
# that is, we compare all the values that should have existed
# to all the values in the array,
# and then we can find the never existed element
# because there is an extra element from the should have existed list
# and that extra element is the missing element
# sorry I like to do this XP
def solution_xor(A):
    ret = len(A) + 1  # adds the missing should have existed element
    # i is the should have existed element starting from 1
    for i, a in enumerate(A, 1):
        ret ^= a ^ i
        # print(f"{i:b}, {a:b}, {ret:b}")  # uncomment to print

    return ret


print(solution_xor([2, 3, 1, 5]))

# speed of large1/2 on codility using addition: 0.128s and 0.096s
# speed of large1/2 on codility using XOR: 0.148s and 0.100s
# as you can see, addition is a little faster here, BUT there's a catch
# mathematical and logical operations are hardware implemented
# so they are of equal speed,
# the addition creates only 2 data storage, that is N and sum(A)
# while the xor crunches ret, i, and a for this particular type of problem

# HOWEVER, the largest number XOR will ever encounter is N
# the largest number the addition will add up is exactly N = (N + 1) * N // 2
# in big-O sense, they are equivalent.
# but there exists a moment when movement of pointers is slower than comparison
# so use XOR, you will need this knowledge again in the future

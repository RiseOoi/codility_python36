# You are given N counters, initially set to 0,
# and you have two possible operations on them:

# increase(X) − counter X is increased by 1,
# max counter − all counters are set to the maximum value of any counter.
# A non-empty array A of M integers is given.
# This array represents consecutive operations:

# if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
# if A[K] = N + 1 then operation K is max counter.

# For example, given integer N = 5 and array A such that:

#     A[0] = 3
#     A[1] = 4
#     A[2] = 4
#     A[3] = 6
#     A[4] = 1
#     A[5] = 4
#     A[6] = 4

# the values of the counters after each consecutive operation will be:

#     (0, 0, 1, 0, 0)
#     (0, 0, 1, 1, 0)
#     (0, 0, 1, 2, 0)
#     (2, 2, 2, 2, 2)
#     (3, 2, 2, 2, 2)
#     (3, 2, 2, 3, 2)
#     (3, 2, 2, 4, 2)

# The goal is to calculate the value of every counter after all operations.

# Write a function:

# def solution(N, A)

# that, given an integer N and a non-empty array A consisting of M integers,
# returns a sequence of integers representing the values of the counters.

# The sequence should be returned as:

# a structure Results (in C), or
# a vector of integers (in C++), or
# a record Results (in Pascal), or
# an array of integers (in any other programming language).

# For example, given:

#     A[0] = 3
#     A[1] = 4
#     A[2] = 4
#     A[3] = 6
#     A[4] = 1
#     A[5] = 4
#     A[6] = 4

# the function should return [3, 2, 2, 4, 2], as explained above.

# Assume that:

# N and M are integers within the range [1..100,000];
# each element of array A is an integer within the range [1..N + 1].

# Complexity:

# expected worst-case time complexity is O(N+M);
# expected worst-case space complexity is O(N),
# beyond input storage (not counting the storage required for input arguments).


# Essentially, we can separate the usual counting part and the max_counter part
# That is, we will just count as normal
# When max_counter case comes, we store the highest values
# and by resetting everything to 0, we can count as normal again
# then we just add the stored values back to the array and voila
# Note that there exist many cases of elements that were never counted
# In these "Sparse" cases, a dictionary is much recommended.
def solution(N, A):
    counters = {}
    max_counter = 0

    for a in A:
        # normal counting case
        if a >= 1 and a <= N:  # these conditions are assumed anyway
            if a in counters:
                counters[a] += 1
            else:
                counters[a] = 1

        # max counter case
        elif a == N + 1:
            if len(counters) >= 1:
                # updates storage and adds it with current highest value
                max_counter += max(counters.values())
                counters = {}  # reset and continue with normal counting

    ret = [max_counter for i in range(N)]
    for key, value in counters.items():
        ret[key - 1] += value

    return ret


print(solution(1, [2, 1, 1, 2, 1]))
print(solution(5, [3, 4, 4, 6, 1, 4, 4]))

# note that although solution above scores 100%, max(counters.values()) is O(N)
# in worst case scenario. However, note that dictionary is fast and the
# bigger a random case gets, the sparser the case usually becomes
# the bigger a random case gets, the less chance it will become max_counter too
# so comparison every single time is actually slower than a one time O(N)
# don't believe me? well, let's test it out


def solution_alternative(N, A):
    counters = {}
    max_counter = 0
    current_max = 0

    for a in A:
        # normal counting case
        if a >= 1 and a <= N:  # these conditions are assumed anyway
            if a in counters:
                counters[a] += 1
            else:
                counters[a] = 1

            # stores current highest value whenever it finds one
            current_max = max(current_max, counters[a])  # quick comparison

        # max counter case
        elif a == N + 1:
            if len(counters) >= 1:
                # updates max_counter and adds it with current highest value
                max_counter += current_max
                current_max = 0  # reset current_max
                counters = {}  # reset and continue with normal counting

    ret = [max_counter for i in range(N)]
    for key, value in counters.items():
        ret[key - 1] += value

    return ret


# speed of solution on large, extreme_large cases:
# large_random1: 0.096s, large_random2: 0.180s
# extreme_large with all max_counter operations: 0.240s, 0.216s

# speed of solution_alternative on extreme_large cases:
# large_random1: 0.100s, large_random2: 0.200s
# extreme_large with all max_counter operations: 0.240s, 0.252s

# behold, using max(dict.values()) is surprisingly slightly faster
# which seemingly shouldn't really happen!
# well, actually it's just a Python trick
# calling a C implemented max() gives higher throughput for a long list
# than calling a max() everytime inside a Python for loop (infamously slow)
# so keep that in mind regardless of you are using Python or other languages

# additional information:
# to get the index of the maximum number of a list
# or list.index(max(list))
# to get the index of the maximum number of a dict
# max(dict, key=dict.get)
# note that you can also always sort them first then get the last number

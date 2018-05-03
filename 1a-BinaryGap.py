# A binary gap within a positive integer N is any maximal sequence of
# consecutive zeros that is surrounded by ones at both ends in the binary
# representation of N.

# For example, number 9 has binary representation 1001 and contains a
# binary gap of length 2. The number 529 has binary representation 1000010001
# and contains two binary gaps: one of length 4 and one of length 3.
# The number 20 has binary representation 10100 and contains one binary gap
# of length 1.
# The number 15 has binary representation 1111 and has no binary gaps.

# Write a function:
# int solution(int N);
# that, given a positive integer N,
# returns the length of its longest binary gap.
# The function should return 0 if N doesn't contain a binary gap.
# For example, given N = 1041 the function should return 5,
# because N has binary representation 10000010001 and so its
# longest binary gap is of length 5.

# Assume that:

# N is an integer within the range [1..2,147,483,647].
# Complexity:

# expected worst-case time complexity is O(log(N));
# expected worst-case space complexity is O(1).


def solution(N):
    binary_gap = 0
    max_binary_gap = 0

    # There are no 0s in front of the most significant 1
    # But there may be 0s in the least significant bits
    # So the first thing is to find the first/least significant 1
    while N >= 1:
        bit = N % 2
        if bit:
            break

        N = N // 2

    # After we found the first/LS 1, we can start counting the 0s between 1s
    while N >= 1:
        bit = N % 2
        if bit:
            max_binary_gap = max(max_binary_gap, binary_gap)
            binary_gap = 0
        else:
            binary_gap += 1

        N = N // 2

    return max_binary_gap


# Of course you can merge them into one
def solution_flag(N):
    # binary = []  # incase you want to know the binary representation
    binary_gap = 0
    max_binary_gap = 0
    flag = False

    while N >= 1:
        bit = N % 2
        # binary.append(bit)
        if bit == 1:
            flag = True
            max_binary_gap = max(max_binary_gap, binary_gap)
            binary_gap = 0

        if flag and bit == 0:
            binary_gap += 1

        N = N // 2

    # print(binary)
    return max_binary_gap


print(solution(1041))
print(solution_flag(1041))

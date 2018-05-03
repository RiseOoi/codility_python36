# You are given an integer n. Count the total of 1 + 2 + ... + n.
# This is a classical mathemicatical olympiad introductary practice problem

# Well, note that 1 + n is equal to 2 + (n - 1) and 3 + (n - 2) and so on
# So we do not even need to traverse the whole array
# We can calculate this in O(1)

# real_mathematical_answer = (N + 1) * (N / 2)
# int_real_mathematical_answer = int(real_mathematical_answer)
# (N - 1) * (N // 2) doesn't work because if N is odd number,
# the middle number gets truncated in Python 3
# But if we just remove the bracket...

N = 101
answer = (N + 1) * N // 2  # voila
print(answer)

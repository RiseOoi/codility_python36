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

# prefix sums, deceivingly simple but is one of the most powerful techniques
import time

# Time test of two simple list generations and computations
start = time.time()

P = [0] * 10001
# P = [0 for i in range(10001)] also works but a bit slower
for i in range(1, 10001):
    P[i] = i

end = time.time()
print("prebuilt list:", end - start)  # ~ 8e-04 on my machine

# ===

start = time.time()
P = [0]
for i in range(1, 10001):
    P.append(i)

end = time.time()
print("list append:", end - start)  # ~ 1.2e-03 on my machine

# the reason is simple, calling append inside a Python loop is infamously slow
# so how about prefix_sums?


def prefix_sums_pure(A):
    P = [0] * (len(A) + 1)  # need an extra element of '0' in front
    for i in range(len(A)):
        P[i + 1] = P[i] + A[i]

    return P


start = time.time()

prefix_sums_pure(range(1000))

end = time.time()
print("prefix_sums_pure:", end - start)  # ~ 1.8e-04s on my machine

# there are other tricks like using numpy arrays and numpy's cumsum function
# but since outside libraries are out of the scope of this repo,
# here, we will build a prefix sum generator instead
# generator is simply just generating a value on the fly instead of
# storing them all at once. (useful if you only need to iterate the array once)
# usually however, you need the list of the computed prefix_sum


def prefix_sums_gen(A):
    cumsum = 0
    for a in A:
        cumsum += a
        yield cumsum


start = time.time()

prefix_sums_gen(range(10000))

end = time.time()
print("prefix_sums_gen:", end - start)  # ~ 1.8e-06s on my machine

start = time.time()

# if you really need the list
list(prefix_sums_gen(range(10000)))

end = time.time()
print("prefix_sums_gen build list:", end - start)
# ~ 8e-04s on my machine, slower than pure

# that means if you really need the list, build it first
# if not, use a generator and loop it over once

# from Python 3.2+, there is a new itertools.accumulate() function
import itertools as itt

start = time.time()

itt.accumulate(range(10000))

end = time.time()
print("itertools accumulate:", end - start)
# ~ 1.8e-06s on my machine, same as prefix_sums_gen()

start = time.time()

list(itt.accumulate(range(10000)))

end = time.time()
print("itertools accumulate build list:", end - start)
# ~ 3.5e-04s on my machine, faster than list(prefix_sums_gen())
# but slower than just building list from start (prefix_sums_pure())

# there you have it, so many ways to find prefix_sums or cumsum
# with prefix_sums, we can lookup suffix_sum in constant time
# just subtract the prefix_sums of index x from index y+1
# and voila, we get the suffix sum from index x to index y
# P[y + 1] - P[x]

# mushroom picker, starts at spot k, can perform m moves.
# how many mushroom can she pick?
# note that maybe it is something like this
# [0, 0, 0, 100, start, 1, 2, 30, 40]
# so you may need to go left once, then change direction to right
# changing direction more than once is unnecessary

# and if you think carefully, we only need to go m // 3 steps before turning
# eg. let's say we can move 9 steps and moved 3 steps right before turning
# we need 3 steps left to reach our starting position,
# and then another 3 step left to finish using our 9 steps.
# if we move 4 steps to the right, then moving 5 steps left results in
# 2 steps left of starting position
# however! we could have moved 2 steps left then 7 steps right

# and there's one more challenge is that we may reach the border (end)
# but that's just min(steps_to_border, m // 3)

# the official solution make use of min(border, max(k, moves))
# but personally I think it is hard to read and have unnecessary loops

# ok now we got the idea let's write it!
# here we use prefix_sums to lookup instead of repeated computations


def mushrooms(A, k, m):
    best_ret = A[k]  # the mushrooms we are standing on without moving
    cumsum = list(itt.accumulate(A))
    # one thing to note is that accumulate doesn't give a zero starting element
    # it is useful in exclusive ends but here we need the inclusive ends
    # cumsum = [0] + list(itt.accumulate(A)) is a possible solution
    # but adding the starting value back is faster that list concatenation

    # let's move either m // 3 steps left or until border before turning
    for i in range(min(m // 3, k) + 1):  # remember end is exclusive, so + 1
        left_pos = k - i
        # after turning, we also need to beware that we may reach the border
        right_pos = min(k + (m - 2 * i), len(A) - 1)
        best_ret = max(best_ret,
                       cumsum[right_pos] - cumsum[left_pos] + A[left_pos])

    # after that, let's do the same thing but this time moving to right first
    for i in range(min(m // 3 + 1, len(A) - k)):
        right_pos = k + i
        # remember the border~
        left_pos = max(k - (m - 2 * i), 0)
        best_ret = max(best_ret,
                       cumsum[right_pos] - cumsum[left_pos] + A[left_pos])

    return best_ret


test = [2, 3, 7, 5, 1, 3, 9]
mytest = [0, 0, 0, 100, 0, 1, 2, 30, 40]
print(mushrooms(test, 4, 6))  # 25
print(mushrooms(mytest, 4, 6))  # 173

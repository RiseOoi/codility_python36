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

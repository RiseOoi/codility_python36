# A small frog wants to get to the other side of the road.
# The frog is currently located at position X and
# wants to get to a position greater than or equal to Y.
# The small frog always jumps a fixed distance, D.

# Count the minimal number of jumps that the small frog
# must perform to reach its target.

# Write a function:

# def solution(X, Y, D)

# that, given three integers X, Y and D,
# returns the minimal number of jumps from position X to
# a position equal to or greater than Y.

# For example, given:

#   X = 10
#   Y = 85
#   D = 30

# the function should return 3, because the frog will be positioned as follows:

# after the first jump, at position 10 + 30 = 40
# after the second jump, at position 10 + 30 + 30 = 70
# after the third jump, at position 10 + 30 + 30 + 30 = 100

# Assume that:

# X, Y and D are integers within the range [1..1,000,000,000];
# X ≤ Y.

# Complexity:

# expected worst-case time complexity is O(1);
# expected worst-case space complexity is O(1).


def solution(X, Y, D):
    return (Y - X - 1) // D + 1


print(solution(10, 85, 30))
print(solution(10, 100, 30))
print(solution(25, 25, 30))


# Ok, the intuitive thing to do first is the get the distance between them
# that is Y - X
# then you might wonder why (Y - X) // D doesn't work
# Well, for example, (85 - 10) // 30 is 2 not 3
# So to counter this, we always need an extra jump
# But (Y - X) // D + 1 no longer works for exact end position.
# (100 - 10) // 30 + 1 = 4 != correct answer
# Well, take advantage of the integer division, just add -1, voila!
# Alternatively, a more compact answer is (Y - X + D - 1) // D

# btw, above solution doesn't work for when Y < X and Y % D != 0
# to make above solution work, you need ceil instead of floor when Y < X

# Mathematics is always faster than if/else, use mathematics whenever you can

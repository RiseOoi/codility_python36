# my way, personally this is more intuitive
def stars(N):
    # number of rows
    for i in range(N):
        # print spaces
        for j in range(i):
            print(' ', end='')

        # print stars
        for j in range(2 * (N - i) - 1):
            print('*', end='')

        # print blank line
        print()


# official codility way
def stars_2(N):
    # reverse counting type
    for i in range(N, 0, -1):
        for j in range(N - i):
            print(' ', end='')
        for j in range(2 * i - 1):
            print('*', end='')
        print()


def stars_3(N):
    # python string processing type
    for i in range(N):
        # print spaces
        print(' ' * i, end='')
        # print stars
        print('*' * (2 * (N - i) - 1))


def fibonacci(N):
    # not exceeding N
    a = 0
    b = 1
    while a <= N:
        print(a)
        c = a + b
        a = b
        b = c


stars(4)
stars_2(4)
stars_3(4)
fibonacci(14)

# =============================================================================
days = set([
    'Monday', 'Tuesday', 'Wednesday',
    'Thursday', 'Friday', 'Saturday', 'Sunday'
    ])

# set is not ordered
for day in days:
    print(day)

days = {
    'mon': 'Monday',
    'tue': 'Tuesday',
    'wed': 'Wednesday',
    'thu': 'Thursday',
    'fri': 'Friday',
    'sat': 'Saturday',
    'sun': 'Sunday'
}

# From Python 3.6+, dict is ordered for CPython implementation
# but you will need to use OrderedDict for across all implementations
# Starting from Python 3.7+ insertion order preserving dict is language feature
for day in days:
    print(day, 'stands for', days[day])

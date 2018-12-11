""" Towers of Hanoi

Move top disc from a, decrease by 1 then repeat while swapping b and c and a and b
f(n, a, b, c) := { f(n-1, a, c, b), f(n-1, b, a, c) if n > 0 }

>>> hanoi(3, a, b, c)
([1, 2, 3], [], [])
>>> hanoi(4, *initialize(4))
([1, 2, 3, 4], [], [])
>>> hanoi_step_count(0, 3, a, b, c)
7
>>> hanoi_step_count(0, 4, *initialize(4))
15

"""

from stack import Stack


def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        hanoi(n-1, b, a, c)

    return a, b, c


def hanoi_step_count(step_count, n, a, b, c):
    if n > 0:
        step_count = hanoi_step_count(step_count, n-1, a, c, b)
        step_count += 1
        step_count = hanoi_step_count(step_count, n-1, b, a, c)

    return step_count


def initialize(num_discs):
    a = Stack()
    b = Stack()
    c = Stack()
    for i in range(1, num_discs + 1):
        a.push(i)
    return a, b, c


if __name__ == '__main__':
    step_count = 0
    n = 3 # number of discs
    a, b, c = initialize(n)

    import doctest
    doctest.testmod()


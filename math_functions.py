from functools import lru_cache
import itertools

def factorial(n):

    """Return the factorial of n

    f(n) = n * f(n-1)
    f(1) = 1
    f(2) = 2 * f(1)

    :param n: positive int
    :returns a positive int for small inputs, else a long

    >>> factorial(4)
    24
    """

    if n < 0:
        print('Input must be a positive integer')
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    return n * factorial(n-1)


def fibo(n):

    """Return nth element of the fibonacci sequence
    0, 1, 1, 2, 3, 5, 8

    f(n) = f(n-1) + f(n-2)
    f(2) = 1
    f(1) = 0
    f(3) = f(2) + f(1) = 1

    >>> fibo(2)
    1
    >>> fibo(6)
    5
    """

    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibo(n-2) + fibo(n-1)


def fibo_memo(n):

    """Use a dictionary to memoize fibonacci calculations
    f(n) := { memo[n] if n in memo else memo[n] = f(n-1) + f(n-2) }

    >>> fibo_memo(6)
    5
    """

    memo = { 0: 1, 1: 1 }

    if n not in memo:
        memo[n] = fibo(n-2) + fibo(n-1)
    return memo[n]


@lru_cache(maxsize=None)
def fibo_cache(n):

    """Use built-in decorator instead of manual memoization
    f(n) := lru_cache(f(n-1) + f(n-2))

    >>> fibo_cache(6)
    5
    """

    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibo_cache(n-1) + fibo_cache(n-2)


def fibo_generator(n):

    """Use a generator
    Track values for minus_one, minus_two, append sum to list until n elements, return last

    f(n) := { m1, m2 = 0, 0;
        [ cur = 0 if num == 0; cur = 1 if num == 1;
          cur = 1 if num == 2; else cur = m1 + m2; m1, m2 = cur, m1 for range(n) ][-1] }

    >>> fibo_generator(7)
    8
    """

    minus_two = 0
    minus_one = 0
    seq = []
    for num in range(n):
        if num == 0:
            current = 0
        elif num == 1:
            current = 1
        else:
            current = minus_two + minus_one
        seq.append(current)
        minus_one, minus_two = current, minus_one

    return seq[-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()


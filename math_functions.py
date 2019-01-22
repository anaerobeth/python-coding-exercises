from functools import lru_cache, reduce
from operator import mul
from itertools import combinations

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


def iter_factorial(num):

    """Return the factorial of n
    >>> iter_factorial(4)
    24
    """

    result = 1
    for n in range(num, 1, -1):
        result *= n

    return result


def reduce_factorial(num):

    """
    >>> reduce_factorial(4)
    24
    """

    return reduce(mul, [n for n in range(num, 1, -1)])


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

    """Create a fibo sequence using a generator

    f(n) := { yield 0 if n == 0; yield 1 if n > 0;
        else m1, m2 = 1, 0; m1, m2 = m1 + m2, m1; yield m1 for range(n-2) }

    >>> for i in fibo_generator(5): print(i)
    0
    1
    1
    2
    3
    """

    yield 0
    if n > 0: yield 1
    minus_two = 0
    minus_one = 1

    for _ in range(n-2):
        minus_one, minus_two = minus_two + minus_one, minus_one
        yield minus_one


def fibo_sequence(n):

    """Create a fibo sequence using list comprehension
    Track values for minus_one, minus_two, append sum to list until n elements

    f(n) := { m1, m2 = 0, 0;
        [ cur = 0 if num == 0; cur = 1 if num == 1;
          cur = 1 if num == 2; else cur = m1 + m2; m1, m2 = cur, m1 for range(n) ] }

    >>> fibo_sequence(7)
    [0, 1, 1, 2, 3, 5, 8]
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

    return seq


def gcd(a, b):

    """Return the greatest common denominator of a and b

    Divide the larger number by the smaller
    While there is a remainder, decrease the 1/2 of smaller by 1 and set this as divisor
    Return the first divisor that divides both without a remainder

    f(a, b) := { a if a % b == 0 else n if b/n == 0 and a/n == 0 for n in range(b//2,1,-1) }

    >>> gcd(12, 16)
    4
    >>> gcd(115, 35)
    5
    """

    if a > b:
        a, b =  b, a

    if a % b == 0:
        return a

    for num in range(b//2,1,-1):
        if a % num == 0 and b % num == 0:
            return num

    return 1


def gcd_euclid(a, b):

    """Replace larger by remainder, stop when remainder is 0
    f(a, b) := { b if a % b == 0 else repeat (a, b = b, a % b) }

    >>> gcd_euclid(12, 16)
    4
    >>> gcd_euclid(115, 35)
    5
    """

    while a % b != 0:
        a, b = b, a % b

    return b


def gcd_euclid_recurse(a, b):

    """Replace larger by remainder, stop when remainder is 0
    f(a, b) := { b if a % b == 0 else f(b, a % b) }

    >>> gcd_euclid_recurse(12, 16)
    4
    >>> gcd_euclid_recurse(115, 35)
    5
    """

    if a % b == 0:
        return b

    return gcd_euclid_recurse(b, a % b)


def pairs(l):
    return list(combinations(l, 2))


def gcd_from_list(num_list):

    """Get the minimum of the gcds of all possible pairs

    [2, 4, 8] -> pairs (2, 4) (2, 8) (4, 8) -> gcds [2, 2, 4] -> min is 2
    f(l) := { min[gcd(pairs) for pair in pairs(l)] }

    >>> gcd_from_list([2, 4, 8])
    2
    >>> gcd_from_list([50, 25, 100])
    25
    """

    if len(num_list) == 2:
        return gcd_euclid(*num_list)

    gcds = [gcd_euclid(*pair) for pair in pairs(num_list)]

    return min(gcds)


if __name__ == "__main__":
    import doctest
    doctest.testmod()


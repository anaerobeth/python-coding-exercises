def gcd(a, b):
    """Finds the greatest common denominator

    >>> print(gcd(12, 16))
    4
    """
    while a % b != 0:
        a, b = b, a % b
    return b

import doctest
doctest.testmod()

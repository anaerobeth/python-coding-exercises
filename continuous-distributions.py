"""
Continuous Distributions

Normal
Standard Normal
T
Chi-square
F

Distribution is probability density function (pdf) y = f(x)
The total area under the curve of the function is equal to one

"""

from operator import mul
from functools import reduce
from math import sqrt, pi, exp, pow


def factorial(val):

    """
    >>> factorial(5)
    120
    """

    if val <= 1:
        return 1
    return reduce(mul, [ item for item in range(val, 1, -1)])


def combination(n, x):

    """Binomial coefficient or Combination - n Choose k
    n! / (k! * (n-k)!

    >>> combination(10, 3)
    120.0
    """

    result = factorial(n) / (factorial(x) * factorial(n - x))
    return result


def normal_prob(x, mu, sd):
    var = pow(sd, 2)
    denom = pow((2 * pi * var), 0.5)
    num = exp(-pow((x - mu), 2)/ (2 * var))

    return num/denom


class Normal():
    def __init__(self, x, mu, sd):
        self.x = x
        self.mu = mu
        self.sd = sd

    def prob(self):
        total = 0
        for i in range(self.x):
            total += normal_prob(i, self.mu, self.sd)

        return round(total, 4)


if __name__ == '__main__':
    import pdb
    import doctest
    doctest.testmod()

    # Examples from https://stattrek.com/probability-distributions

    # Example exercises for Normal Distribution
    # 1. What is the prob that a bulb with N(300, 50) will last <= 365 days ?
    given = Normal(365, 300, 50)
    assert given.prob() == 0.9015

    # 2. What is the prob that a person who takes an IQ test with N(100, 10)
    # will score between 90 and 110?
    # Hint: P( 90 < X < 110 ) = P( X < 110 ) - P( X < 90 )
    high = Normal(110, 100, 10)
    low = Normal(90, 100, 10)
    assert round(high.prob() - low.prob(), 2) == 0.68

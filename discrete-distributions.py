"""
Discrete Probability Distributions

Binomial
Hypergeometric
Multinomial
Negative Binomial
Poisson
"""

from operator import mul
from functools import reduce


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


def binomial_prob(x, n, psuccess):

    """
    >>> binomial_prob(45, 100, 0.5)
    0.0485
    """

    ncx = combination(n, x)
    success = psuccess ** x
    failure = (1 - psuccess) ** (n - x)

    return round(ncx * success * failure, 4)


def hypergeometric_prob(x, pop, n, k):

    """
    >>> hypergeometric_prob(2, 52, 5, 26)
    0.3251
    """

    success = combination(k, x)
    failure = combination(pop - k, n - x)
    items = combination(pop, n)

    return round(success * failure / items, 4)

def negative_binomial_prob(x, r, p):
    xcr = combination(x-1, r-1)
    success = p ** r
    failure = (1 - p) ** (x - r)

    result = xcr * success * failure

    return round(result, 4)


def geometric_prob(x, p):
    failure = (1 - p) ** (x - 1)

    return round(p * failure, 4)


def poisson_prob(x, mu):
    e = 2.71828
    result = (e ** (-mu)) * (mu ** x) / factorial(x)

    return round(result, 4)


class Binomial():

    """
    x: The number of successes
    n: The number of trials
    P: The probability of success on an individual trial
    b(x; n, P): Binomial probability for exactly x sucesses
    b(a < x; n, P): Cumulative probability for a range of x
    cumulative: Boolean, specifies cumulative probability
    """

    def __init__(self, x, n, psuccess, cumulative=False):
        self.x = x
        self.n = n
        self.psuccess = psuccess
        self.cumulative = cumulative


    def prob(self):

        """
        b(x; n, P): Binomial probability for exactly x sucesses
        >>> given = Binomial(45, 100, 0.5)
        >>> given.prob()
        0.0485

        b(a < x; n, P): Cumulative probability for a range of x
        >>> given = Binomial(45, 100, 0.5, True)
        >>> given.prob()
        0.1358
        """

        try:
            if self.cumulative is False:
                return binomial_prob(self.x, self.n, self.psuccess)
            else:
                total = 0
                for i in range(0, self.x):
                    total += binomial_prob(i, self.n, self.psuccess)

                return round(total, 4)
        except:
            return 'Invalid inputs'


class Hypergeometric():

    """
    x: The number of items in the sample that are classified as successes
    pop: The number of items in the population
    n: The number of items in the sample
    k: The number of items in the population that are classified as successes
    h(x; N, n, k): Hypergeometric probability for exactly x successes
    cumulative: Boolean, specifies cumulative probability

    Random selection without replacement, prob of success changes on each trial
    """

    def __init__(self, x, pop, n, k, cumulative=False):
        self.x = x
        self.pop = pop
        self.n = n
        self.k = k
        self.cumulative = cumulative


    def prob(self):

        """
        >>> given = Hypergeometric(2, 52, 5, 26)
        >>> given.prob()
        0.3251
        """

        try:
            if self.cumulative is False:
                return hypergeometric_prob(self.x, self.pop, self.n, self.k)
            else:
                total = 0
                for i in range(0, self.x):
                    total += hypergeometric_prob(i, self.pop, self.n, self.k)

                return total
        except:
            return 'Invalid inputs'


class Multinomial():

    """
    n: The number of trials
    nk: The list of k possible outcomes
    pk: The list of probabilities of k possible outcomes

    Independent trials repeated n times with discrete outcomes and constant probs
    """

    def __init__(self, n, nk, pk):
        self.n = n
        self.nk = nk
        self.pk = pk


    def distribution(self):

        """
        >>> given = Multinomial(5, [1, 1, 1, 2], [0.25, 0.25, 0.25, 0.25])
        >>> given.distribution()
        0.0586
        """

        products_nk = 1
        products_pk = 1

        for i in range(len(self.pk)):
            products_nk *= factorial(self.nk[i])
            products_pk *= self.pk[i] ** self.nk[i]

        result = (factorial(self.n) / products_nk) * products_pk

        return round(result, 4)


class NegativeBinomial():

    """
    x: The number of trials required to produce r successes
    r: The number of successes
    p: The probability of success on an individual trial
    b*(x; r, P): Negative binomial probability, rth success on the xth trial

    Independent trials repeated x times with constant prob to produce r successes
    AKA Pascal distribution
    """

    def __init__(self, x, r, p):
        self.x = x
        self.r = r
        self.p = p


    def prob(self):

        """
        >>> given = NegativeBinomial(5, 3, 0.7)
        >>> given.prob()
        0.1852
        >>> given = NegativeBinomial(5, 1, 0.7)
        >>> given.prob()
        0.0057
        """

        if self.r == 1:
            return geometric_prob(self.x, self.p)
        else:
            return negative_binomial_prob(self.x, self.r, self.p)


class Poisson():

    """
    x: The actual number of successes that occur in a specified region
    mu: The average number of successes in a region (length, area, volume, time)
    P(x; μ): The Poisson probability that exactly x successes occur
    """

    def __init__(self, x, mu, cumulative=False):
        self.x = x
        self.mu = mu
        self.cumulative = cumulative


    def prob(self):

        """
        >>> given = Poisson(3, 2)
        >>> given.prob()
        0.1804
        >>> given = Poisson(4, 5, True)
        >>> given.prob()
        0.265
        """

        if self.cumulative is False:
            return poisson_prob(self.x, self.mu)
        else:
            total = 0
            for i in range(self.x):
                total += poisson_prob(i, self.mu)

            return total



if __name__ == '__main__':
    import pdb
    import doctest
    doctest.testmod()

    # Examples from https://stattrek.com/probability-distributions

    # Example exercises for Binomial Distribution:
    # 1. What is the probability of obtaining 45 or fewer heads in 100 tosses of a coin?
    given = Binomial(46, 100, 0.5, True)
    assert given.prob() == 0.1843

    # 2. The probability that a student is accepted to a prestigious college is 0.3.
    # If 5 students from the same school apply, what is the probability that at most 2 are accepted?
    given = Binomial(3, 5, 0.3, True)
    assert given.prob() == 0.8369

    # 3. What is the probability that the world series will last K games? Assume teams are evenly matched
    # Four games: Team A or Team B wins first 4 games in a row
    given = Binomial(4, 4, 0.5)
    assert given.prob() == 0.0625 # Total prob is 0.125 for both teams
    # Five games: Team A or Team B wins 3 of first 4 games then wins the 5th game
    given = Binomial(3, 4, 0.5)
    assert given.prob() == 0.25 # Each team has 0.5 chance to win 5th game, total prob is 0.25
    # Six games: Team A or Team B wins 3 of first 5 games then wins the 6th game
    given = Binomial(3, 5, 0.5)
    assert given.prob() == 0.3125 # Each team has 0.5 chance to win 6th game, total prob is 0.3125
    # Seven games: Team A or Team B wins 3 of first 6 games then wins the 7th game
    given = Binomial(3, 6, 0.5)
    assert given.prob() == 0.3125 # Each team has 0.5 chance to win 7th game, total prob is 0.3125


    # Example exercises for Hypergeometric Distribution:
    # 1. Select 5 cards without replacement from an ordinary deck of playing cards.
    # What is the probability of getting exactly 2 red cards (i.e., hearts or diamonds)?
    given = Hypergeometric(2, 52, 5, 26)  # 52 cards in a deck, 26 red cards
    assert given.prob() == 0.3251

    # 2. What is the probability of obtaining 2 or fewer hearts if we select 5 cards?
    given = Hypergeometric(3, 52, 5, 13, True)  # 52 cards in a deck, 13 heart cards
    assert given.prob() == 0.9072


    # Example exercises for Multinomial Distribution:
    # 1. What is the probability of drawing 1 spade, 1 heart, 1 diamond, and 2 clubs 
    # if drawn randomly 5 times with replacement?
    given = Multinomial(5, [1, 1, 1, 2], [0.25, 0.25, 0.25, 0.25])
    assert given.distribution() == 0.0586

    # 2. Four marbles were selected with replacement from 10 marbles - 2 red, 3 green, 5 blue.
    # What is the probability of selecting 2 green marbles and 2 blue marbles?
    given = Multinomial(4, [0, 2, 2], [0.2, 0.3, 0.5])
    assert given.distribution() == 0.135


    # Example exercises for Negative Binomial Distribution:
    # 1. What is the prob that a 70% FT shooter makes his third FT on his fifth shot?
    given = NegativeBinomial(5, 3, 0.7)
    assert given.prob() == 0.1852

    # 2. What is the prob that a 70% FT shooter makes his first FT on his fifth shot?
    given = NegativeBinomial(5, 1, 0.7)  # geometric distribution, special case for r=1
    assert given.prob() == 0.0057


    # Example exercises for Poisson Distribution:
    # 1. What is the probab that exactly 3 homes will be sold tomorrow if daily average is 2?
    given = Poisson(3, 2)
    assert given.prob() == 0.1804

    # 2. Suppose the average number of lions seen on a 1-day safari is 5.
    # What is the prob that tourists will see fewer than 4 lions on the next 1-day safari?
    given = Poisson(4, 5, True)
    assert given.prob() == 0.265


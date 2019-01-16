"""
Estimate the value of pi using Monte Carlo simulation

Given a square enclosing the upper right quadrant of a unit cirle,
randomly generate x,y pairs with values between 1 and 2,
assign pairs that fall inside the circle as hits, and
compute pi from: Area = pi * radius ^ 2
"""
import math
from random import random

import matplotlib.pyplot as plt


def estimate_pi(iterations):
    hits = 0
    pi_values = []
    for i in range(1, iterations):
        x = random()
        y = random()
        h = math.sqrt(x ** 2 + y ** 2)
        if h <= 1:
            hits += 1
        # The ratio of the area of a quarter of circle and square
        pi =  (float(hits) / i) * 4
        if (i % 1000 == 0):
            pi_values.append(pi)

    print('Value of pi after {} iterations: {}'.format(i + 1, pi))
    return pi_values

pi_values = estimate_pi(500000)
plt.plot(pi_values)
plt.xlabel('Iteration (in thousands)')
plt.ylabel('Ratio')
plt.show()
plt.close()

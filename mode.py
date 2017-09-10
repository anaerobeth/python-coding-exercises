"""
Given a set of n items, determine the mode (element that occurs the most number of times)
"""
from mergesort import sorter

def mode(given):
    """ Find the mode

    >>> print(mode([5, 9, 1, 3, 4, 4, 8]))
    4
    """
    arr = sorter(given)
    mode = arr[0]
    longest_run = 0
    runs = 0

    for n in range(len(arr)-1):
        if n < len(arr):
            diff = abs(arr[n] - arr[n+1])

            if diff == 0:
                runs += 1
                if longest_run < runs:
                    longest_run = runs
                    mode = arr[n]
            else:
                run = 0
    return mode

import doctest
doctest.testmod()

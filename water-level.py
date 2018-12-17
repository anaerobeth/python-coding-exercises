"""Find maximum amount of water that can be trapped between bars

Ex: [3, 0, 0, 2, 0, 4] holds 3 units at index 1, 2 and 4, and 1 unit at index 3
"""

import doctest
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
log = logging.info


def find_amount1(arr):

    """For each index, find the highest bars on left and right
    Amount of water: min(left, right) - current if positive
    O(n2)

    >>> arr = [3, 0, 0, 4, 0, 4]
    >>> find_amount1(arr)
    10
    """

    n = len(arr)
    water = 0
    for i in range(0, n):
        left_high = arr[0]
        right_high = arr[-1]
        for j in range(0, n):
            if (arr[j] > left_high and j < i):
                left_high = arr[j]
            if (arr[j] > right_high and j > i):
                right_high = arr[j]

        log(f"{i}: l={left_high} r={right_high} current={arr[i]}")
        diff = min(left_high, right_high) - arr[i]
        if diff > 0:
            water += diff
        log(f"water = {water}")

    return water


def find_amount2(arr):

    """Precompute the highest bars on left and right for each index
    Amount of water is min(left, right) - current
    O(n)

    >>> arr = [3, 0, 0, 4, 0, 4]
    >>> find_amount2(arr)
    10
    >>> find_amount2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    6
    """

    n = len(arr)
    left = [0] * n
    right = [0] * n
    water = 0

    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i-1], arr[i])

    # Walk backwards from next to last item
    # Avoid index out of bounds error on i+1
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], arr[i])

    for i in range(0, n):
        log(f"{i}: l={left} r={right} current={arr[i]}")
        water += min(left[i], right[i]) - arr[i]
        log(f"water={water}")

    return water


def find_amount3(arr):

    """"
    Similar to find_amount2 but keep high values as vars not in arrays
    Starting from first and last index, move pointers inward until they meet
    Track high values and add up water level at each step

    >>> find_amount3([3, 0, 0, 4, 0, 4])
    10
    >>> find_amount3([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    6
    """

    water = 0
    left_high = 0
    right_high = 0
    l_pointer = 0
    r_pointer = len(arr) - 1  # Avoid index out of bounds error on += 1

    while l_pointer < r_pointer:
        log(f"l_pointer={l_pointer} r_pointer={r_pointer}")
        if (arr[l_pointer] < arr[r_pointer]):
            if (arr[l_pointer] > left_high):
                log("New left high")
                left_high = arr[l_pointer]
            else:
                log(f"Adding water")
                water += left_high - arr[l_pointer]
            l_pointer += 1
        else:
            if (arr[r_pointer] > right_high):
                log("New right high")
                right_high = arr[r_pointer]
            else:
                log(f"Adding water")
                water += right_high - arr[r_pointer]
            r_pointer -= 1
        log(f"left_high={left_high} right_high={right_high}")
        log(f"water={water}")
    log('END')

    return water


if __name__ == '__main__':
    doctest.testmod()

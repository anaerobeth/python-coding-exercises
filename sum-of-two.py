"""
Find the indices of two integers that sum up to k

arr = [1, 3, 5, 8]
k = 6
Return (0, 2)
"""

import logging

def sum_of_two(integers, total):
    """
    Brute force - Time complexity O(n^2), Space complexity O(1)
    Looping twice and summing until k is found (Not implemented)

    Single pass - Time complexity O(n), Space complexity O(n)
    Subtract int from k, save the diff as key, index as value in matches
    If next int is a key in matches, return the int index and looked up value
    """

    try:
        matches = {}
        for index, num in enumerate(integers):
            print(num)
            if isinstance(num, int):
                diff = total - num
                logging.info('Looking for', diff, 'in', matches)
                if diff not in matches:
                    matches[num] = index
                else:
                    return (index, matches[diff])
            else:
                pass
        logging.info('No pairs that sum up to {} were found'.format(total))
    except TypeError:
        logging.warning('Invalid inputs')


def test_sum_found():
    arr = [1, 3, 5, 8]
    k = 6
    assert(sum_of_two(arr, k) == (2, 0))

def test_sum_not_found():
    arr = [1, 3, 5, 8, 15, 32, 25]
    k = 10
    assert(sum_of_two(arr, k) == None)

def test_sum_found_with_validation():
    arr = ['a', 1, 3, 5, 8]
    k = 6
    print(sum_of_two(arr, k) == (3, 1))

def test_sum_warning():
    arr = [5, 1, 2]
    k = 'a'
    assert(sum_of_two(arr, k) == None)


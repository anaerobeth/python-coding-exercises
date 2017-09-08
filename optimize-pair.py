"""
Given 2n real numbers, partitions the numbers into pairs
such that the maximum sum of pairs is minimized
"""

def merge(left, right, reverse=False):
    arr = []
    while left and right:
        if reverse:
            if left[0] > right[0]:
                arr.append(left.pop(0))
            else:
                arr.append(right.pop(0))
        else:
            if left[0] < right[0]:
                arr.append(left.pop(0))
            else:
                arr.append(right.pop(0))
    arr += left + right

    return arr


def sorter(arr, reverse=False):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = sorter(arr[:mid])
    right = sorter(arr[mid:])

    if reverse:
        sorted_arr = merge(left, right, reverse=True)
    else:
        sorted_arr = merge(left, right)

    return sorted_arr


def pair_up(arr):
    mid = len(arr) // 2
    pairs = []

    left = arr[:mid]
    right = sorter(arr[mid:], reverse=True)

    while left and right:
        pair = (left.pop(0), right.pop(0))
        pairs.append(pair)

    return pairs


given = [5, 9, 1, 3, 4, 8]

print(pair_up(sorter(given)))



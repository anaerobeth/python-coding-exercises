"""
Given a set of n items, determine the median and kth largest element in the set
"""
from mergesort import sorter

def median(given):
    arr = sorter(given)

    return arr[len(given) // 2]


def kth_largest(k):
    arr = sorter(given, reverse=True)

    return arr[k-1]


given = [5, 9, 1, 3, 7, 2, 4, 1, 8]

print(median(given))
print(kth_largest(1))
print(kth_largest(3))


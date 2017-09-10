"""
Given a set of n items, determine if there are duplicates
"""
from mergesort import sorter

def with_duplicates(given):
    arr = sorter(given)

    for n in range(len(arr)-1):
        if n < len(arr):
            diff = abs(arr[n] - arr[n+1])

            if diff == 0:
                return True
            else:
                continue
    return False


given = [5, 9, 1, 3, 9, 4, 8]
print(with_duplicates(given))



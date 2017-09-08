"""
Given n numbers, find the pair which are closest to each other
"""
from mergesort import sorter

def find_closest_pair(given):
    arr = sorter(given)
    closest_pair = ()
    smallest_diff = abs(arr[0] - arr[1])

    for n in range(len(arr)-1):
        print(smallest_diff)
        if n < len(arr):
            diff = abs(arr[n] - arr[n+1])

            if diff < smallest_diff:
                smallest_diff = diff
                closest_pair = (arr[n], arr[n+1])

    return closest_pair

given = [5, 9, 1, 3, 4, 8]
print(find_closest_pair(given))


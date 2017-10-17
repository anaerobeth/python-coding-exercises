"""Given a sorted list, return the index of the target element"""

import math

def search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = math.floor(left + (right - left) / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
    return -1


arr = [1, 4, 5, 8, 10]
print(search(arr, 9))
assert(search(arr, 4)) == 1
assert(search(arr, 16)) == -1


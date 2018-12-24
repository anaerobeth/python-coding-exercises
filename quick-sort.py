"""
Optimize quicksort
Adapted from https://yourbasic.org/golang/quicksort-optimizations/

1. Pick a good pivot
2. Partition the array such that p divides elements in order
3. Recursively apply 1 and 2 to sublists of elements
"""

from random import randint

def partition(arr, low, high):
    # Reorder array elements so that p is middle
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

    return arr



if __name__ == '__main__':
    import doctest
    doctest.testmod()

    arr1 = [2, 1, 3]
    n = len(arr1)
    print(quick_sort(arr1, 0, n-1))

    arr2 = [10, 7, 8, 9, 1, 5]
    n = len(arr2)
    print(quick_sort(arr2, 0, n-1))

    arr3 = [2, 1, 3, 10, 12, 11, 14, 4, 5, 6, 7, 8, 9, 15, 17, 20, 16, 18, 19, 13]
    n = len(arr3)
    print(quick_sort(arr3, 0, n-1))


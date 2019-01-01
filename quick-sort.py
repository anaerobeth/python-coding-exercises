"""
Optimize quicksort
Adapted from https://yourbasic.org/golang/quicksort-optimizations/

1. Pick a good pivot
2. Partition the array such that p divides elements in order
3. Recursively apply 1 and 2 to sublists of elements
4. For short sublists, use insertion sort (faster for small lists)
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

def optimized_quick_sort(arr):
    if len(arr) < 20:
        return insertion_sort(arr)
    p = pivot(arr)
    low, high = optimized_partition(arr, p)
    optimized_quick_sort(arr[:low])
    optimized_quick_sort(arr[high:])

    return arr

def optimized_partition(arr, p):
    # Reorder array elements so that p is middle
    low, high = 0, len(arr)
    mid = 0

    while mid < high:
        temp = arr[mid]
        if temp < p:
            arr[mid], arr[low] = arr[low], temp
            low += 1
            mid +=1
        elif temp == p:
            mid += 1
        else:
            import pdb
            pdb.set_trace()
            arr[mid], arr[high-1] =  arr[high-1], temp
            high += 1
        if high == len(arr):
            return low, high

    return low, high

def insertion_sort(arr):
    for j in range(len(arr)):
        key = arr[j]
        i = j - 1
        while (i >= 0) and (arr[i] > key):
            arr[i+1] = arr[i]
            i -= 1

        arr[i+1] = key

    return arr


def pivot(arr):
    n = len(arr)
    med = median(arr[randint(0, n)], arr[randint(0, n)], arr[randint(0, n)])

    return med

def median(a, b, c):
    if a < b:
        if b < c:
            return b
        elif a < c:
            return c
        else:
            return a
    if a < c:
        return a
    elif b < c:
        return c
    else:
        return b


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    arr1 = [2, 1, 3]
    n = len(arr1)
    print(quick_sort(arr1, 0, n-1))
    print(optimized_quick_sort(arr1))

    arr2 = [10, 7, 8, 9, 1, 5]
    n = len(arr2)
    print(quick_sort(arr2, 0, n-1))
    print(optimized_quick_sort(arr2))

    arr3 = [2, 1, 3, 10, 12, 11, 14, 4, 5, 6, 7, 8, 9, 15, 17, 20, 16, 18, 19, 13]
    n = len(arr3)
    print(quick_sort(arr3, 0, n-1))
    print(optimized_quick_sort(arr3))


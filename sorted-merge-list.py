"""
Return a new sorted merged list from K sorted lists of size N
Adapted from Daily Coding Problem exercise:
    How To Solve a Hard Programming Interview Question

>>> arr = [[1, 2], [ 10, 20], [5, 6]]
>>> flatten_merge_sorted(arr)
[1, 2, 5, 6, 10, 20]
>>> merge_sorted(arr)
[1, 2, 5, 6, 10, 20]
"""

import heapq

def flatten(arr):
    flat_list = []
    for sublist in arr:
        for item in sublist:
            flat_list.append(item)
    return flat_list



def flatten_merge_sorted(arr):

    """Flatten then sort - O(kn log kn)"""

    if len(arr) == 0:
        return 'Empty array'
    flat_list = flatten(arr)

    return sorted(flat_list)


def initialize_heap(arr):
    # Create tuples for (value, list index, element index)
    heap = []
    for i, el in enumerate(arr):
        heap.append((el[0], i, 0))
    heapq.heapify(heap)

    return heap


def merge_sorted(arr):

    """Assumes arr has k lists that are sorted and of same size
    Find smallest element and append to heap - O(kn log k)
    Neek k tuples for (value, list index, element index)
    Extract minimum from heap then add next tuple until heap is empty
    """

    merged_list = []
    heap = initialize_heap(arr)

    while heap:
        # Pop smallest item from heap
        val, li, ei = heapq.heappop(heap)
        merged_list.append(val)

        # Push next_tuple from sublist to heap if present
        if ei + 1 < len(arr[li]):
            next_tuple = (arr[li][ei+1], li, ei+1)
            heapq.heappush(heap, next_tuple)

    return merged_list


if __name__ == '__main__':
    import doctest
    doctest.testmod()

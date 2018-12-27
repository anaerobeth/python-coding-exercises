"""
Return a new sorted merged list from K sorted lists of size N

Adapted from https://dxmahata.gitbooks.io/leetcode-python-solutions/merge_k_sorted_linked_lists.html

>>> a = Node('a')
>>> b = Node('b')
>>> a.set_next(b)
>>> c = Node('c')
>>> d = Node('d')
>>> c.set_next(d)
>>> merge_sorted([a, c])
['a', 'b', 'c', 'd']
"""

import heapq

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, new_next):
        self.next = new_next


def merge_sorted(arr):

    """Assumes arr has k linked lists that are sorted and of same size
    Find smallest element and append to heap - O(kn log k)
    Need k tuples for (node value, list index, node)
    Extract minimum from heap then add next tuple until heap is empty
    """

    merged_list = []
    heap = []

    # Initialize heap with tuples for first nodes from each linked list
    for i in range(len(arr)):
        if arr[i] != None:
            # Push next_tuple from sublist to heap if present
            next_tuple = (arr[i].val, i, arr[i])
            heapq.heappush(heap, next_tuple)

    while heap:
        # Pop smallest item from heap and add to merged_list
        val, li, node = heapq.heappop(heap)
        merged_list.append(val)

        # Push next_tuple from sublist to heap if present
        if node.next != None:
            next_tuple = (node.next.val, li, node.next)
            heapq.heappush(heap, next_tuple)

    return merged_list


if __name__ == '__main__':
    import doctest
    doctest.testmod()

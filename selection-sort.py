"""
Implement Selection Sort

O(n^2) for list or unsorted linked lists, O(n logn) for bst or heaps
"""

def selection_sort(given):

    """
    Repeatedly scan a given list, move the smallest to new list until empty
    f(l) := { n = []; n.append(min(l)) until empty(l) }


    >>> selection_sort([1, 2, 4, 7, 1, 3, 5, 8, 9])
    [1, 1, 2, 3, 4, 5, 7, 8, 9]
    """
    sorted_list = []

    while len(given) > 0:
        smallest = min(given)
        sorted_list.append(smallest)
        given.remove(smallest)

    return sorted_list


def selection_sort_in_place(given):

    """
    Set pointer at start of a given list, set its value as smallest
    Scan the rest to find the smallest, swap it with item in pointer if smaller
    Move pointer and repeat until pointer reaches the end of list

    f(l) := { s = l[0]; (s = n if s < n for n in l; s_index = p + n + 1
        l[p], l[s_index]  = s, l[p] if s < l[p]) for p in range(n) }

    >>> selection_sort_in_place([4, 2, 1, 7, 6, 3, 5, 8, 9])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> selection_sort_in_place([4, 2, 1, 1])
    [1, 1, 2, 4]
    """

    for p in range(len(given)):
        smallest = given[p]
        for index, n in enumerate(given[p+1:]):
            if n < smallest:
                smallest = n
                smallest_index = p + index + 1
        if smallest < given[p]:
            given[p], given[smallest_index] = smallest, given[p]

    return given

if __name__ == '__main__':
    import doctest
    doctest.testmod()

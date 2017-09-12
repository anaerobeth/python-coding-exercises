"""
Implement Selection Sort
Repeatedly scan the list to find the smallest remaining element
O(n^2) for list or unsorted linked lists, O(n logn) for bst or heaps
"""

def selection_sort(given):
    sorted_list = []

    while len(given) > 0:
        smallest = min(given)
        sorted_list.append(smallest)
        given.remove(smallest)

    return sorted_list

given = [1, 2, 4, 7, 1, 3, 5, 8, 9]
print(selection_sort(given))


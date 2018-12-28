"""
Count the number of inversions in an array and display all the inverted pairs

Adapted from https://medium.com/@ssbothwell/counting-inversions-with-merge-sort-4d9910dc95f0 and modified to list all inverted pairs
"""

def merge_sort(arr):

    """
    >>> merge_sort([1, 3, 4, 2])
    ([1, 2, 3, 4], 2, [(4, 2), (3, 2)])
    """

    if len(arr) == 1:
        return arr, 0, []
    else:
        left, l_inversions, r_pairs = merge_sort(arr[:len(arr)//2])
        right, r_inversions, l_pairs = merge_sort(arr[len(arr)//2:])

        sorted_arr = []
        i = 0
        j = 0
        inversions = 0 + l_inversions + r_inversions
        pairs = [] + r_pairs + l_pairs

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                # Inversion found: increment count and add inverted pairs
                # Inversion applies to all remaining items in left
                inversions += len(left) - i
                for k in range(i, len(left)):
                    pairs.append((left[k], right[j]))

                sorted_arr.append(right[j])
                j += 1

        sorted_arr += left[i:] + right[j:]

        return sorted_arr, inversions, pairs


def inversions(given):

    """
    >>> inversions([3, 2, 1])
    Inversions: 3
    Inverted pairs: [(2, 1), (3, 1), (3, 2)]

    >>> inversions([6, 5, 4, 3, 2, 1])
    Inversions: 15
    Inverted pairs: [(5, 4), (6, 4), (6, 5), (2, 1), (3, 1), (3, 2), (4, 1), (5, 1), (6, 1), (4, 2), (5, 2), (6, 2), (4, 3), (5, 3), (6, 3)]

    """

    _, inversions, pairs = merge_sort(given)
    print(f"Inversions: {inversions}")
    print(f"Inverted pairs: {pairs}")



if __name__ == '__main__':
    import pdb
    import doctest
    doctest.testmod()


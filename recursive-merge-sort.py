"""
Merge two sorted lists

Compare the first items in each list, move the lower to the combined list
If one list is empty, add the remaining list to the combined list
Repeat until both lists are empty and return the combined list

f(l, r, c) := { c = [] if c = None; c if empty(l) and empty(r);
    c.extend(l), c if empty(r); c.extend(r), c if empty(l);
    c.append(l.pop())if l[0] < r[0] else c.append(r.pop(0));
    f(l, r, c) }


>>> merge([2, 4, 7, 8], [1, 3, 5, 6])
[1, 2, 3, 4, 5, 6, 7, 8]
"""

def is_empty(l):
    return len(l) == 0


def merge(left, right, combined=None):
    if combined is None:
        combined = []

    if is_empty(left) and is_empty(right):
        return combined

    if is_empty(right):
        combined.extend(left)
        return combined

    if is_empty(left):
        combined.extend(right)
        return combined

    if left[0] < right[0]:
        combined.append(left.pop(0))
    else:
        combined.append(right.pop(0))

    merge(left, right, combined)

    return combined


if __name__ == '__main__':
    import doctest
    doctest.testmod()

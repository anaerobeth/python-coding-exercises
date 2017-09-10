def merge(left, right, reverse=False):
    arr = []

    while left and right:
        if reverse:
            if left[-1] > right[-1]:
                arr.append(left.pop(-1))
            else:
                arr.append(right.pop(-1))
        else:
            if left[0] < right[0]:
                arr.append(left.pop(0))
            else:
                arr.append(right.pop(0))
    arr += left + right

    return arr


def sorter(arr, reverse=False):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = sorter(arr[:mid])
    right = sorter(arr[mid:])

    if reverse:
        sorted_arr = merge(left, right, reverse=True)
    else:
        sorted_arr = merge(left, right)

    return sorted_arr

# given = [1, 2, 4, 7, 8, 1, 3, 5, 9]
# print(sorter(given))
# print(sorter(given, reverse=True))


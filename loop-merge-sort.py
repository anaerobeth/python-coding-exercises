def merge(left, right):
    combined = []
    while left and right:
        if left[0] < right[0]:
            # Python lists are optimized for fast fixed-length ops of O(n) memory cost
            # Use deque for fast appends and pops on either end at O(1) cost, but slows to O(n) in the middle
            combined.append(left.pop(0))
        else:
            combined.append(right.pop(0))
    combined += left
    combined += right

    return combined


def merge_sort(unsorted):
    if len(unsorted) < 2:
        return unsorted

    midpoint = len(unsorted) // 2
    left = merge_sort(unsorted[:midpoint])
    right = merge_sort(unsorted[midpoint:])

    sorted = merge(left, right)

    return sorted

f = open('random_integers.txt', 'r')
random_integers = [int(line) for line in f.readlines()]

random_sorted = merge_sort(random_integers)
print(random_sorted)



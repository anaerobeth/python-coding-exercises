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

sorted_list_1 = [2, 4, 7, 8]
sorted_list_2 = [1, 3, 5, 6]

print(merge(sorted_list_1, sorted_list_2))

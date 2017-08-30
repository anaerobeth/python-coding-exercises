"""
Merge two sorted lists
"""

def merge(left, right, combined=None):
    if combined is None:
        combined = []

    if len(left) == 0 and len(right) == 0:
        return combined

    if len(right) == 0:
        combined.extend(left)
        return combined

    if len(left) == 0:
        combined.extend(right)
        return combined

    if left[0] < right[0]:
        combined.append(left[0])
        left = left[1:]
    else:
        combined.append(right[0])
        right = right[1:]

    merge(left, right, combined)

    return combined

sorted_list_1 = [2, 4, 7, 8]
sorted_list_2 = [1, 3, 5, 6]

print(merge(sorted_list_1, sorted_list_2))
# [1, 2, 3, 4, 5, 6, 7, 8]

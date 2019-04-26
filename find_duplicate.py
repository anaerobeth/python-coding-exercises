"""
Given an array of length n + 1 from the set {1, 2, ..., n},
find the duplicate in linear time and space
"""

def find_dup(arr):
    # Loop through the list and create a dict with items as keys
    # If item is an existing key in the dict, return as duplicate

    temp = {}
    for item in arr:
        if item in temp:
            print('Found duplicate item: {}'.format(item))
        else:
            temp[item] = 1

def find_dup2(arr):
    for item in arr:
        pos_item = abs(item)
        if pos_item == len(arr):
            el = -1
        else:
            el = arr[pos_item]

        if el > 0:
            arr[pos_item] = -el
        elif el == 0:
            arr[pos_item] = -len(arr)
        else:
            if arr[pos_item] == len(arr):
                print('Found duplicate item: {}'.format(0))
            else:
                print('Found duplicate item: {}'.format(pos_item))



if __name__ == '__main__':
    arr = [4, 1, 3, 2, 1]

    find_dup(arr)
    find_dup2(arr)




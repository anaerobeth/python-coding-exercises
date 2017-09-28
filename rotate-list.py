def rotate(arr, step, reverse=False):
    """ Return a list that has been rotated the required number of steps """
    if reverse:
        """ Rotating in reverse is the same as rotating the number of steps less than the length of the list"""
        step = len(arr) - step
    return (arr + arr[:step])[step:]

arr = [1, 2, 3, 4, 5]
assert rotate(arr, 1) == [2, 3, 4, 5, 1]
assert rotate(arr, 3) == [4, 5, 1, 2, 3]
assert rotate(arr, 1, reverse=True) == [5, 1, 2, 3, 4]
assert rotate(arr, 2, reverse=True) == [4, 5, 1, 2, 3]

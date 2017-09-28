def rotate(arr, step):
    """ Return a list that has been rotated the required number of steps """
    if type(step) == int:
        if step == 0:
            return arr

        if step < 0:
            """ Rotating in reverse is the same as rotating the number of steps less than the length of the list"""
            step = len(arr) + step # step is negative
            print(step)

        return (arr + arr[:step])[step:]
    else:
        print('Invalid input')



arr = [1, 2, 3, 4, 5]
assert rotate(arr, 1) == [2, 3, 4, 5, 1]
assert rotate(arr, 3) == [4, 5, 1, 2, 3]
assert rotate(arr, 0) == [1, 2, 3, 4, 5]
assert rotate(arr, -1) == [5, 1, 2, 3, 4]
assert rotate(arr, -2) == [4, 5, 1, 2, 3]

def rotate(arr, step=None):
    """ Return a list that has been rotated the required number of steps """
    try:
        if int(step) == 0:
            return arr

        if int(step) < 0:
            """ Rotating in reverse is the same as rotating the number of steps less than the length of the list"""
            step = len(arr) + step # step is negative
            print(step)

        return (arr + arr[:step])[step:]
    except ValueError:
        return 'Please provide a step'
    except:
        return 'Invalid input'



arr = [1, 2, 3, 4, 5]
assert rotate(arr, 1) == [2, 3, 4, 5, 1]
assert rotate(arr, 3) == [4, 5, 1, 2, 3]
assert rotate(arr, 0) == [1, 2, 3, 4, 5]
assert rotate(arr, -1) == [5, 1, 2, 3, 4]
assert rotate(arr, -2) == [4, 5, 1, 2, 3]
print(rotate(arr, 2.0))
print(rotate(arr, 'foo'))
print(rotate(arr))

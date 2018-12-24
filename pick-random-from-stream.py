"""
Pick one or more random elements from a stream

Avoid storing all elements - should not need O(n) space
Instead, adjust probability of picking a random element
as more elements are read in from the stream - O(1) space
"""

from random import randint

def pick(stream, size=None):
    if size == None:
        size = 1


    if size == 1:
        result = None
        for i, el in enumerate(stream):
            if i == 0:
                result = el
            if randint(1, i+1) == 1:
                result = el
        return result
    else:
        result = [None] * size
        for i, el in enumerate(stream):
            if i == 0:
                result[0] = el
            if randint(1, i+1) == 1:
                if any(item is None for item in result):
                    index = result.index(None)
                else:
                    index = randint(0, size-1)
                result[index] = el
        return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    stream = [1, 5, 10, 15, 3, 21, 7, 12, 14, 3]
    print(pick(stream))
    print(pick(stream, 3))

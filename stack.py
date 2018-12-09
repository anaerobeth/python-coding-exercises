"""Implement Stack

>>> Stack([1, 2, 5]).isEmpty()
False
>>> Stack([1, 2, 5]).push(6)
[1, 2, 5, 6]
>>> Stack([1, 2, 5]).pop()
5
>>> Stack([1, 2, 5]).peek()
5
>>> Stack([1, 2, 5]).size()
3
"""

class Stack():
    def __init__(self, l=None):
        self._container = [] if l == None else l

    def isEmpty(self):
        return len(self._container) == 0

    def push(self, item):
        self._container.append(item)
        return self._container

    def pop(self):
        return self._container.pop()

    def peek(self):
        return self._container[-1]

    def size(self):
        return len(self._container)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

"""Implement Stack

>>> Stack([1, 2, 5]).is_empty()
False
>>> Stack([1, 2, 5]).push(6)
[1, 2, 5, 6]
>>> Stack([1, 2, 5]).pop()
5
>>> Stack([1, 2, 5]).peek()
5
>>> Stack([1, 2, 5]).size()
3
>>> print(Stack([1, 2, 5]))
[1, 2, 5]
>>> Stack([1, 2, 5]).sorted()
True
"""

class Stack():
    def __init__(self, l=None):
        self._container = [] if l == None else l

    def is_empty(self):
        return len(self._container) == 0

    def push(self, item):
        self._container.append(item)
        return self._container

    def pop(self):
        if not self.is_empty() :
            return self._container.pop()

    def peek(self):
        if self.is_empty():
            return 0
        else:
            return self._container[-1]

    def size(self):
        return len(self._container)

    def __repr__(self):
        return repr(self._container)

    def sorted(self):
        last = self._container[0]
        for item in self._container:
            if item < last:
                return False
            else:
                last = item
        return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()

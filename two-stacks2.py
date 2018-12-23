"""
Implement two stacks in one array

Given a fixed number of elements, add elements of the first stack to
the front of the array but add elements of the second stack to the back

Pushing new elements to indexed positions for constant time operations

>>> ts = TwoStacks(5)
>>> ts.push1(1)
>>> ts.push1(2)
>>> ts.push1(3)
>>> print(ts)
array([1, 2, 3, 0, 0])
>>> ts.push2(4)
>>> ts.push2(5)
>>> print(ts)
array([1, 2, 3, 5, 4])
>>> ts.push2(6)
'Stack Overflow'
>>> print(ts.pop1())
3
>>> print(ts.pop2())
5
>>> print(ts.pop2())
4
>>> print(ts.pop2())
Stack Underflow
>>> print(ts)
array([1, 2, 3, 5, 4])
"""


import numpy as np


class TwoStacks():

    def __init__(self, n):
        self.size = n
        self.arr = np.zeros([n], dtype=int)
        self.top1 = -1  # first stack will start at the front of the array
        self.top2 = self.size  # second stack will start at the back af the array


    def _has_empty_space(self):
        # Check if there is a space for new element
        return self.top1 < self.top2 - 1


    def push1(self, value):
        # First stack starts at the front of the array, so move top pointer forwards
        if self._has_empty_space():
            self.top1 += 1
            self.arr[self.top1] = value
        else:
            return 'Stack Overflow'


    def push2(self, value):
        # Second stack starts at the end of the array, so move top pointer backwards
        if self._has_empty_space():
            self.top2 -= 1
            self.arr[self.top2] = value
        else:
            return 'Stack Overflow'


    def pop1(self):
        # Move top pointer towards the front of array
        if self.top1 >= 0:
            front = self.arr[self.top1]
            self.top1 -= 1
            return front
        else:
            return 'Stack Underflow'


    def pop2(self):
        # Move top pointer backwards to end of array
        if self.top2 < self.size:
            back = self.arr[self.top2]
            self.top2 += 1
            return back
        else:
            return 'Stack Underflow'


    def __repr__(self):
        return repr(self.arr)


if __name__ == '__main__':
    import doctest
    doctest.testmod()


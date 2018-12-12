"""
Check if an integer is in a sorted list of integers

>>> l = SortedList(2, 5, 8, 1)
>>> l.included(2)
True
>>> l.included(0)
False
"""

class SortedList():
    def __init__(self, *args):
        self.items = sorted([item for item in args])

    def included(self, integer):
        for item in self.items:
            if item == integer:
                return True
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()

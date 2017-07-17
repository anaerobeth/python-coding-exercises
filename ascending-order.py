"""
Check if an integer is in a sorted list of integers
"""

class SortedList():
    def __init__(self, *args):
        self.items = []
        for arg in args:
            self.items.append(arg)
        self.items = sorted(self.items)
        print(self.items)

    def included(self, integer):
        found = False
        for item in self.items:
            if item == integer:
                found = True
        return found

l = SortedList(2, 5, 8, 1)
print(l.included(2))
print(l.included(0))






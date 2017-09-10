"""
Loop over a sequence backwards
"""

class Reverse():
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        """Add iterator behavior to the class"""
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

    def reverse(self):
        """Implement reverse using generators"""
        for i in range(self.index-1, -1, -1):
            yield self.data[i]

# Using iterators
rev = Reverse('spam')
iter(rev)
for char in rev:
    print(char)

# Using generators
g = Reverse('golf')
for char in g.reverse():
    print(char)


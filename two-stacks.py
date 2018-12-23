"""
Implement two stacks in one array

>>> ts = TwoStacks()
>>> ts.push1('x')
>>> ts.push1('y')
>>> ts.push2('a')
>>> ts.push2('b')
>>> print(ts.pop1())
y
>>> print(ts.pop2())
b
>>> print(ts.pop2())
a
>>> print(ts.pop2())
Empty stack
>>> print(ts.pop2())
Empty stack
"""

class TwoStacks():

    def __init__(self):
        self._container = ['|']  # boundary between stacks


    def push1(self, value):
        self._container.append(value)


    def push2(self, value):
        self._container = [value] + self._container


    def peek1(self):
        return self._container[-1]


    def peek2(self):
        return self._container[0]


    def pop1(self):
        back = self.peek1()
        if back ==  '|':
            return 'Empty stack'
        back = self._container.pop()
        return back


    def pop2(self):
        front = self.peek2()
        if front ==  '|':
            return 'Empty stack'
        front = self._container.pop(0)
        return front


if __name__ == '__main__':
    import doctest
    doctest.testmod()



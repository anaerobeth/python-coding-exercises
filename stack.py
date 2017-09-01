class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[:-1]

    def size(self):
        return len(self.items)

s = Stack()
s.push(1)
s.push(2)
print(s.size())
s.peek()
print(s.size())
s.pop()
print(s.size())


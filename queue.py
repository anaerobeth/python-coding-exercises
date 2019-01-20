"""
Implement Queue data structure

Linear Queue - First in, first out. Insert at the back.
Circular Queue - Connected. Front and rear diverge.
Priority Queue - Higher priority goes to the front.
Can implemented with list, linked list or queue

>>> queue = Queue()
>>> queue.enqueue(2)
>>> queue.enqueue(4)
>>> print(queue)
[2, 4]
>>> queue.front()
2
>>> queue.back()
4
>>> queue.dequeue()
2
"""

class Queue():

    def __init__(self, l=None):
        self._container = [] if l == None else l


    def is_empty(self):
        return True if len(self._container) == 0 else False


    def front(self):
        if self.is_empty():
            return None
        return self._container[0]


    def back(self):
        if self.is_empty():
            return None
        return self._container[-1]


    def size(self):
        return len(self._container)


    def enqueue(self, value):
        self._container.append(value)


    def dequeue(self):
        if self.is_empty():
            return None
        front = self.front()
        self._container = self._container[1:]
        return front


    def __repr__(self):
        return repr(self._container)


if __name__ == '__main__':
    import doctest
    doctest.testmod()


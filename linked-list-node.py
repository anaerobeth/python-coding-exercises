class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next



class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert_at_head(self, data):
        # set data as head and point next to the old head
        old_head = self.head
        self.head = data
        self.head.next_node = old_head

    def size(self):
        # count how many nodes found by looking at next nodes
        node_count = 0
        target = self.head
        while target:
            target = target.next_node
            node_count += 1

        return node_count

    def search(self, data):
        # keep looking at next nodes until a match is found
        target = self.head
        found = False
        while target and found is False:
            if data == target.data:
                found = True
            else:
                target = target.next_node

        return 'Not found' if target is None else 'Found'

    def delete(self, data):
        # look at next nodes while saving previous node visited
        # when a match is found, set previous node's next to data
        previous = None
        target = self.head
        found = False

        while target and found is False:
            if data == target.data:
                found = True
                previous.next_node = target.next_node
            else:
                previous, target = target, target.next_node

        return "One node deleted. The new node size is {}.".format(self.size()) if found else "Data for deletion not found in the list."


a = Node('A')
b = Node('B')
c = Node('C')

a.set_next(b)
b.set_next(c)

k = LinkedList(a)
assert(k.head.data) == 'A'

d = Node('D')
k.insert_at_head(d)
assert(k.head.data) == 'D'
assert(k.head.next_node.data) == "A"

assert(k.size()) == 4
assert(k.search('B')) == 'Found'
assert(k.search('Q')) == 'Not found'

assert(k.delete('X')) == 'Data for deletion not found in the list.'
assert(k.delete('B')) == 'One node deleted. The new node size is 3.'

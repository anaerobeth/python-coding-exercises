"""
Implement a linked list structure that supports basic operations
orig_linked_list = ((10), (10->20), (20->30), (30->40), (40->50)
item_to_search = 50
item_to_insert = 15
insert_after = 10
item_to_delete = 40
item_to_merge = 60
item_to_update = 50
item_replacement = 99
"""

class LinkedListNode(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return self.value


class MyLinkedList(object):

    def __init__(self, *args):
        self.length = 0
        self.head = None
        self.nodes = []
        target_node, prev_node = None, None

        # create a node for each argument passed
        for index, arg in enumerate(args):
            target_node = prev_node
            current_node = LinkedListNode(arg)
            self.nodes.append(current_node)

            if index == 0:
                self.head = current_node
            else:
                # after creating the head node, set the `next` property
                # to the previously created target node
                target_node.next = current_node
                print("Node {} is followed by Node {}".format(target_node.value, target_node.next.value))

            # the current value will be the previous value in
            # succeeding rounds
            prev_node = current_node


    def __str__(self):
        nodes = []
        for node in self.nodes:
            nodes.append(node.__str__())
        return nodes


    def _search(self, node):
        result = [True for i in self.__str__() if i == node]
        return "Not found" if not result else "Found"


    def _traverse(self, node):
        nodes = []
        while node:
            nodes = node.value
            node = node.next
        return nodes


    def _insert(self, node, parent):
        for i in self.nodes:
            if i.value == parent:
                current_node = LinkedListNode(node, next = i.next)
                i = current_node
                print(current_node.__str__(), current_node.next.value)
        return self.__str__()


    def _delete(self, node):
        pass

    def _merge(self, node, link):
        pass

    def _update(self, new_node, link):
        pass


l = MyLinkedList(10, 20, 30, 40, 50)
assert(l.__str__()) == [10, 20, 30, 40, 50]
assert(l._search(20)) == "Found"
assert(l._search(99)) == "Not found"
print(l._insert(15, 10))
# assert(l._insert(15, 10)) == [10, 15, 20, 30, 40, 50]
# assert(l._delete(40)) == [10, 20, 30, 50]
# assert(l._delete(99)) == [10, 20, 30, 40, 50]
# assert(l._merge(60)) == [10, 20, 30, 40, 50, 60]
# assert(l._update(99, 5)) == [10, 20, 30, 40, 99]

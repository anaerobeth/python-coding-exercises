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


class MyLinkedList(object):

    def __init__(self, *args):
        target_node, prev_node = None, None
        for index, arg in enumerate(args):
            target_node = prev_node
            current_node = LinkedListNode(arg)
            if index != 0:
                target_node.next = current_node
            prev_node = current_node
            # print("Current node is: ", current_node.value)
            if index != 0:
                print("Node {} is followed by Node {}".format(target_node.value, target_node.next.value))


    def _traverse(self):
        pass

    def _search(self, node):
        pass

    def _insert(self, node, parent):
        pass 

    def _delete(self, node):
        pass

    def _merge(self, node, link):
        pass

    def _update(self, new_node, link):
        pass


l = MyLinkedList(10, 20, 30, 40, 50)
# assert(l._traverse()) == [10, 20, 30, 40, 50]
# assert(l._search(20)) == "Found"
# assert(l._search(99)) == "Not found"
# assert(l._insert(15, 2)) == [10, 15, 20, 30, 40, 50]
# assert(l._delete(40)) == [10, 20, 30, 50]
# assert(l._delete(99)) == [10, 20, 30, 40, 50]
# assert(l._merge(60)) == [10, 20, 30, 40, 50, 60]
# assert(l._update(99, 5)) == [10, 20, 30, 40, 99]

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None


def delete_node(node_to_delete):
    next_node = node_to_delete.next

    if next_node:
        node_to_delete.value = next_node.value
        node_to_delete.next = next_node.next
    else:
        raise Exception("Can't delete the last node")


def contains_cycle(first_node):
    """ Loop through each node to check is current node is a visited node
    Add to set or return False if end of the list is reached 
    Runtime is O(n) and space cost is O(n)
    Improves to O(1) if storing a constant number of nodes
    Use Fast and slow runners as landmarks
    """
    pass


a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

delete_node(b)

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BaseBinaryTree:
    def __init__(self, values=None):
        self.root = None
        if values:
            self.insert(values)

    def insert(self, values, index=0):
        node = None
        if index < len(values):
            node = Node(value=values[index])
            if not self.root:
                self.root = node
            node.left = self.insert(values, index=index*2+1)
            node.right = self.insert(values, index=index*2+2)

        return node

class BinaryTree(BaseBinaryTree):
    def is_parent(self, node):
        return bool(node.left or node.right)

    def is_interior(self, node):
        return (not node == self.root) and self.is_parent(node)

    def is_leaf(self, node):
        return (not node == self.root) and (not self.is_interior(node))

level_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tree = BinaryTree(level_order)

print(tree.is_parent(tree.root))
print(tree.is_interior(tree.root.left))
print(tree.is_leaf(tree.root.left.left.left))

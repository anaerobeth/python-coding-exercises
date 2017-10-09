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
    def traverse(self, node):
        if not node:
            return None
        print(node.value)
        self.traverse(node.left)
        self.traverse(node.right)

level_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tree = BinaryTree(level_order)
tree.traverse(tree.root) # 1 2 4 8 9 5 10 3 6 7


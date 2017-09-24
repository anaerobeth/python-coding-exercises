class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
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

level_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tree = BinaryTree(level_order)
root = tree.root.value
left = tree.root.left.value
right = tree.root.right.value

print(root, left, right) # 1 2 3

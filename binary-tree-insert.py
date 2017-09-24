class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        if not self.root:
            self.root = Node(value=value)
        elif not self.root.left:
            self.root.left = Node(value=value)
        elif not self.root.right:
            self.root.right = Node(value=value)

tree = BinaryTree(Node(value=1))
tree.insert(2)
tree.insert(3)
tree.insert(4)

root = tree.root.value
left = tree.root.left.value
right = tree.root.right.value

print(root, left, right) # 1 2 3

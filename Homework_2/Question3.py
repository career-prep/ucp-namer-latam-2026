# Implement a Binary Search Tree with the following methods:
# min, max, contains, insert, delete.
# Use a Node struct with data, left, and right fields.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def min(self):
        current = self.root
        while current.left:
            current = current.left
        return current.data

    def max(self):
        current = self.root
        while current.right:
            current = current.right
        return current.data

    def contains(self, val):
        current = self.root
        while current:
            if val == current.data:
                return True
            elif val < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return
        current = self.root
        while True:
            if val == current.data:
                return
            elif val < current.data:
                if current.left is None:
                    current.left = Node(val)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(val)
                    return
                current = current.right

    def delete(self, val):
        self.root = self._delete_helper(self.root, val)

    def _delete_helper(self, node, val):
        if node is None:
            return None
        if val < node.data:
            node.left = self._delete_helper(node.left, val)
        elif val > node.data:
            node.right = self._delete_helper(node.right, val)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor = node.right
            while successor.left:
                successor = successor.left
            node.data = successor.data
            node.right = self._delete_helper(node.right, successor.data)
        return node


def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.data] + inorder(node.right)


bst = BinarySearchTree()
for val in [10, 5, 15, 3, 7, 12, 18]:
    bst.insert(val)
print(inorder(bst.root))
print(bst.min())
print(bst.max())
print(bst.contains(7))
print(bst.contains(9))

bst.insert(7)
print(inorder(bst.root))

bst.delete(3)
print(inorder(bst.root))

bst.delete(15)
print(inorder(bst.root))

bst.delete(10)
print(inorder(bst.root))

# min: O(log n)
# max: O(log n)
# contains: O(log n)
# insert: O(log n)
# delete: O(log n)
# Spent 60 mins

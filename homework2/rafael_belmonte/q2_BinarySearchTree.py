# Data Structure Implementation: Binary Search Tree
# time complexity per method noted inline
# 35 minutes

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def min(self):  # O(log n)
        if not self.root:
            return None
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.data

    def max(self):  # O(log n)
        if not self.root:
            return None
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.data

    def contains(self, val):  # O(log n)
        curr = self.root
        while curr:
            if val == curr.data:
                return True
            elif val < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def insert(self, val):  # O(log n)
        if not self.root:
            self.root = Node(val)
            return
        curr = self.root
        while True:
            if val == curr.data:
                return  # no duplicates
            elif val < curr.data:
                if not curr.left:
                    curr.left = Node(val)
                    return
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = Node(val)
                    return
                curr = curr.right

    def delete(self, val):  # O(log n)
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if not node:
            return None
        if val < node.data:
            node.left = self._delete(node.left, val)
        elif val > node.data:
            node.right = self._delete(node.right, val)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # replace with in-order successor (min of right subtree)
            successor = node.right
            while successor.left:
                successor = successor.left
            node.data = successor.data
            node.right = self._delete(node.right, successor.data)
        return node

# test cases
bst = BinarySearchTree()
for val in [10, 8, 16, 9, 13, 17, 20]:
    bst.insert(val)

assert bst.min() == 8
assert bst.max() == 20
assert bst.contains(13) == True
assert bst.contains(15) == False

bst.delete(13)
assert bst.contains(13) == False
assert bst.contains(10) == True

bst.insert(10)  # duplicate, should be no-op
assert bst.min() == 8

bst.delete(10)  # delete root
assert bst.contains(10) == False
assert bst.min() == 8
assert bst.max() == 20

print("yay!!")

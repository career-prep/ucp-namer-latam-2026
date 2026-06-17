"""40 minutes
Oluwatomi
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self,val):
        self.root = self.insertHelper(self.root, val)

    def insertHelper(self, node, val):
        if not node:
            return Node(val)

        if val < node.data:
            node.left = self.insertHelper(node.left, val)
        else:
            node.right = self.insertHelper(node.right, val)

        return node

    def minimum(self):
        return self.minimumHelper(self.root)

    def minimumHelper(self,node):
        if node is None:
            return None
        if node.left is None:
            return node.data
        return self.minimumHelper(node.left)

    def maximum(self):
        return self.maximumHelper()
    def maximumHelper(self):
        if self.root is None:
            return -1
        cur = self.root
        while cur.right:
            cur = cur.right

        return cur.data

    def contains(self, val):
        return self.containsHelper(self.root, val)

    def containsHelper(self, node, val):
        if node is None:
            return False

        if node.data == val:
            return True
        if node.data < val:
            return self.containsHelper(node.right, val)
        else:
            return self.containsHelper(node.left, val)

    """
    Problems with deletion
    """

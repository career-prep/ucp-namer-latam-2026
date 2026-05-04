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
        return self.maximumHelper(self.root)
    def maximumHelper(self, node):
        if node is None:
            return None
        cur = node
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
    def delete(self, val):
        self.root = self.deleteHelper(self.root, val)
    def deleteHelper(self, node, val):
        if node is None: #empty case
            return None
        if val < node.data:
            node.left =  self.deleteHelper(node.left, val)
        elif val > node.data:
            node.right =  self.deleteHelper(node.right, val)
        else:
            if node.left is None and node.right is None: #has no child
                return None

            """ has one child """
            if node.left and node.right is None:
                return node.left
            if node.right and node.left is None:
                return node.right 

            """ has multiple children"""
            next_node = node.right
            while next_node.left:
                next_node = next_node.left

            node.data = next_node.data
            node.right = self.deleteHelper(node.right, next_node.data)

        return node
                

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
 
    def min(self):
        # O(log n) time (O(n) worst case skewed tree)
        if self.root is None:
            return None
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.data
 
    def max(self):
        # O(log n) time
        if self.root is None:
            return None
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.data
 
    def contains(self, val):
        # O(log n) time
        curr = self.root
        while curr:
            if val == curr.data:
                return True
            elif val < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return False
 
    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return
        curr = self.root
        while True:
            if val == curr.data:
                return
            elif val < curr.data:
                if curr.left is None:
                    curr.left = new_node
                    return
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = new_node
                    return
                curr = curr.right
 
    def findMin(self, node):
        while node.left:
            node = node.left
        return node
 
    def deleteHelper(self, node, val):
        if node is None:
            return None
        if val < node.data:
            node.left = self.deleteHelper(node.left, val)
        elif val > node.data:
            node.right = self.deleteHelper(node.right, val)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            successor = self.findMin(node.right)
            node.data = successor.data
            node.right = self.deleteHelper(node.right, successor.data)
        return node
 
    def delete(self, val):
        # O(log n) time
        self.root = self.deleteHelper(self.root, val)
 
    def inorder(self):
        result = []
        def helper(node):
            if node:
                helper(node.left)
                result.append(node.data)
                helper(node.right)
        helper(self.root)
        return result
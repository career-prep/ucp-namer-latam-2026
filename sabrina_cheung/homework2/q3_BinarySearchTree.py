'''
Time: 30 mins
'''

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, data):
        self.root = Node(data)

    def min(self):
        cur = self.root
        while cur.left:
            cur = cur.left
        return cur

    def max(self):
        cur = self.root
        while cur.right:
            cur = cur.right
        return cur
    
    def contains(self, val):
        if not self.root:
            return False
        if self.root.data == val:
            return True
        elif val < self.root.data:
            return self.contains(self.root.left, val)
        else:
            return self.contains(self.root.right, val)
    
    def insert(self, val):
        if not self.root:
            return Node(val)

        if val < self.root.data:
            self.root.left = self.insert(self.root.left, val)
        elif val > self.root.data:
            self.root.right = self.insert(self.root.right, val)

        return self.root
    
    def delete(self, val):
        if not self.contains(val): # Value not in tree
            return self.root
        
        # Case 1: Node deleted has no children

        # Case 2: Node deleted has one children and can be replaced by it

        # Case 3: Node deleted has two children
#Binary Search Tree Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def min(self):
        if not self.root:
            return -1
        
        node = self.root
        while node.left:
            node = node.left
        return node.data
    
    def max(self):
        if not self.root:
            return -1
        
        node = self.root
        while node.right:
            node = node.right
        return node.data
    
    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return
        newNode = Node(val)
        curr = self.root
        while curr:
            if val < curr.data:
                if curr.left is None:
                    curr.left = newNode
                    return
                curr = curr.left
            elif val > curr.data:
                if curr.right is None:
                    curr.right = newNode
                    return
                curr = curr.right
            else:
                return
            
    def delete(self,val):
        if not self.root:
            return None
        
        
    def contain(self, val):
        if not self.root:
            return False
        curr = self.root
        while curr:
            if val < curr.data:
                curr = curr.left
            elif val > curr.data:
                curr = curr.right
            else:
                return True
        return False
#Binary Search Tree Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def min(self): #O(log n)
        if not self.root:
            return -1
        
        node = self.root
        while node.left:
            node = node.left
        return node.data
    
    def max(self): #O(log n)
        if not self.root:
            return -1
        
        node = self.root
        while node.right:
            node = node.right
        return node.data
    
    def insert(self, val): #O(log n)
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
            
    def delete(self, val): #O(log n)
        if not self.root:
            return

        parent, node = None, self.root
        while node and node.val != val:
            parent = node
            if val < node.val:
                node = node.left
            else:
                node = node.right

        if not node:
            return

        if node.left and node.right:
            successorParent = node
            successor = node.right
            while successor.left:
                successorParent = successor
                successor = successor.left
            node.val = successor.val
            parent = successorParent
            node = successor

        if node.left:
            child = node.left
        else:
            child = node.right

        if not parent:
            self.root = child
        elif parent.left == node:
            parent.left = child
        else:
            parent.right = child
        
        
    def contain(self, val): #O(log n)
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
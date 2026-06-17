# Time: 40 minutes
class Node:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def min(self):
        current = self.root

        if current is None:
            return None
        
        while current.left is not None:
            current = current.left
        
        return current.data

    ## returns the minimum value in the BST.  O(logn) time.

    def max(self):
        current = self.root

        if current is None:
            return None

        while current.right is not None:
            current = current.right
        
        return current
    
    ## returns the maximum value in the BST.  O(logn) time.

    def contains(self, val):

        current = self.root
        
        while current is not None:
            if val == current.data:
                return True
            if val < current.data:
                current = current.left
            else:
                current = current.right
        return False
        
    ## returns a boolean indicating whether val is present in the  BST.  O(logn) time.

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return 
        
        current = self.root
        while True:
            if val == current.data:
                return
            
            if val < current.data:
                if current.left is None:
                    current.left = Node(val)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(val)
                    return
                current = current.right

    ## creates a new Node with data val in the appropriate location.   
    ## For simplicity, do not allow duplicates. If val is already 
    ## present, insert is a no-op. O(logn) time.

    def delete(self, val):
        parent = None
        current = self.root

        while current is not None and current.data != val:
            parent = current
            if val < current.data:
                current = current.left
            else:
                current = current.right
        
        if current is None:
            return
        
        if parent.left is current:
            parent.left = None
        else:
            parent.right = None
    ## deletes the Node with data val, if it exists. O(logn) time.

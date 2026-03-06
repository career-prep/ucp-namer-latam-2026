class Node:
    def __init__ (self, data):
        self.val = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__ (self, data):
        self.root = Node(data)


    #returns the minimum value in the BST.  O(logn) time.
    def min:
        current = self.root
        while current.left != None:
            current = current.left
        return current

    #returns the maximum value in the BST.  O(logn) time.
    def max:
        current = self.root
        while current.rigth != None:
            current = current.right
        return current

    #returns a boolean indicating whether val is present in the BST.  O(logn) time.
    def contains(val):

        current = self.root
        while current:
            if current.val == val:
                return True
            if val < current.val:
                current = current.left
            else:
                current = current.right

        return -1

    #creates a new Node with data val in the appropriate location.  
    #For simplicity, do not allow duplicates. 
    #If val is already present, insert is a no-op. O(logn) time.
    def insert(val):
        if self.contains(val):
            return
        
        current = self.root
        while current != None:
            if current.val < val:
                current = current.right
            else:
                current = current.left


    #deletes the Node with data val, if it exists. O(logn) time.
    def delete(val):
        if not self.contains(val):
            return
        current = self.root
    
        while current.val != val:
            if current.val < val:
                current = current.right
            else:
                current = current.left


            
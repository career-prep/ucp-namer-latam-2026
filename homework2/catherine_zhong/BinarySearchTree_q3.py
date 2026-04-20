
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
        if not self.root:
            return None

        current = self.root
        while current.left != None:
            current = current.left
        return current

    #returns the maximum value in the BST.  O(logn) time.
    def max:
        if not self.root:
            return None 

        current = self.root
        while current.right != None:
            current = current.right
        return current

    #returns a boolean indicating whether val is present in the BST.  O(logn) time.
    def contains(self, val):

        current = self.root
        while current:
            if current.val == val:
                return True
            if val < current.val:
                current = current.left
            else:
                current = current.right

        return False

    #creates a new Node with data val in the appropriate location.  
    #For simplicity, do not allow duplicates. 
    #If val is already present, insert is a no-op. O(logn) time.
    def insert(self, val):
        if self.contains(val):
            return
        
        current = self.root
        while current != None:
            if current.val < val:
                if not current.right:
                    current.right = Node(val)
                    return 
                else:
                    current = current.right
            else:
                if not current.left:
                    current.left = Node(val)
                    return 
                else: 
                    current = current.left


    #deletes the Node with data val, if it exists. O(logn) time.
    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _min(self, node):
        while node.left:
            node = node.left
        return node

    def _delete(self, node, val):
        if not self.contains(val):
            return

        current = self.root

        if val < node.val:
            node.left = self.delete(node.left, val)
        elif val > node.val: 
            node.right = self.delete(node.right, val)

        else:
            if not node.left and not node.right:
                return None

            if not node.left:
                return node.right
            if not node.right:
                return node.left
            
            successor = self._min(node.right)
            node.val = successor.val
            node.right = self._delete(node.right, successor.val)

        return node


#time spent: 30 min   
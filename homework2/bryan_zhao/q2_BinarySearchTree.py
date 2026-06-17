# Time Spent: 40 minutes

from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    # Returns the minimum value in the BST. O(log n) time.

    def min(self, start) -> Optional[int]:
        if start:
            curr = start
        else:
            curr = self.root
        
        if not curr:
            return None
        
        while curr.left:
            curr = curr.left
        
        return curr.data
    
    # Returns the maximum value in the BST. O(log n) time.

    def max(self) -> Optional[int]:
        if not self.root:
            return None
        
        curr = self.root
        while curr.right:
            curr = curr.right

        return curr.data
    
    # Returns a boolean indicating whether val is present in the BST. O(log n) time.

    def contains(self, val: int) -> bool:
        if not self.root:
            return False
        
        curr = self.root

        while curr:
            if val == curr.data:
                return True
            elif val < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        
        return False
    
    # Creates a new Node with data val in the appropriate location. For simplicity,
    # do not allow duplicates. If val is already present, insert is a no-op. O(log n) time.

    def insert(self, val: int) -> None:
        if not self.root:
            self.root = Node(val)
            return
        
        curr = self.root
        
        while curr:
            if val < curr.data:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(val)
                    return
            elif val > curr.data:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(val)
                    return
            else:
                return

    # Deletes the node with data val, if it exists. O(log n) time.

    def delete(self, val: int) -> None:
        self.root = self.deleteHelper(self.root, val)

    def deleteHelper(self, curr: Optional[Node], val: int) -> Optional[Node]:
        if not curr:
            return None
        
        if val < curr.data:
            curr.left = self.deleteHelper(curr.left, val)
        elif val > curr.data:
            curr.right = self.deleteHelper(curr.right, val)
        else:
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left
            
            # Needed to alter the min() function to take a parameter so that
            # I could reuse function instead of making new function for minimum.
            successor_val = self.min(curr.right)

            if successor_val:
                curr.data = successor_val
                curr.right = self.deleteHelper(curr.right, successor_val)
        
        return curr

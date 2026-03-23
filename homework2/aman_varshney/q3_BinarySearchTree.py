# spent 40 minutes

class Node:
    """Node struct in python"""
    def __init__(self, data: int, left: Node = None, right: Node = None) -> None:
        self.data = data
        self.left = left 
        self.right = right
        
        
class BinarySearchTree:
    def __init__(self, root) -> None:
        self.root = root
        
        
    def min(self):
        """Returns the min value in tree. O(logn)"""
        if not self.root: # empty case
            return None
        
        curr = self.root
        while curr.left:
            curr = curr.left       
        return curr.data
    
    
    def max(self):
        """Returns the max value in tree. O(logn)"""
        if not self.root: # empty case
            return None
        
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.data
    
    
    def contains(self, val):
        """Searches for a node with data `val` and returns true if found. O(logn)"""
        if not self.root: # empty case
            return False
        
        curr = self.root
        
        # helper
        def finder(node, val):
            if not node: # empty case
                return False
            if node.data > val: 
                return finder(node.left, val)
            elif node.data < val:
                return finder(node.right, val) 
            else:
                return True
            
        return finder(curr, val)
    
    
    def insert(self, val):
        """Creates a new node with data `val` and inserts it into the tree. If a node with `val`
        is already in the tree, no-op. O(logn)"""
        if not self.root:
            self.root = Node(val, None, None)
            return
            
        curr = self.root
            
        # helper
        def helper(node, val):
            if node.data > val:
                if not node.left: # min value
                    node.left = Node(val, None, None)
                else:
                    helper(node.left, val)
            elif node.data < val:
                if not node.right: # max value
                    node.right = Node(val, None, None)
                else:
                    helper(node.right, val)
            else: # no op
                return
            
        helper(curr, val)
        
        
    def delete(self, val):
        """Deletes the node with data `val` if it exists. O(logn)"""
        curr = self.root
        
        # helper
        def helper(node, val):
            if not node: # empty case
                return None
            
            if node.data > val:
                node.left = helper(node.left, val) 
            elif node.data < val:
                node.right = helper(node.right, val)
            else: # node found
                # no children case
                if not node.left and not node.right:
                    return None
                
                # one child
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                
                # two children
                # find min in right subtree
                min_in_right = node.right
                while min_in_right.left:
                    min_in_right = min_in_right.left
                # 
                node.data = min_in_right.data
                node.right = helper(node.right, min_in_right.data)
            
            return node
        
        self.root = helper(curr, val)
                
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def min(self): # Time, Space Complexities: O(log n), O(1)
        if self.root is None:
            return None
        #1. Traverse to the leftmost node

        curr = self.root
        while curr.left is not None:
            curr = curr.left
        return curr.data

    def max(self): # Time, Space Complexities: O(log n), O(1)
        if self.root is None:
            return None
        
        #1. Traverse to the rightmost node
        curr = self.root
        while curr.right is not None:
            curr = curr.right
        return curr.data

    def contains(self, val): # Time, Space Complexities: O(log n), O(1)
        curr = self.root

        #1. Search by comparing val with current node data
        while curr is not None:
            if val == curr.data:
                return True
            elif val < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def insert(self, val): # Time, Space Complexities: O(log n), O(1)
        if self.root is None:
            self.root = Node(val)
            return
        
        curr = self.root
        while True:

            #1. Do nothing if value is a duplicate
            if val == curr.data:
                return
            
            #2. Traverse left if value is smaller
            elif val < curr.data:
                if curr.left is None:
                    curr.left = Node(val)
                    return
                curr = curr.left

            #3. Traverse right if value is larger
            else:
                if curr.right is None:
                    curr.right = Node(val)
                    return
                curr = curr.right

    def delete(self, val): # Time, Space Complexities: O(log n), O(log n)
        
        #1. Recursive helper to handle the three deletion cases
        def _delete(node, val):
            if node is None:
                return None
            
            if val < node.data:
                node.left = _delete(node.left, val)
            elif val > node.data:
                node.right = _delete(node.right, val)
            else:

                #2.Node has zero or one child
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                
                #3.Node has two children (find successor)
                successor = node.right
                while successor.left is not None:
                    successor = successor.left
                
                node.data = successor.data
                node.right = _delete(node.right, successor.data)
                
            return node

        self.root = _delete(self.root, val)
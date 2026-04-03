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
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.data

    def max(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.data

    def contains(self, val):
        current = self.root
        while current:
            if val == current.data:
                return True
            elif val < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return

        current = self.root
        while True:
            if val == current.data:
                return  # No-op for duplicates
            elif val < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(val)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(val)
                    break

    def delete(self, val):

        def helper(node, val):
            if not node:
                return None
            
            # go left
            if val < node.val:
                node.left = helper(node.left, val)
            
            # go right
            elif val > node.val:
                node.right = helper(node.right, val)
            
            # node found
            else:
                # case 1: no child
                if not node.left and not node.right:
                    return None
                
                # case 2: one child
                if not node.left:
                    return node.right
                
                if not node.right:
                    return node.left
                
                # case 3: two children
                # find inorder successor (smallest in right subtree)
                successor = node.right
                while successor.left:
                    successor = successor.left
                
                node.val = successor.val
                node.right = helper(node.right, successor.val)
            
            return node
        
        self.root = helper(self.root, val)
    
        
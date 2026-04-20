class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def min(self):
        """Return the minimum value in the BST. O(log n)."""
        if not self.root:
            return -1 
        
        node = self.root
        while node.left:
            node = node.left
        
        return node.data
    
    def getMinNode(self, node):
        cur = node
        while cur.left:
            cur = cur.left

        return cur 

    def max(self):
        """Return the maximum value in the BST. O(log n)."""
        if not self.root:
            return -1 

        node = self.root
        while node.right:
            node = node.right
        
        return node.data

    def contains(self, val):
        """Return whether val is present in the BST. O(log n)."""
        node = self.root
        while node:
            if node.data > val:
                node = node.left
            elif node.data < val:
                node = node.right
            else:
                return True
        
        return False

    def insert(self, val):
        """
        Create a new Node with data val in the appropriate location.
        Do not allow duplicates; if val already exists, do nothing. O(log n).
        """
        if not self.root:
            self.root = Node(val)
            return 
        
        cur = self.root
        while True:
            if val < cur.data:
                if not cur.left:
                    cur.left = Node(val)
                    return
                cur = cur.left
            elif val > cur.data:
                if not cur.right:
                    cur.right = Node(val)
                    return
                cur = cur.right
            else:
                return

    def delete(self, val):
        """Delete the Node with data val, if it exists. O(log n)."""

        def deleteNode(node, val):
            if not node:
                return None

            if val < node.data:
                node.left = deleteNode(node.left, val)
            elif val > node.data:
                node.right = deleteNode(node.right, val)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left

                succ = self.getMinNode(node.right)
                node.data = succ.data
                node.right = deleteNode(node.right, succ.data)
            
            return node
        
        self.root = deleteNode(self.root, val)


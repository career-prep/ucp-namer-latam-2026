class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # O(log n)
    def min(self):
        if not self.root:
            return None
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.data

    # O(log n)
    def max(self):
        if not self.root:
            return None
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.data

    # O(log n)
    def contains(self, val):
        curr = self.root
        while curr:
            if val == curr.data:
                return True
            elif val < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return False

    # O(log n)
    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return
        curr = self.root
        while True:
            if val == curr.data:
                return  # no duplicates
            elif val < curr.data:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(val)
                    return
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(val)
                    return

    # O(log n)
    def delete(self, val):
        def delete_node(node, val):
            if not node:
                return None
            if val < node.data:
                node.left = delete_node(node.left, val)
            elif val > node.data:
                node.right = delete_node(node.right, val)
            
            else:
                # Case 1: No children
                if not node.left and not node.right:
                    return None
                
                # Case 2: If there is one child
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                
                # Case 3: If there are two children
                # Find inorder successor (smallest in right subtree)
                successor = node.right
                while successor.left:
                    successor = successor.left
                
                node.data = successor.data
                node.right = delete_node(node.right, successor.data)
            
            return node
        
        self.root = delete_node(self.root, val)
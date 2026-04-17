class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
 
class BinarySearchTree:
    def __init__(self):
        self.root = None
 
    # go left as far as possible since smallest is always leftmost
    # Time: O(log n) for balanced, O(n) worst case
    def min(self):
        if self.root is None:
            return None
        curr = self.root
        while curr.left is not None:
            curr = curr.left
        return curr.data
 
    # same but go right for the max
    # Time: O(log n)
    def max(self):
        if self.root is None:
            return None
        curr = self.root
        while curr.right is not None:
            curr = curr.right
        return curr.data
 
    # standard BST search - go left if smaller, right if bigger
    # Time: O(log n)
    def contains(self, val):
        curr = self.root
        while curr is not None:
            if val == curr.data:
                return True
            elif val < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return False
 
    # Time: O(log n)
    def insert(self, val):
        if self.root is None:
            self.root = BSTNode(val)
            return
        curr = self.root
        while True:
            if val == curr.data:
                return  # no duplicates allowed, just bail
            elif val < curr.data:
                if curr.left is None:
                    curr.left = BSTNode(val)
                    return
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = BSTNode(val)
                    return
                curr = curr.right
 
    # delete 3 cases:
    # 1. node has no children - just remove it
    # 2. node has one child - replace node with that child
    # 3. node has two children - replace with inorder successor (smallest in right subtree)
    # Time: O(log n)
    def delete(self, val):
        self.root = self._delete_helper(self.root, val)
 
    def _delete_helper(self, node, val):
        if node is None:
            return None  # value not found, nothing to do
        if val < node.data:
            node.left = self._delete_helper(node.left, val)
        elif val > node.data:
            node.right = self._delete_helper(node.right, val)
        else:
            # found the node to delete
            if node.left is None:
                return node.right  # case 1 or 2 (no left child)
            elif node.right is None:
                return node.left   # case 2 (no right child)
            else:
                # case 3: two children
                # find the inorder successor (smallest in right subtree)
                successor = node.right
                while successor.left is not None:
                    successor = successor.left
                node.data = successor.data  # copy successor's value up
                node.right = self._delete_helper(node.right, successor.data)  # delete the successor
        return node
 

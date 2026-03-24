class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def min(self):
        if not self.root:
            return None
        curr = self.root
        while curr.left != None:
            curr = curr.left
        return curr.val
    # time: O(logn)

    def max(self):
        if not self.root:
            return None
        curr = self.root
        while curr.right != None:
            curr = curr.right
        return curr.val
    # time: O(logn)

    def contains(self, val):
        curr = self.root
        while curr != None:
            if val == curr.val:
                return True
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return False
    # time: O(logn)

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return
        curr = self.root
        while True:
            if val < curr.val:
                if curr.left == None:
                    curr.left = Node(val)
                    return
                curr = curr.left
            elif val > curr.val:
                if curr.right == None:
                    curr.right = Node(val)
                    return
                curr = curr.right
            else:
                return
    # time: O(logn)

    def delete(self, val):
        def _delete(root, val):
            if not root:
                return None
            if val < root.val:
                root.left = _delete(root.left, val)
            elif val > root.val:
                root.right = _delete(root.right, val)
            else:
                if root.left == None:
                    return root.right
                if root.right == None:
                    return root.left
                nxt = root.right
                while nxt.left != None:
                    nxt = nxt.left
                root.val = nxt.val
                root.right = _delete(root.right, nxt.val)
            return root

        self.root = _delete(self.root, val)
    # time: O(logn)
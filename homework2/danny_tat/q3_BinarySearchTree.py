# Question 3:

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def min(self):
        # Time: O(log n) avg, O(n) worst and Space: O(1)
        cur = self.root
        while cur.left:
            cur = cur.left
        return cur.data

    def max(self):
        # Time: O(log n) avg, O(n) worst and Space: O(1)
        cur = self.root
        while cur.right:
            cur = cur.right
        return cur.data

    def contains(self, val):
        # Time: O(log n) avg, O(n) worst and Space: O(1)
        cur = self.root
        while cur:
            if val == cur.data:
                return True
            elif val < cur.data:
                cur = cur.left
            else:
                cur = cur.right
        return False

    def insert(self, val):
        # Time: O(log n) avg, O(n) worst and Space: O(1)
        if not self.root:
            self.root = Node(val)
            return
        cur = self.root
        while True:
            if val == cur.data:
                return
            elif val < cur.data:
                if not cur.left:
                    cur.left = Node(val)
                    return
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = Node(val)
                    return
                cur = cur.right

    def delete(self, val):
        # Time: O(log n) avg, O(n) worst and Space: O(log n) — recursion stack
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if not node:
            return None
        if val < node.data:
            node.left = self._delete(node.left, val)
        elif val > node.data:
            node.right = self._delete(node.right, val)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            successor = node.right
            while successor.left:
                successor = successor.left
            node.data = successor.data
            node.right = self._delete(node.right, successor.data)
        return node

# time: 40 min

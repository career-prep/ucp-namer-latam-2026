class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self, root):
        self.root = root

    # Time Complexity: O(log n)
    def min(self):
        if self.root is None:
            return None
        curr = self.root
        min_val = curr.data

        while curr.left is not None:
            curr = curr.left
            min_val = min(min_val, curr.data)
        return min_val

    # Time Complexity: O(log n)
    def max(self):
        if self.root is None:
            return None
        curr = self.root
        max_val = curr.data

        while curr.right is not None:
            curr = curr.right
            max_val = max(max_val, curr.data)
        return max_val

    # Time Complexity: O(log n)
    def contains(self, val):
        curr = self.root

        while curr is not None:
            if val > curr.data:
                curr = curr.right
            elif val < curr.data:
                curr = curr.left
            else:
                return True
        return False

    # Time Complexity: O(log n)
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return
        if self.contains(val):
            return
        curr = self.root
        while True:
            if val < curr.data:
                if curr.left is None:
                    curr.left = Node(val)
                    return
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = Node(val)
                    return
                curr = curr.right

    # Time Complexity: O(log n)
    def delete(self, val):
        if not self.contains(val):
            return
        parent = None
        curr = self.root

        while curr.data != val:
            parent = curr
            if val > curr.data:
                curr = curr.right
            elif val < curr.data:
                curr = curr.left

        if curr.left is None and curr.right is None:
            if curr is self.root:
                self.root = None
            else:
                if parent.left is curr:
                    parent.left = None
                else:
                    parent.right = None
        elif curr.left is None or curr.right is None:
            if curr.left is not None:
                child = curr.left
                if curr is self.root:
                    self.root = child
                else:
                    if parent.left == curr:
                        parent.left = child
                    else:
                        parent.right = child
            else:
                child = curr.right
                if curr is self.root:
                    self.root = child
                else:
                    if parent.left == curr:
                        parent.left = child
                    else:
                        parent.right = child
        else:
            successor_parent = None
            right_child = curr.right
            while right_child.left is not None:
                successor_parent = right_child
                right_child = right_child.left

            curr.data = right_child.data

            if successor_parent is None:
                curr.right = right_child.right
            else:
                successor_parent.left = right_child.right
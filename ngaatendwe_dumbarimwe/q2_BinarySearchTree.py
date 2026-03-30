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
        pass
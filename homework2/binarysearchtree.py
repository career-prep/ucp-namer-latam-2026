class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # min
    def min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data

    # max
    def max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data

    #  contains or not
    def contains(self, val):
        current = self.root
        while current is not None:
            if val == current.data:
                return True
            elif val < current.data:
                current = current.left
            else:
                current = current.right
        return False

    # insert
    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if val == current.data:       
                return
            elif val < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def min(self):  # O(log n)
        if not self.root:
            return None
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.data

    def max(self):  # O(log n)
        if not self.root:
            return None
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.data

    def contains(self, val):  # O(log n)
        curr = self.root
        while curr:
            if curr.data == val:
                return True
            elif val < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def insert(self, val):  # O(log n)
        if not self.root:
            self.root = Node(val)
            return
        curr = self.root
        while True:
            if val == curr.data:
                return
            elif val < curr.data:
                if not curr.left:
                    curr.left = Node(val)
                    return
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = Node(val)
                    return
                curr = curr.right

    def delete(self, val):  # O(log n)
        self.root = self._deleteHelper(self.root, val)

    def _deleteHelper(self, node, val):
        if not node:
            return None
        if val < node.data:
            node.left = self._deleteHelper(node.left, val)
        elif val > node.data:
            node.right = self._deleteHelper(node.right, val)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                successor = node.right
                while successor.left:
                    successor = successor.left
                node.data = successor.data
                node.right = self._deleteHelper(node.right, successor.data)
        return node

    def inorder(self):
        result = []
        def helper(node):
            if not node:
                return
            helper(node.left)
            result.append(node.data)
            helper(node.right)
        helper(self.root)
        return result


print("BinarySearchTree Results:")

bst = BinarySearchTree()
for v in [10, 8, 16, 9, 13, 17, 20]:
    bst.insert(v)

print(bst.inorder())
print(bst.min())
print(bst.max())
print(bst.contains(13))
print(bst.contains(15))

bst.insert(10)
print(bst.inorder())

bst.delete(20)
print(bst.inorder())

bst.delete(17)
print(bst.inorder())

bst.delete(10)
print(bst.inorder())

bst.delete(99)
print(bst.inorder())

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def min(self):
        if self.root is None:
            return None
        curr = self.root
        while curr.left is not None:
            curr = curr.left
        return curr.data

    def max(self):
        if self.root is None:
            return None
        curr = self.root
        while curr.right is not None:
            curr = curr.right
        return curr.data
        
    def _containsHelper(self, curr, val):
        if curr is None:
            return False
        
        if val == curr.data:
            return True
        
        if val < curr.data:
            return self._containsHelper(curr.left, val)
        else:
            return self._containsHelper(curr.right, val)

    def contains(self, val):
        return self._containsHelper(self.root, val)
    
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            curr = self.root
            while True:
                if val < curr.data:
                    if curr.left is None:
                        curr.left = Node(val)
                        break
                    else:
                        curr = curr.left
                elif val > curr.data:
                    if curr.right is None:
                        curr.right = Node(val)
                        break
                    else:
                        curr = curr.right
                else:
                    break  # value already exists

    def _deleteHelper(self, curr, val):
        if curr is None:
            return None

        if val < curr.data:
            curr.left = self._deleteHelper(curr.left, val)
        elif val > curr.data:
            curr.right = self._deleteHelper(curr.right, val)
        else:
            if curr.left is None and curr.right is None:
                return None
            elif curr.left is None:
                return curr.right
            elif curr.right is None:
                return curr.left
            else:
                successor = curr.right
                while successor.left is not None:
                    successor = successor.left
                curr.data = successor.data
                curr.right = self._deleteHelper(curr.right, successor.data)
        return curr
            
    def delete(self, val):
        self.root = self._deleteHelper(self.root, val)

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.data)
            self._inorder(node.right, result)

    def printInOrder(self):
        result = []
        self._inorder(self.root, result)
        print(result)


if __name__ == "__main__":
    bst = BinarySearchTree()

    for val in [10, 5, 15, 3, 7, 13, 20]:
        bst.insert(val)
    bst.printInOrder()

    print(bst.contains(7))
    print(bst.contains(99))

    print(bst.min())
    print(bst.max())

    bst.insert(10)
    bst.printInOrder()

    bst.delete(5)
    bst.printInOrder()
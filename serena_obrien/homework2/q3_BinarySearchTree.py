class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Time complexity: O(h), where h is the height of the BST
    def min(self):
        if not self.root:
            return None
        
        curr = self.root
        while curr.left:
            curr = curr.left

        return curr.data
    
    # Time complexity: O(h), where h is the height of the BST
    def max(self):
        if not self.root:
            return None
        
        curr = self.root
        while curr.right:
            curr = curr.right

        return curr.data

    # Time complexity: O(log n)
    def contains(self, val):
        def _contains(node, val):
            if not node:
                return False
            if node.data == val:
                return True
            elif val < node.data:
                return _contains(node.left, val)
            else:
                return _contains(node.right, val)

        return _contains(self.root, val)

    # Time complexity: O(log n)
    def insert(self, val):
        def _insert(node, val):
            if not node:
                return Node(val)
            if val < node.data:
                node.left = _insert(node.left, val)
            elif val > node.data:
                node.right = _insert(node.right, val)
            return node
    
        self.root = _insert(self.root, val)

    # Time complexity: O(log n)
    def delete(self, val):
        def _delete(node, val):
            if not node:
                return None
            
            if val < node.data:
                node.left = _delete(node.left, val)
            elif val > node.data:
                node.right = _delete(node.right, val)
            else: # this is the node to delete
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                successor = node.right
                while successor.left:
                    successor = successor.left
                node.data = successor.data
                node.right = _delete(node.right, successor.data)
            return node
        
        self.root = _delete(self.root, val)

if __name__ == '__main__':
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(7)

    print(bst.contains(7))   # should be true
    print(bst.contains(8))   # should be false

    bst.delete(5)
    print(bst.contains(5))   # should be false

    print(bst.min()) # should be 7
    print(bst.max()) # should be 15
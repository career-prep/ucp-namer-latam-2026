# Time complexity: O(n)
# Space complexity: O(n)

# Technique: I don't know if I was supposed to use on of the traversal algorithms, but this is a form of linked list recursion I guess

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self, root = None):
        self.root = root

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

    def inorder(self):
        result = []

        def _inorder(node):
            if not node:
                return
            _inorder(node.left)
            result.append(node.data)
            _inorder(node.right)

        _inorder(self.root)
        return result

def IsBST(root, low=float('-inf'), high = float('inf')):
    if not root:
        return True
    
    if not (low < root.data < high):
        return False
    
    return (IsBST(root.left, low, root.data) and IsBST(root.right, root.data, high))
        
if __name__ == '__main__':
    bst = BST()
    for val in [10, 5, 15, 3, 7, 12, 18]:
        bst.insert(val)
    
    print(f"Original BST inorder: {bst.inorder()}")
    print(f"Is this a valid BST? {IsBST(bst.root)}")

    print("Manually messing it up")
    bst.root.left.right.data = 86

    print(f"Is this a valid BST? {IsBST(bst.root)}")

# ~ time spent: 20 minutes
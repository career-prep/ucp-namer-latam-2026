# Time complexity: O(n)
# Space complexity: O(n)

# Technique: Depth-first traversal - pre-order

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

def CopyTree(root):
    if not root:
        return None
    
    copyRoot = Node(root.data)
    copyRoot.left = CopyTree(root.left)
    copyRoot.right = CopyTree(root.right)
    return copyRoot
        
if __name__ == '__main__':
    bst = BST()
    for val in [2,6,7,12,3,7,8]:
        bst.insert(val)
    
    print(f"BST inorder: {bst.inorder()}")

    copyTree = BST(CopyTree(bst.root))
    print(f"Copied BST inorder: {copyTree.inorder()}")

    # make sure it is a deep copy
    copyTree.insert(100)
    print("After adding 100")
    print(f"BST inorder: {bst.inorder()}")  
    print(f"Copied BST inorder: {copyTree.inorder()}")

# ~ time spent: 25 minutes
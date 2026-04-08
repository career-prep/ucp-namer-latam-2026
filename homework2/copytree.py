# Technique: Depth-first traversal (Pre-order)
# Time Complexity: O(n)
# Space Complexity: O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

def copyTree(root):
    if root is None:
        return None

    new_node       = TreeNode(root.val)
    new_node.left  = copyTree(root.left)
    new_node.right = copyTree(root.right)

    return new_node

# Test cases
# Build a simple tree:   1
#                       / \
#                      2   3
root = TreeNode(1)
root.left  = TreeNode(2)
root.right = TreeNode(3)

copy = copyTree(root)

# Test 1: same values
print(copy.val, copy.left.val, copy.right.val)  # 1 2 3

# Test 2: 
print(copy is not root)        # True

# Test 3: empty tree
print(copyTree(None))          # None

# Time spent: ~40 minutes

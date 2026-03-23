# Technique: Search binary search tree (BST)
# Time Complexity: O(n)
# Space Complexity: O(h) — h is the height of the tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

def isBST(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True

    if not (min_val < root.val < max_val):
        return False

    return (isBST(root.left,  min_val, root.val) and
            isBST(root.right, root.val, max_val))

# Test cases
# Test 1: valid BST → True
#        10
#       /  \
#      8   16
#       \  / \
#       9 13  17
#               \
#               20
root1 = TreeNode(10)
root1.left        = TreeNode(8)
root1.left.right  = TreeNode(9)
root1.right       = TreeNode(16)
root1.right.left  = TreeNode(13)
root1.right.right = TreeNode(17)
root1.right.right.right = TreeNode(20)

print(isBST(root1))   # True

# Time spent: ~35 minutes
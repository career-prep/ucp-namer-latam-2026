# Technique: Search binary search tree (BST)
# Time Complexity: O(h) — h is the height of the tree
# Space Complexity: O(1)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

def floorInBST(root, target):
    floor = None
    curr  = root

    while curr:
        if curr.val == target:
            return curr.val          
        elif curr.val < target:
            floor = curr.val          
            curr  = curr.right        
        else:
            curr  = curr.left         

    return floor

root = TreeNode(10)
root.left             = TreeNode(8)
root.left.right       = TreeNode(9)
root.right            = TreeNode(16)
root.right.left       = TreeNode(13)
root.right.right      = TreeNode(17)
root.right.right.right = TreeNode(20)

# Test 1: target=13, exact match → 13
print(floorInBST(root, 13))   # 13

# Test 2: target=15, no exact match → 13
print(floorInBST(root, 15))   # 13

# Test 3: target=18 → 17
print(floorInBST(root, 18))   # 17

# Test 4: target=7 → None (no floor exists)
print(floorInBST(root, 7))    # None

# Time spent: ~40 minutes

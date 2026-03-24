# Technique: Search binary search tree (BST)
# Time Complexity: O(h)
# Space Complexity: O(1)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def floorInBST(root, target):
    floor = None

    while root:
        if root.val == target:
            return root.val
        
        if root.val < target:
            floor = root.val  # possible answer
            root = root.right
        else:
            root = root.left

    return floor

# root = TreeNode(10)
# root.left = TreeNode(8)
# root.right = TreeNode(16)
# root.left.right = TreeNode(9)
# root.right.left = TreeNode(13)

# # test
# print(floorInBST(root, 15))  # Output: 13

# Depth First TRaversal: Pre-Order Traversal
# O(n) Time Complexity. n number of nodes is visited exactly once
# O(h) Space Complexity, where h is the height of the tree. O(n) in skewed cases, O(log(n)) in balanced cases
# Given a binary tree, determine if it is a binary search tree

# Binary Tree Consists of these nodes
class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def isBst(root):

    # An empty tree is still a BST
    if not root:
        return True
    
    def check(root, minAllowed, maxAllowed):

        # Base Case
        if not root:
            return True
        
        # Check if current Node violates constraints. No Duplicates Allowed in the BSTs
        # minAllowed < root.data < maxAllowed
        if root.data <= minAllowed or root.data >= maxAllowed:
            return False
        
        # Check left and right children

        # Left child cannot be greater than current node's data
        resL = check(root.left, minAllowed, root.data)

        # Right child cannot be smaller than current node's data
        resR = check(root.right, root.data, maxAllowed)

        return resL and resR


    return check(root, float("-inf"), float("inf"))



# Test Cases
root1 = TreeNode(10)
root1.left = TreeNode(8)
root1.left.right = TreeNode(9)
root1.right = TreeNode(16)
root1.right.left = TreeNode(13)
root1.right.right = TreeNode(17)
root1.right.right.right = TreeNode(20)

root2 = TreeNode(10)
root2.left = TreeNode(8)
root2.left.right = TreeNode(9)
root2.right = TreeNode(16)
root2.right.left = TreeNode(13)
root2.right.right = TreeNode(17)
root2.right.right.right = TreeNode(15)


print(isBst(root1))
print(isBst(root2))

# 29 minutes
# Technique: Depth-first traversal (pre-order)
# Time Complexity: O(n)  
# Space Complexity: O(n)
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def copyTree(root):
    if root is None:
        return None
    
    new_node = TreeNode(root.val)
    new_node.left = copyTree(root.left)
    new_node.right = copyTree(root.right)

    return new_node


# build tree
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)

# copy tree
# new_root = copyTree(root)

# print copied tree (preorder)
# def printTree(node):
#     if not node:
#         return
#     print(node.val, end=" ")
#     printTree(node.left)
#     printTree(node.right)

# printTree(new_root)  # Expected: 1 2 4 3
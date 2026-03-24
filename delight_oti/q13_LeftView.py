# Technique: Depth-first traversal (pre-order)
# Time Complexity: O(n)
# Space Complexity: O(h)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def leftView(root):
    result = []

    def dfs(node, level):
        if not node:
            return
        
        
        if level == len(result):
            result.append(node.val)
        
        # go left first!
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    return result

# simple test
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)

# print(leftView(root))  # [1, 2, 4]
# Technique: Level-order (breadth-first) traversal
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

def leftView(root):
    if not root:
        return []

    result = []
    queue  = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == 0:               
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


# Test cases
# Test 1: expected [7, 8, 9, 20, 15]
root1 = TreeNode(7)
root1.left              = TreeNode(8)
root1.right             = TreeNode(3)
root1.right.left        = TreeNode(9)
root1.right.right       = TreeNode(13)
root1.right.left.left   = TreeNode(20)
root1.right.left.right  = TreeNode(14)
root1.right.left.right.right = TreeNode(15)
print(leftView(root1))  # [7, 8, 9, 20, 15]

# Test 2: expected [7, 20, 15]
root2 = TreeNode(7)
root2.left        = TreeNode(20)
root2.right       = TreeNode(4)
root2.left.left   = TreeNode(15)
root2.left.right  = TreeNode(6)
root2.right.left  = TreeNode(8)
root2.right.right = TreeNode(11)
print(leftView(root2))  # [7, 20, 15]

# Test 3: empty tree
print(leftView(None))    # []

# Time spent: ~30 minutes

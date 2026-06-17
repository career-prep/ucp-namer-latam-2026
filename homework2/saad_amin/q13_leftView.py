#Time Complexity: O(n)
#Space Complexit: O(n)
#Technique: Level Order BFS traversal

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def leftView(root):
    if not root:
        return []
    
    q = deque()
    q.append(root)
    res = []

    while q:
        levels = []

        for _ in range(len(q)):
            node = q.popleft()

            if node:
                levels.append(node.val)
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        if levels:
            res.append(levels[0])

    return res

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(9)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.right = TreeNode(10)
root.left.left.left = TreeNode(0)

print(leftView(root))

#Time taken: 20 min
from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leftView(root):
    if not root:
        return []

    out = []
    q = deque([root])
    while len(q):
        out.append(q[0].val)
        for _ in range(len(q)):
            node = q.popleft()
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)
    return out
# time: O(n)

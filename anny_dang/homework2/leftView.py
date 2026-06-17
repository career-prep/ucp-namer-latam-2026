class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

from collections import deque
def leftView(root):
    """
    Given a binary tree, return an array of the left view
    (leftmost element at each level).

    Idea: do level-order traversal (BFS). At each level,
    record the first node in the queue as the left view node.

    Time: O(n)
    Space: O(n)
    """
    if not root:
        return []

    res = []
    q = deque([root])
    while q:
        n = len(q)
        res.append(q[0].data)

        for _ in range(n):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    
    return res


# Example 1
# Expected output: [7, 8, 9, 20, 15]
root1 = Node(7)
root1.left = Node(8)
root1.right = Node(3)

root1.right.left = Node(9)
root1.right.right = Node(13)

root1.right.left.left = Node(20)
root1.right.right.left = Node(14)
root1.right.right.left.right = Node(15)


# Example 2
# Expected output: [7, 20, 15]
root2 = Node(7)
root2.left = Node(20)
root2.right = Node(4)

root2.left.left = Node(15)
root2.left.right = Node(6)
root2.right.left = Node(8)
root2.right.right = Node(11)

print(leftView(root1))
print(leftView(root2))

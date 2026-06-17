# Technique: BFS
# Time Complexity: O(N)
# Space Complexity: O(N)

# Time taken: 12 minutes

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node|None = None
        self.right: Node|None = None

def left_view(root):
    # Given a binary tree, create an array of the left view (leftmost elements in each level) of the tree.
    q = deque([root])
    res = []
    while q:
        res.append(q[0].data)
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return res

if __name__ == "__main__":
    #        10
    #       /  \
    #      5    15
    #       \     \
    #       7    20
    #            /
    #           21
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.right = Node(7)
    root.right.right = Node(20)
    root.right.right.left = Node(21)
    print(left_view(root)) # expected: [10, 5, 7, 21]
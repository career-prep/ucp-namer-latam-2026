# Question 13: LeftView

# Given a binary tree, create an array of the left view (leftmost element at each level).

# Time Complexity = O(n) — BFS visits every node once
# Space Complexity = O(w) — w = max width of tree (queue size), worst case O(n)

# Examples:

# Input:        7
#              / \
#             8   9
#            / \   \
#           10  11  12
#          /
#         20
#          \
#          15
# Output: [7, 8, 10, 20, 15]

# Input:        7
#              / \
#             20  9
#              \
#              15
# Output: [7, 20, 15]

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(vals):
    if not vals:
        return None
    root = Node(vals[0])
    queue = deque([root])
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = Node(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = Node(vals[i])
            queue.append(node.right)
        i += 1
    return root


def LeftView(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == 0:
                result.append(node.data)  # leftmost node in this level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


# --- Tests ---

# Test 1: example from problem — output [7, 8, 10, 20, 15]
#         7
#        / \
#       8   9
#      / \   \
#     10  11  12
#    /
#   20
#    \
#    15
root = Node(7)
root.left = Node(8)
root.right = Node(9)
root.left.left = Node(10)
root.left.right = Node(11)
root.right.right = Node(12)
root.left.left.left = Node(20)
root.left.left.left.right = Node(15)
print("Test 1:", LeftView(root))   # [7, 8, 10, 20, 15]

# Test 2: example from problem — output [7, 20, 15]
#         7
#        / \
#       20  9
#        \
#        15
root2 = Node(7)
root2.left = Node(20)
root2.right = Node(9)
root2.left.right = Node(15)
print("Test 2:", LeftView(root2))  # [7, 20, 15]

# Test 3: single node
root3 = build_tree([1])
print("Test 3:", LeftView(root3))  # [1]

# Test 4: empty tree
print("Test 4:", LeftView(None))   # []

# Test 5: right-skewed tree (left view is just each level's only element)
root5 = build_tree([1, None, 2, None, 3])
print("Test 5:", LeftView(root5))  # [1, 2, 3]

# Spent a total of 20 mins on this question

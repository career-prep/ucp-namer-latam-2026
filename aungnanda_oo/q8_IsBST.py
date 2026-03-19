# Question 8: IsBST

# Given a binary tree, determine if it is a binary search tree.
# BST property: for every node, all values in left subtree < node.data < all values in right subtree.

# Time Complexity = O(n) — visit every node once
# Space Complexity = O(h) — call stack where h = height of tree

# Examples:

# Input:        5
#              / \
#             3   7
#            / \ / \
#           1  4 6  9
# Output: True

# Input:        5
#              / \
#             3   7
#            / \ / \
#           1  6 6  9   (6 in left subtree of 7 is fine, but 6 in right subtree of 3 violates BST)
# Output: False


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def IsBST(root):
    def helper(node, min_val, max_val):
        if not node:
            return True
        if node.data <= min_val or node.data >= max_val:
            return False
        return (helper(node.left, min_val, node.data) and
                helper(node.right, node.data, max_val))
    return helper(root, float("-inf"), float("inf"))


# Helper to build tree from level-order list (None = missing node)
def build_tree(vals):
    if not vals:
        return None
    root = Node(vals[0])
    queue = [root]
    i = 1
    while queue and i < len(vals):
        node = queue.pop(0)
        if i < len(vals) and vals[i] is not None:
            node.left = Node(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = Node(vals[i])
            queue.append(node.right)
        i += 1
    return root


# --- Tests ---

# Test 1: valid BST
t1 = build_tree([5, 3, 7, 1, 4, 6, 9])
print("Test 1 (valid BST):", IsBST(t1))                    # True

# Test 2: invalid — right child smaller than root
t2 = build_tree([5, 3, 4])
print("Test 2 (right < root):", IsBST(t2))                 # False

# Test 3: invalid — left subtree violates ancestor constraint
# Tree:      10
#           /  \
#          5   15
#         / \
#        3   12   <- 12 > 10, violates BST
t3 = build_tree([10, 5, 15, 3, 12])
print("Test 3 (subtree violates ancestor):", IsBST(t3))    # False

# Test 4: single node
t4 = build_tree([42])
print("Test 4 (single node):", IsBST(t4))                  # True

# Test 5: None (empty tree)
print("Test 5 (empty tree):", IsBST(None))                 # True

# Test 6: left-only valid BST
t6 = build_tree([5, 3, None, 1])
print("Test 6 (left-only valid):", IsBST(t6))              # True

# Spent a total of 20 mins on this question

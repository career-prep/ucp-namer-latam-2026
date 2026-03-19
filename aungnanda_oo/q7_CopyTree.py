# Question 7: CopyTree

# Given a binary tree, create a deep copy. Return the root of the new tree.

# Time Complexity = O(n) — visit every node once
# Space Complexity = O(n) — new tree + O(h) call stack (h = height)

# Examples:

# Input:        1
#              / \
#             2   3
#            / \
#           4   5
# Output: deep copy (structurally identical, no shared nodes)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def CopyTree(root):
    if not root:
        return None
    new_node = Node(root.data)
    new_node.left = CopyTree(root.left)
    new_node.right = CopyTree(root.right)
    return new_node


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


# Helper to collect nodes inorder for comparison
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.data] + inorder(root.right)


# Helper to verify no shared nodes between two trees
def collect_ids(root, ids):
    if not root:
        return
    ids.add(id(root))
    collect_ids(root.left, ids)
    collect_ids(root.right, ids)


# --- Tests ---

# Test 1: basic tree
original = build_tree([1, 2, 3, 4, 5])
copy = CopyTree(original)
print("Test 1 - original inorder:", inorder(original))
print("Test 1 - copy inorder:    ", inorder(copy))
orig_ids, copy_ids = set(), set()
collect_ids(original, orig_ids)
collect_ids(copy, copy_ids)
print("Test 1 - no shared nodes:", orig_ids.isdisjoint(copy_ids))  # True

# Test 2: single node
original2 = build_tree([42])
copy2 = CopyTree(original2)
print("Test 2 - copy data:", copy2.data)                           # 42
print("Test 2 - different objects:", original2 is not copy2)       # True

# Test 3: None input
print("Test 3 - None input:", CopyTree(None))                      # None

# Test 4: skewed tree (left-only)
original4 = build_tree([1, 2, None, 3])
copy4 = CopyTree(original4)
print("Test 4 - original inorder:", inorder(original4))
print("Test 4 - copy inorder:    ", inorder(copy4))

# Spent a total of 15 mins on this question

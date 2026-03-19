# Question 14: FloorInBST

# Given a target numeric value and a binary search tree, return the floor
# (greatest element less than or equal to the target) in the BST.
# Return None if no such element exists (all values are greater than target).

# Time Complexity = O(log n) — traverse down one path of the BST
# Space Complexity = O(1) — only a floor variable, no extra storage

# Examples:

# BST:      10
#          /  \
#         5   15
#        / \  / \
#       3   7 12  20
# Target: 8  -> Floor: 7
# Target: 10 -> Floor: 10 (exact match)
# Target: 11 -> Floor: 10
# Target: 2  -> Floor: None (no element <= 2)
# Target: 20 -> Floor: 20
# Target: 25 -> Floor: 20


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def FloorInBST(root, target):
    floor = None
    cur = root

    while cur:
        if cur.data == target:
            return cur.data          # exact match is the floor
        elif cur.data > target:
            cur = cur.left           # too big, go left
        else:
            floor = cur.data         # candidate floor, go right for something closer
            cur = cur.right

    return floor


# Helper to build a BST by inserting values
def insert(root, val):
    if not root:
        return Node(val)
    if val < root.data:
        root.left = insert(root.left, val)
    elif val > root.data:
        root.right = insert(root.right, val)
    return root


def build_bst(vals):
    root = None
    for v in vals:
        root = insert(root, v)
    return root


# --- Tests ---

#         10
#        /  \
#       5   15
#      / \  / \
#     3   7 12  20
bst = build_bst([10, 5, 15, 3, 7, 12, 20])

print("Test 1 - target=8,  floor:", FloorInBST(bst, 8))    # 7
print("Test 2 - target=10, floor:", FloorInBST(bst, 10))   # 10 (exact match)
print("Test 3 - target=11, floor:", FloorInBST(bst, 11))   # 10
print("Test 4 - target=2,  floor:", FloorInBST(bst, 2))    # None
print("Test 5 - target=20, floor:", FloorInBST(bst, 20))   # 20 (exact match)
print("Test 6 - target=25, floor:", FloorInBST(bst, 25))   # 20
print("Test 7 - target=6,  floor:", FloorInBST(bst, 6))    # 5
print("Test 8 - target=13, floor:", FloorInBST(bst, 13))   # 12

# Single node tests
bst2 = build_bst([5])
print("Test 9  - single node, target=5:  floor:", FloorInBST(bst2, 5))   # 5
print("Test 10 - single node, target=3:  floor:", FloorInBST(bst2, 3))   # None
print("Test 11 - single node, target=10: floor:", FloorInBST(bst2, 10))  # 5

# Spent a total of 20 mins on this question

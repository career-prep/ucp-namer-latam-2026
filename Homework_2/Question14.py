# Given a target numeric value and a binary search tree, return the floor
# (greatest element less than or equal to the target) in the BST.

# Examples:

# Input: target=13
#            10
#          /    \
#        8       16
#       / \     /  \
#      4   9  13    25
#               \
#                14
# Output: 13

# Input: target=15 (same tree)
# Output: 14

# Technique: Search binary search tree (BST)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def floor_in_bst(root, target):
    result = None
    current = root
    while current:
        if current.data == target:
            return current.data
        elif current.data < target:
            result = current.data
            current = current.right
        else:
            current = current.left
    return result


root = Node(10)
root.left = Node(8)
root.right = Node(16)
root.left.left = Node(4)
root.left.right = Node(9)
root.right.left = Node(13)
root.right.right = Node(25)
root.right.left.right = Node(14)

print(floor_in_bst(root, 13))
print(floor_in_bst(root, 15))
print(floor_in_bst(root, 1))
print(floor_in_bst(root, 10))
print(floor_in_bst(root, 25))
print(floor_in_bst(root, 100))
print(floor_in_bst(None, 5))

# Time Complexity: O(log n)
# Space Complexity: O(1)
# Spent 40 mins

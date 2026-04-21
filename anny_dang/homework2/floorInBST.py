class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def floorInBST(root, target):
    """
    Given a BST and a target value, return the floor:
    the greatest value <= target.

    Idea: walk down the BST. If node <= target, it is a floor
    candidate, save it and move right for a larger valid value.
    If node > target, move left.

    Time: O(h = tree height)
    Space: O(1)
    """
    greatest = -1
    cur = root
    while cur:
        if cur.data < target:
            greatest = cur.data
            cur = cur.right
        elif cur.data > target:
            cur = cur.left
        else:
            return cur.data
    
    return greatest


#          10
#         /  \
#        8    16
#         \   / \
#          9 13 17
#                 \
#                 20
root = Node(10)
root.left = Node(8)
root.left.right = Node(9)

root.right = Node(16)
root.right.left = Node(13)
root.right.right = Node(17)
root.right.right.right = Node(20)


# Example 1
# Input: target = 13
# Output: 13
target1 = 13


# Example 2
# Input: target = 15
# Output: 13
target2 = 15

print(floorInBST(root, target1))
print(floorInBST(root, target2))

# Question 14: FloorInBST
# Technique: Search Binary Search Tree (BST)
# Time: O(log n) avg, O(n) worst
# Space: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def floorInBST(root, target):
    floor_val = None
    cur = root
    while cur:
        if cur.data == target:
            return cur.data
        elif cur.data < target:
            floor_val = cur.data
            cur = cur.right
        else:
            cur = cur.left
    return floor_val


root = Node(10)
root.left = Node(8)
root.left.right = Node(9)
root.right = Node(16)
root.right.left = Node(13)
root.right.right = Node(17)
root.right.right.right = Node(20)

# target=13 → 13
print(floorInBST(root, 13))

# target=15 → 13
print(floorInBST(root, 15))

# time: 36 minutes

# Technique: Search binary search tree (BST)
# Time: O(h)
# Space: O(1)
# Time Spent: 15 minutes


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def floorInBST(root, target):
    floor_val = None
    curr = root

    while curr:
        if curr.data == target:
            return curr.data
        elif curr.data > target:
            curr = curr.left
        else:
            floor_val = curr.data
            curr = curr.right

    return floor_val


root = Node(10)
root.left = Node(8)
root.right = Node(16)
root.left.right = Node(9)
root.right.left = Node(13)
root.right.right = Node(17)
root.right.right.right = Node(20)

print(floorInBST(root, 13))
print(floorInBST(root, 15))
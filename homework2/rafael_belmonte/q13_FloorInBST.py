# Technique: Search binary search tree (BST)
# time complexity: O(log n)
# space complexity: O(1)
# 15 minutes

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def floorInBST(root, target):
    floor = None
    curr = root
    while curr:
        if curr.data == target:
            return curr.data
        elif curr.data < target:
            floor = curr.data  # curr.data is a valid floor candidate; search right for a closer one
            curr = curr.right
        else:
            curr = curr.left  # curr.data too large; search left
    return floor

# test cases

# BST: 10 -> (8, 16) -> (9, 13, 17) -> (20)
root = Node(10)
root.left = Node(8)
root.right = Node(16)
root.left.right = Node(9)
root.right.left = Node(13)
root.right.right = Node(17)
root.right.right.right = Node(20)

assert floorInBST(root, 13) == 13   # exact match
assert floorInBST(root, 15) == 13   # between 13 and 16
assert floorInBST(root, 10) == 10   # exact match at root
assert floorInBST(root, 7) is None  # smaller than all values
assert floorInBST(root, 21) == 20   # larger than all values
assert floorInBST(root, 16) == 16   # exact match internal node

print("yay!!")

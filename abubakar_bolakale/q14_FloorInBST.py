class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def findFloor(root, target):
    floor = None
    curr = root

    while curr:
        if curr.val == target:
            return curr.val

        if curr.val > target:
            curr = curr.left
        else:
            floor = curr.val
            curr = curr.right

    return floor

def insert(root, val):
    if not root:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

values = [10, 5, 15, 2, 7]
root = None
for v in values:
    root = insert(root, v)

print(f"Floor of 6:  {findFloor(root, 6)}")
print(f"Floor of 11: {findFloor(root, 11)}")
print(f"Floor of 15: {findFloor(root, 15)}")
print(f"Floor of 1:  {findFloor(root, 1)}")

# Technique: Search Binary Search Tree (BST) - Iterative
# Time Complexity: O(h) 
# Space Complexity: O(1)
# Time Spent: 30 minutes
# Technique used: Search binary search tree (BST)
# Time Complexity: O(log n)
# Space Complexity: O(1)

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
            floor = curr.data
            curr = curr.right
        else:
            curr = curr.left

    return floor


def buildBST():
    root = Node(10)
    root.left = Node(8)
    root.right = Node(16)
    root.left.right = Node(9)
    root.right.left = Node(13)
    root.right.right = Node(17)
    root.right.right.right = Node(20)
    return root


print("floorInBST Results:")

bst = buildBST()
print(floorInBST(bst, 13))
print(floorInBST(bst, 15))
print(floorInBST(bst, 10))
print(floorInBST(bst, 7))
print(floorInBST(bst, 20))
print(floorInBST(bst, 100))
print(floorInBST(bst, 9))
print(floorInBST(bst, 11))

# Time Taken: 25 mins

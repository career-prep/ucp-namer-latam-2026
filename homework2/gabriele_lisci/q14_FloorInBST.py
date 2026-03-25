# Runtime: O(h) where h is the height of the tree (O(log n) for balanced, O(n) for skewed)
# Space complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def FloorInBST(root, target):
    floor = None
    curr = root

    while curr:
        if curr.data == target:
            return curr.data

        if curr.data > target:
            curr = curr.left
        else:
            floor = curr.data
            curr = curr.right

    return floor

def run_tests():
    # 1. Test Standard BST
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(7)

    assert FloorInBST(root, 6) == 5
    assert FloorInBST(root, 11) == 10
    assert FloorInBST(root, 15) == 15
    assert FloorInBST(root, 1) is None
    print("Standard BST tests passed")

    # 2. Test single node
    root2 = Node(100)
    assert FloorInBST(root2, 150) == 100
    assert FloorInBST(root2, 50) is None
    print("Single node tests passed")

    # 3. Test empty tree
    assert FloorInBST(None, 10) is None
    print("Empty tree test passed")

run_tests()

# Time spent: 28:00

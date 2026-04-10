# Technique: Search BST because a target value must be searched for.
# Time Complexity: O(h) where h is the height of the tree.
# Space Complexity: O(1) because this is done iteratively rather than recursion.

from typing import Optional

class Node:
    def __init__(self, data: int):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

def FloorInBST(root: Optional[Node], target: int) -> Optional[int]:
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

def TestCase():
    root = Node(10)
    root.left = Node(8)
    root.left.right = Node(9)
    
    root.right = Node(16)
    root.right.left = Node(13)
    root.right.right = Node(17)
    root.right.right.right = Node(20)

    print(f"Output: {FloorInBST(root, 13)}")

TestCase()

# Time Spent: 9 minutes
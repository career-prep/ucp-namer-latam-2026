# Technique: Pre-order traversal because it follows pattern of root, left, right
# Time Complexity: O(n) because recursive calls are needed to visit every single node.
# Space Complexity: O(h) where h is the height of the tree.

from typing import Optional

class Node:
    def __init__(self, data: int):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

def CopyTree(root: Optional[Node]) -> Optional[Node]:
    if not root:
        return None
    
    new_node = Node(root.data)

    new_node.left = CopyTree(root.left)
    new_node.right = CopyTree(root.right)

    return new_node

def TestCase():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(13)

    copy = CopyTree(root)

    print(f"Original Root: {root.data}, Copy Root: {copy.data}")
    print(f"Original Left: {root.left.data}, Copy Left: {copy.left.data}")

TestCase()

# Time Spent: 5 minutes
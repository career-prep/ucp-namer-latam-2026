# Technique: In-order traversal because a valid BST visits nodes in left, root, right
# Time Complexity: O(n) because recursive calls are needed to visit every single node.
# Space Complexity: O(h) where h is the height of the tree.

from typing import Optional

class Node:
    def __init__(self, data: int):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

def inorder(root: Optional[Node], prev: list) -> bool:
    if not root:
        return True
    
    if not inorder(root.left, prev):
        return False
    
    if root.data <= prev[0]:
        return False
    
    prev[0] = root.data

    return inorder(root.right, prev)

def isBST(root: Optional[Node]) -> bool:
    prev = [float('-inf')]
    return inorder(root, prev)

def ValidTree():
    root = Node(10)
    root.left = Node(8)
    root.right = Node(16)

    root.left.right = Node(9)
    
    root.right.left = Node(13)
    root.right.right = Node(17)

    root.right.right.right = Node(20)
    
    return root

def InvalidTree():
    root = Node(10)
    root.left = Node(8)
    root.right = Node(16)
    
    root.left.right = Node(9)
    root.right.left = Node(13)
    root.right.right = Node(17)

    root.right.right.right = Node(15)
    return root

valid_root = ValidTree()
invalid_root = InvalidTree()

print(isBST(valid_root))
print(isBST(invalid_root))

# Time Spent: 18 minutes
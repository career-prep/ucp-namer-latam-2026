class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def getLeftView(node, level=0, result=None):
    if result is None:
        result = []

    if not node:
        return result

    if level == len(result):
        result.append(node.val)

    getLeftView(node.left, level + 1, result)
    getLeftView(node.right, level + 1, result)

    return result

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.right = Node(4)
root1.right.right = Node(5)

print(f"Test 1 (Standard): {getLeftView(root1)}")

root2 = Node(1)
root2.right = Node(2)
root2.right.right = Node(3)

print(f"Test 2 (Right-heavy): {getLeftView(root2)}")

print(f"Test 3 (Empty): {getLeftView(None)}")

# Technique: Tree Traversal - Depth-first (Recursive)
# Time Complexity: O(n)
# Space Complexity: O(h)
# Time Spent: 15 minutes
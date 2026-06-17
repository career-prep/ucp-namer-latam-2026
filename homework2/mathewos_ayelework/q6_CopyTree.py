# Technique used: Depth-first traversal (pre-order)
# Time Complexity: O(n)
# Space Complexity: O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def copyTree(root):
    if not root:
        return None
    new_node = Node(root.data)
    new_node.left = copyTree(root.left)
    new_node.right = copyTree(root.right)
    return new_node


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.data] + inorder(root.right)


print("copyTree Results:")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

copy = copyTree(root)
print(inorder(root))
print(inorder(copy))

root.left.data = 99
print(inorder(root))
print(inorder(copy))

print(inorder(copyTree(Node(10))))
print(copyTree(None))

# Time Taken: 20 mins

# Qustion 8: Is_BST
# Technique: Search Binary Search Tree (BST)
# Time: O(n)
# Space: O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def Is_BST(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if root.data <= min_val or root.data >= max_val:
        return False
    return (Is_BST(root.left, min_val, root.data) and
            Is_BST(root.right, root.data, max_val))


root1 = Node(10)
root1.left = Node(8)
root1.left.right = Node(9)
root1.right = Node(16)
root1.right.left = Node(13)
root1.right.right = Node(17)
root1.right.right.right = Node(20)

# true
print(Is_BST(root1))

root2 = Node(10)
root2.left = Node(8)
root2.left.right = Node(9)
root2.right = Node(16)
root2.right.left = Node(13)
root2.right.right = Node(17)
root2.right.right.right = Node(15)

# false
print(Is_BST(root2))

# time: 20 minutes

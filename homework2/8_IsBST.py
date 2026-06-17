# Technique: Depth-first traversal (in-order)
# Time: O(n)
# Space: O(n)
# Time Spent: 25 minutes


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBST(root):
    def helper(node, low, high):
        if not node:
            return True

        if not (low < node.data < high):
            return False

        return helper(node.left, low, node.data) and helper(node.right, node.data, high)

    return helper(root, float('-inf'), float('inf'))


# Test cases
root1 = Node(10)
root1.left = Node(8)
root1.right = Node(16)
root1.left.right = Node(9)
root1.right.left = Node(13)
root1.right.right = Node(17)
root1.right.right.right = Node(20)

print(isBST(root1))

root2 = Node(10)
root2.left = Node(8)
root2.right = Node(16)
root2.left.right = Node(9)
root2.right.left = Node(13)
root2.right.right = Node(17)
root2.right.right.right = Node(15)

print(isBST(root2))
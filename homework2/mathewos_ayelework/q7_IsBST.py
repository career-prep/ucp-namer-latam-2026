# Technique used: Depth-first traversal (in-order)
# Time Complexity: O(n)
# Space Complexity: O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBST(root):
    result = []

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.data)
        inorder(node.right)

    inorder(root)

    for i in range(1, len(result)):
        if result[i] <= result[i - 1]:
            return False
    return True


print("isBST Results:")

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

print(isBST(Node(5)))
print(isBST(None))

root3 = Node(5)
root3.left = Node(10)
root3.right = Node(7)
print(isBST(root3))

# Time Taken: 25 mins

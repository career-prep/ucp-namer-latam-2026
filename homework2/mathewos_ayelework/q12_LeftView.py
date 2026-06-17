# Technique used: Level-order (breadth-first) traversal
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def leftView(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == 0:
                result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


print("leftView Results:")

root1 = Node(7)
root1.left = Node(8)
root1.right = Node(3)
root1.right.left = Node(9)
root1.right.right = Node(13)
root1.right.left.left = Node(20)
root1.right.left.right = Node(14)
root1.right.left.right.right = Node(15)
print(leftView(root1))

root2 = Node(7)
root2.left = Node(20)
root2.right = Node(4)
root2.left.left = Node(15)
root2.left.right = Node(6)
root2.right.left = Node(8)
root2.right.right = Node(11)
print(leftView(root2))

print(leftView(Node(1)))
print(leftView(None))

root3 = Node(1)
root3.right = Node(2)
root3.right.right = Node(3)
print(leftView(root3))

# Time Taken: 30 mins

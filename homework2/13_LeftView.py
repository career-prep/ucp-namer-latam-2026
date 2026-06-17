# Technique: Level-order (breadth-first) traversal
# Time: O(n)
# Space: O(n)
# Time Spent: 20 minutes


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
        size = len(queue)

        for i in range(size):
            node = queue.popleft()

            if i == 0:
                result.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


root1 = Node(7)
root1.left = Node(8)
root1.right = Node(3)
root1.right.left = Node(9)
root1.right.right = Node(13)
root1.right.left.left = Node(20)
root1.right.right.left = Node(14)
root1.right.right.left.right = Node(15)

print(leftView(root1))


root2 = Node(7)
root2.left = Node(20)
root2.right = Node(4)
root2.left.left = Node(15)
root2.left.right = Node(6)
root2.right.left = Node(8)
root2.right.right = Node(11)

print(leftView(root2))
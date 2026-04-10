# Approach:
# Use level-order traversal (BFS)
# For each level, the first node we see is the leftmost node
# So for every level, record the first element

# Time Complexity: O(n)


# Space Complexity: O(n)


from collections import deque

def leftView(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            # first node of this level → left view
            if i == 0:
                result.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result
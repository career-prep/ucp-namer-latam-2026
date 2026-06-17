# Runtime: O(n)
# Space complexity: O(w) where w is the max width of the tree

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def LeftView(root):
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

def run_tests():
    # 1. Test Standard Tree
    #      1
    #    /   \
    #   2     3
    #    \   / \
    #     4 5   6
    # Left view should be [1, 2, 4]
    h1 = Node(1)
    h1.left = Node(2)
    h1.right = Node(3)
    h1.left.right = Node(4)
    h1.right.left = Node(5)
    h1.right.right = Node(6)
    assert LeftView(h1) == [1, 2, 4]
    print("Standard tree test passed")

    # 2. Test Right-Skewed Tree
    #  1
    #   \
    #    2
    #     \
    #      3
    h2 = Node(1)
    h2.right = Node(2)
    h2.right.right = Node(3)
    assert LeftView(h2) == [1, 2, 3]
    print("Right-skewed tree test passed")

    # 3. Test Left-Skewed Tree
    h3 = Node(10)
    h3.left = Node(20)
    h3.left.left = Node(30)
    assert LeftView(h3) == [10, 20, 30]
    print("Left-skewed tree test passed")

    # 4. Test Single Node
    assert LeftView(Node(5)) == [5]
    print("Single node test passed")

    # 5. Test Empty Tree
    assert LeftView(None) == []
    print("Empty tree test passed")

run_tests()

# Time spent: 30:30

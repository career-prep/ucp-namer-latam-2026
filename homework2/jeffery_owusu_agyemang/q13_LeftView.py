"""
Technique: Level-order (breadth-first) traversal
Time Complexity: O(n) - Every node is visited once.
Space Complexity: O(w) - Where w is the maximum width of the tree (size of the queue).
"""
from collections import deque

def left_view(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == 0:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result

# --- Test Cases ---
if __name__ == "__main__":
    # Tree:    7
    #        /   \
    #       8     20
    #        \    /
    #         9  15
    tree = Node(7, Node(8, None, Node(9)), Node(20, Node(15)))
    print(f"Left View: {left_view(tree)}") # Expected: [7, 8, 9] or [7, 8, 15]
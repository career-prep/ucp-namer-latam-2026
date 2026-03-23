# Technique: Level-order traversal (BFS)
# Time Complexity: O(n)
# Space Complexity: O(w), where w is the maximum width of the tree

from collections import deque


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def left_view(root: Node) -> list[int]:
    
    if root is None:
        return []

    visible_values = []
    node_queue = deque([root])

    while node_queue:
        level_size = len(node_queue)

        for position_in_level in range(level_size):
            current_node = node_queue.popleft()

            # The first node at this level is the one visible from the left
            if position_in_level == 0:
                visible_values.append(current_node.value)

            if current_node.left is not None:
                node_queue.append(current_node.left)

            if current_node.right is not None:
                node_queue.append(current_node.right)

    return visible_values


def run_tests() -> None:
    # empty tree
    assert left_view(None) == []

    # single node
    single_root = Node(10)
    assert left_view(single_root) == [10]

    # balanced tree
    balanced_root = Node(1)
    balanced_root.left = Node(2)
    balanced_root.right = Node(3)
    balanced_root.left.left = Node(4)
    balanced_root.left.right = Node(5)
    balanced_root.right.left = Node(6)
    balanced_root.right.right = Node(7)
    assert left_view(balanced_root) == [1, 2, 4]

    # left skewed tree
    left_skewed_root = Node(1)
    left_skewed_root.left = Node(2)
    left_skewed_root.left.left = Node(3)
    left_skewed_root.left.left.left = Node(4)
    assert left_view(left_skewed_root) == [1, 2, 3, 4]

    # right skewed tree
    right_skewed_root = Node(1)
    right_skewed_root.right = Node(2)
    right_skewed_root.right.right = Node(3)
    right_skewed_root.right.right.right = Node(4)
    assert left_view(right_skewed_root) == [1, 2, 3, 4]

    # uneven tree
    uneven_root = Node(1)
    uneven_root.left = Node(2)
    uneven_root.right = Node(3)
    uneven_root.left.right = Node(5)
    uneven_root.right.right = Node(4)
    assert left_view(uneven_root) == [1, 2, 5]

    # another uneven tree
    another_root = Node(8)
    another_root.left = Node(4)
    another_root.right = Node(12)
    another_root.left.left = Node(2)
    another_root.right.left = Node(10)
    another_root.right.right = Node(14)
    another_root.right.left.left = Node(9)
    assert left_view(another_root) == [8, 4, 2, 9]

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
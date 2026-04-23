# Technique: Depth-first traversal (recursive tree copy)
# Time Complexity: O(n)
# Space Complexity: O(h) recursion stack, where h is tree height
# In the worst case, h can be O(n)

from collections import deque


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def copy_tree(root: Node) -> Node:
    
    if root is None:
        return None

    copied_root = Node(root.value)
    copied_root.left = copy_tree(root.left)
    copied_root.right = copy_tree(root.right)

    return copied_root


def level_order_values(root: Node) -> list:
    
    if root is None:
        return []

    values = []
    node_queue = deque([root])

    while node_queue:
        current_node = node_queue.popleft()

        if current_node is None:
            values.append(None)
        else:
            values.append(current_node.value)
            node_queue.append(current_node.left)
            node_queue.append(current_node.right)

    while values and values[-1] is None:
        values.pop()

    return values


def run_tests() -> None:
    # empty tree
    assert copy_tree(None) is None

    # single node tree
    single_root = Node(10)
    copied_single_root = copy_tree(single_root)

    assert copied_single_root is not single_root
    assert copied_single_root.value == 10
    assert copied_single_root.left is None
    assert copied_single_root.right is None

    # larger tree
    original_root = Node(8)
    original_root.left = Node(4)
    original_root.right = Node(12)
    original_root.left.left = Node(2)
    original_root.left.right = Node(6)
    original_root.right.left = Node(10)
    original_root.right.right = Node(14)

    copied_root = copy_tree(original_root)

    assert level_order_values(original_root) == [8, 4, 12, 2, 6, 10, 14]
    assert level_order_values(copied_root) == [8, 4, 12, 2, 6, 10, 14]

    assert copied_root is not original_root
    assert copied_root.left is not original_root.left
    assert copied_root.right is not original_root.right
    assert copied_root.left.left is not original_root.left.left

    copied_root.left.value = 999
    assert original_root.left.value == 4
    assert copied_root.left.value == 999

    original_root.right.right.value = 777
    assert copied_root.right.right.value == 14
    assert original_root.right.right.value == 777

    print("All tests passed")


if __name__ == "__main__":
    run_tests()

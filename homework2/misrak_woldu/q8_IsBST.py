# Technique: Depth-first traversal with valid min/max range
# Time Complexity: O(n)
# Space Complexity: O(h) recursion stack, where h is tree height
# In the worst case, h can be O(n)

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def is_bst(root: Node) -> bool:

    def validate_subtree(current_node: Node, min_allowed, max_allowed) -> bool:
        if current_node is None:
            return True

        if not (min_allowed < current_node.value < max_allowed):
            return False

        return (
            validate_subtree(current_node.left, min_allowed, current_node.value)
            and validate_subtree(current_node.right, current_node.value, max_allowed)
        )

    return validate_subtree(root, float("-inf"), float("inf"))


def run_tests() -> None:
    # empty tree
    assert is_bst(None) is True

    # single node
    single_root = Node(10)
    assert is_bst(single_root) is True

    # valid BST
    valid_root = Node(8)
    valid_root.left = Node(4)
    valid_root.right = Node(12)
    valid_root.left.left = Node(2)
    valid_root.left.right = Node(6)
    valid_root.right.left = Node(10)
    valid_root.right.right = Node(14)
    assert is_bst(valid_root) is True

    # invalid BST: left child greater than parent
    invalid_root_one = Node(8)
    invalid_root_one.left = Node(9)
    invalid_root_one.right = Node(12)
    assert is_bst(invalid_root_one) is False

    # invalid BST: right child smaller than parent
    invalid_root_two = Node(8)
    invalid_root_two.left = Node(4)
    invalid_root_two.right = Node(7)
    assert is_bst(invalid_root_two) is False

    # invalid BST: deeper violation
    # 10 is in the left subtree of 8 so it should not be there
    invalid_root_three = Node(8)
    invalid_root_three.left = Node(4)
    invalid_root_three.right = Node(12)
    invalid_root_three.left.left = Node(2)
    invalid_root_three.left.right = Node(10)
    assert is_bst(invalid_root_three) is False

    # invalid BST: duplicate values not allowed in this implementation
    duplicate_root = Node(8)
    duplicate_root.left = Node(4)
    duplicate_root.right = Node(8)
    assert is_bst(duplicate_root) is False

    # skewed valid BST
    right_skewed_root = Node(1)
    right_skewed_root.right = Node(2)
    right_skewed_root.right.right = Node(3)
    right_skewed_root.right.right.right = Node(4)
    assert is_bst(right_skewed_root) is True

    left_skewed_root = Node(4)
    left_skewed_root.left = Node(3)
    left_skewed_root.left.left = Node(2)
    left_skewed_root.left.left.left = Node(1)
    assert is_bst(left_skewed_root) is True

    print("All tests passed")


if __name__ == "__main__":
    run_tests()

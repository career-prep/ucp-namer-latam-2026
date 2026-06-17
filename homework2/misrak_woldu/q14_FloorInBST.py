# Technique: BST search / traversal
# Time Complexity: O(h), where h is the height of the tree
# Space Complexity: O(1)

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def floor_in_bst(root: Node, target: int):
    
    current_node = root
    best_floor = None

    while current_node is not None:
        
        if current_node.value == target:
            return current_node.value

        if current_node.value < target:
            best_floor = current_node.value
            current_node = current_node.right
        else:
            
            current_node = current_node.left

    return best_floor


def run_tests() -> None:
    # empty tree
    assert floor_in_bst(None, 10) is None

    # build BST
    root = Node(8)
    root.left = Node(4)
    root.right = Node(12)
    root.left.left = Node(2)
    root.left.right = Node(6)
    root.right.left = Node(10)
    root.right.right = Node(14)

    # exact matches
    assert floor_in_bst(root, 8) == 8
    assert floor_in_bst(root, 2) == 2
    assert floor_in_bst(root, 14) == 14

    # between values
    assert floor_in_bst(root, 5) == 4
    assert floor_in_bst(root, 7) == 6
    assert floor_in_bst(root, 11) == 10
    assert floor_in_bst(root, 13) == 12

    # below smallest value
    assert floor_in_bst(root, 1) is None

    # above largest value
    assert floor_in_bst(root, 20) == 14

    # single node
    single_root = Node(10)
    assert floor_in_bst(single_root, 10) == 10
    assert floor_in_bst(single_root, 9) is None
    assert floor_in_bst(single_root, 15) == 10

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
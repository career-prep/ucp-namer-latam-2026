# Technique: Binary Search Tree Basics
# Time Complexity:
# - min: O(log n) average
# - max: O(log n) average
# - contains: O(log n) average
# - insert: O(log n) average
# - delete: O(log n) average
#
# Space Complexity:
# - O(1) extra space for iterative methods
# - O(h) recursion stack for recursive helpers where h is tree height


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def min(self) -> int:
        
        if self.root is None:
            raise ValueError("BST is empty")

        current_node = self.root
        while current_node.left is not None:
            current_node = current_node.left

        return current_node.value

    def max(self) -> int:
        
        if self.root is None:
            raise ValueError("BST is empty")

        current_node = self.root
        while current_node.right is not None:
            current_node = current_node.right

        return current_node.value

    def contains(self, target_value: int) -> bool:
        
        current_node = self.root

        while current_node is not None:
            if target_value == current_node.value:
                return True
            if target_value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return False

    def insert(self, value_to_insert: int) -> None:
        
        if self.root is None:
            self.root = Node(value_to_insert)
            return

        current_node = self.root

        while True:
            if value_to_insert == current_node.value:
                return  
            if value_to_insert < current_node.value:
                if current_node.left is None:
                    current_node.left = Node(value_to_insert)
                    return
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = Node(value_to_insert)
                    return
                current_node = current_node.right

    def delete(self, value_to_delete: int) -> None:
        
        self.root = self._delete_recursive(self.root, value_to_delete)

    def _delete_recursive(self, current_node: Node, value_to_delete: int):
        if current_node is None:
            return None

        if value_to_delete < current_node.value:
            current_node.left = self._delete_recursive(current_node.left, value_to_delete)
            return current_node

        if value_to_delete > current_node.value:
            current_node.right = self._delete_recursive(current_node.right, value_to_delete)
            return current_node

        if current_node.left is None and current_node.right is None:
            return None

        if current_node.left is None:
            return current_node.right

        if current_node.right is None:
            return current_node.left

        successor_value = self._find_min_value(current_node.right)
        current_node.value = successor_value
        current_node.right = self._delete_recursive(current_node.right, successor_value)
        return current_node

    def _find_min_value(self, subtree_root: Node) -> int:
        current_node = subtree_root
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def inorder_values(self) -> list[int]:
        
        values = []
        self._inorder_traversal(self.root, values)
        return values

    def _inorder_traversal(self, current_node: Node, values: list[int]) -> None:
        if current_node is None:
            return

        self._inorder_traversal(current_node.left, values)
        values.append(current_node.value)
        self._inorder_traversal(current_node.right, values)


def run_tests() -> None:
    bst = BinarySearchTree()

    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(18)

    assert bst.contains(10) is True
    assert bst.contains(7) is True
    assert bst.contains(99) is False

    bst.insert(10)
    bst.insert(5)
    assert bst.inorder_values() == [3, 5, 7, 10, 12, 15, 18]

    assert bst.min() == 3
    assert bst.max() == 18

    bst.delete(3)
    assert bst.inorder_values() == [5, 7, 10, 12, 15, 18]

    bst.delete(5)
    assert bst.inorder_values() == [7, 10, 12, 15, 18]

    bst.delete(15)
    assert bst.inorder_values() == [7, 10, 12, 18]

    bst.delete(10)
    assert bst.inorder_values() == [7, 12, 18]
 
    bst.delete(999)
    assert bst.inorder_values() == [7, 12, 18]

    single_bst = BinarySearchTree()
    single_bst.insert(42)
    assert single_bst.min() == 42
    assert single_bst.max() == 42
    assert single_bst.contains(42) is True

    single_bst.delete(42)
    assert single_bst.inorder_values() == []

    empty_bst = BinarySearchTree()

    try:
        empty_bst.min()
        assert False
    except ValueError:
        pass

    try:
        empty_bst.max()
        assert False
    except ValueError:
        pass

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
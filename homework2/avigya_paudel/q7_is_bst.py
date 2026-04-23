# Technique: Tree Traversal Generic

# Time Complexity: O(N)
# Space Complexity: O(N)

# Time taken: 8 minutes

class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node|None = None
        self.right: Node|None = None

def is_bst(root):
    return test_is_bst(root, -float("inf"), float("inf"))

def test_is_bst(root, min, max):
    if not root:
        return True 
    if min <= root.data <= max:
        return test_is_bst(root.left, min, root.data) and test_is_bst(root.right, root.data, max)
    else:
        return False


if __name__ == "__main__":
    #        10
    #       /  \
    #      5    15
    #     / \     \
    #    3   7    20
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.right = Node(20)
    print(is_bst(root))
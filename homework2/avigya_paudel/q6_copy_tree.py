# Technique: Generic Tree Traversal

# Time Complexity: O(N)
# Space Complexity: O(log(N))

# Time taken: 15 minutes

class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node|None = None
        self.right: Node|None = None

def copy_tree(root):
    # returns a deep copy of the tree
    if not root:
        return None
    
    copy_root = Node(root.data)
    copy_root.left = copy_tree(root.left)
    copy_root.right = copy_tree(root.right)

    return copy_root

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

    copy = copy_tree(root)

    print(copy.data)               # 10
    print(copy.left.data)          # 5
    print(copy.right.data)         # 15
    print(copy.left.left.data)     # 3
    print(copy.left.right.data)    # 7
    print(copy.right.right.data)   # 20

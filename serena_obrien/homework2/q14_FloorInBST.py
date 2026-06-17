# Time complexity: O(log n)
# Space complexity: O(1)

# Technique: Search binary search tree (BST)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def contains(self, val):
        def _contains(node, val):
            if not node:
                return False
            if node.data == val:
                return True
            elif val < node.data:
                return _contains(node.left, val)
            else:
                return _contains(node.right, val)

        return _contains(self.root, val)

    def insert(self, val):
        def _insert(node, val):
            if not node:
                return Node(val)
            if val < node.data:
                node.left = _insert(node.left, val)
            elif val > node.data:
                node.right = _insert(node.right, val)
            return node
    
        self.root = _insert(self.root, val)

def floorBST(root, target):
    floor_val = None

    while root:
        if root.data == target:
            return root.data
        elif root.data > target:
            root = root.left
        else:
            floor_val = root.data
            root = root.right

    return floor_val

if __name__ == '__main__':
    bst = BST()
    for val in [20, 10, 30, 5, 15, 25, 35]:
        bst.insert(val)

    tests = [4, 5, 12, 15, 16, 20, 26, 35, 40]

    for target in tests:
        f = floorBST(bst.root, target)
        print(f"Floor of {target}: {f}")


    """
    Floor of 4: None   # smaller than all nodes
    Floor of 5: 5
    Floor of 12: 10
    Floor of 15: 15
    Floor of 16: 15
    Floor of 20: 20
    Floor of 26: 25
    Floor of 35: 35
    Floor of 40: 35  # largest node
    """

# ~ time spent: 35 minutes
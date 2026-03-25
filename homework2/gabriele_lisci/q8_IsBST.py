# Runtime: O(n)
# Space complexity: O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBST(root):
    def helper(node, low, high):
        if not node:
            return True

        if not (low < node.data < high):
            return False

        return (helper(node.left, low, node.data) and
                helper(node.right, node.data, high))

    return helper(root, float('-inf'), float('inf'))

def run_tests():

    # 1. Test Valid BST
    root1 = Node(5)
    root1.left = Node(3)
    root1.right = Node(7)
    assert isBST(root1) == True
    print("Valid BST test passed")

    # 2. Test Invalid BST
    root2 = Node(5)
    root2.left = Node(3)
    root2.right = Node(4)
    assert isBST(root2) == False
    print("Invalid BST (out of range) passed")

    # 3. Test Invalid BST
    root3 = Node(10)
    root3.left = Node(5)
    root3.right = Node(15)
    root3.right.left = Node(6)
    assert isBST(root3) == False
    print("Invalid BST (sub-child violation) passed")

    # 4. Test Single Node
    root4 = Node(10)
    assert isBST(root4) == True
    print("Single node test passed")

    # 5. Test Empty Tree
    assert isBST(None) == True
    print("Empty tree test passed")

if __name__ == "__main__":
    run_tests()

# Time spent: 40:00

# Technique: Search binary search tree (BST)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBST(root): # Time, Space Complexities: O(n), O(n)
    #1. Define helper to enforce range constraints (min/max) for each node
    def validate(node, min_val, max_val):
        #2. Base case: an empty tree is a valid BST
        if not node:
            return True
        
        #3. Check if current node value violates the min/max constraints
        if not (min_val < node.data < max_val):
            return False
        
        #4. Recursively validate subtrees with updated ranges
        # Left child must be < node.data ^ Right child must be > node.data
        return (validate(node.left, min_val, node.data) and 
                validate(node.right, node.data, max_val))

    #5. Start recursion with infinity as initial boundaries
    return validate(root, float('-inf'), float('inf'))

class TestIsBST:
    def run_tests(self):
        #1. Valid BST test case
        root1 = Node(10)
        root1.left = Node(8)
        root1.right = Node(16)
        root1.left.right = Node(9)
        root1.right.left = Node(13)
        root1.right.right = Node(17)
        root1.right.right.right = Node(20)
        assert isBST(root1) is True
        
        root2 = Node(10)
        root2.left = Node(8)
        root2.right = Node(16)
        root2.right.right = Node(17)
        root2.right.right.right = Node(15) 
        assert isBST(root2) is False

        print("All tests passed")

if __name__ == "__main__":
    tester = TestIsBST()
    tester.run_tests()
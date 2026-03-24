# Technique: Depth-first traversal (Pre-order)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def copyTree(root): # Time, Space Complexities: O(n), O(n)
    #1. Base case: if current node is None, return None
    if root is None:
        return None
    
    #2. Create a new node with data from the original (Pre-order)
    new_node = Node(root.data)
    
    #3. Recursively copy the left and right subtrees
    new_node.left = copyTree(root.left)
    new_node.right = copyTree(root.right)
    
    #4. Return the new root of the copied subtree
    return new_node

#playing w class test instead of =func test
class TestCopyTree:
    def run_tests(self):
        #1. case: Empty Tree
        assert copyTree(None) is None
        
        #2. case: Single Node
        root = Node(10)
        copied = copyTree(root)
        assert copied is not None
        assert copied.data == 10
        assert copied is not root  # Ensure it is a deep copy (different memory address)
        
        #3. case: Full Binary Tree
        # Structure: 1
        #          /   \
        #         2     3
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        
        copied = copyTree(root)
        assert copied.data == 1
        assert copied.left.data == 2
        assert copied.right.data == 3
        
        #4. Verify Deep Copy Independence
        # Changing the copy should not affect the og
        copied.left.data = 99
        assert root.left.data == 2
        assert copied.left.data == 99
        
        print("All tests passed")

if __name__ == "__main__":
    tester = TestCopyTree()
    tester.run_tests()
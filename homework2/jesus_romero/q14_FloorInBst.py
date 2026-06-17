# Technique: Search binary search tree (BST)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def floorInBST(root, target): # Time, Space Complexities: O(log n), O(1).
    floor = None
    current = root
    
    #1. Traverse the tree starting from the root
    while current is not None:
        #2. If current data matches target, return it as the exact floor
        if current.data == target:
            return current.data
        
        #3. If current data is larger than target, go left to find smaller values
        if current.data > target:
            current = current.left
        else:
            #4. If current data is smaller than target, it's a potential floor
            # Store it and move right to see if a larger floor exists
            floor = current.data
            current = current.right
            
    #5. Return the largest value found that was less than the target
    return floor

def run_test():
    #1. Build the BST from the example image
    root = Node(10)
    root.left = Node(8)
    root.right = Node(16)
    root.left.right = Node(9)
    root.right.left = Node(13)
    root.right.right = Node(17)
    root.right.right.right = Node(20)
    
    #2. Test Target = 13 (Exact match)
    assert floorInBST(root, 13) == 13
    
    #3. Test Target = 15 (Largest value <= 15 is 13)
    assert floorInBST(root, 15) == 13
    
    #4. Test Target = 7 (No values <= 7 exist in this tree)
    assert floorInBST(root, 7) is None
    
    print("All tests passed: Floor found correctly.")

if __name__ == "__main__":
    run_test()
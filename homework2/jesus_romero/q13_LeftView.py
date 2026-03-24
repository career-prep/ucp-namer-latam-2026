# Technique: Level-order (breadth-first) traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def leftView(root): # Time, Space Complexities: O(n), O(w) where w is max width
    #1. Handle empty tree case
    if not root:
        return []
    
    result = []
    #2. Initialize q with the root node
    queue = [root]
    
    #3. Process the tree level by level
    while queue:
        #4. The number of nodes currently in the queue is the size of the current level
        level_size = len(queue)
        
        for i in range(level_size):
            curr = queue.pop(0)
            
            #5. If it's the first node of the current level then add it to results
            if i == 0:
                result.append(curr.data)
            
            #6. Add children to the queue for the next level
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
                
    return result

def run_test():
    #1. Build the tree from the first example
    root = Node(7)
    root.left = Node(8)
    root.right = Node(3)
    root.right.left = Node(9)
    root.right.right = Node(13)
    root.right.left.left = Node(20)
    root.right.right.left = Node(14)
    root.right.right.left.right = Node(15)
    
    #2. Execute and verify
    output = leftView(root)
    assert output == [7, 8, 9, 20, 15]
    
    #3. Build second example
    root2 = Node(7)
    root2.left = Node(20)
    root2.right = Node(4)
    root2.left.left = Node(15)
    root2.left.right = Node(6)
    root2.right.left = Node(8)
    root2.right.right = Node(11)
    
    output2 = leftView(root2)
    assert output2 == [7, 20, 15]
    
    print("All tests passed: Left view captured correctly.")

if __name__ == "__main__":
    run_test()
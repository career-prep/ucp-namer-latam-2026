# Hi Luis, I hope grading is going well! I wanted to let you know q4, q5 and q6 were Queue and 
# Stack problems marked as "Bonus questions" which I have skipped for now. Hence the jump from q3 
# to q7. I'll return to these in my own time to review before the next workshop. 


class Node:
    def __init__(self,value):
        self.right = None
        self.left = None
        self.value = value

#  5      
# 4 7   
#3 6 8  
    
def recursive_copy(node): # time and space complexity is O(n)
    if node is None:
        return None

    newNode = Node(node.value)

    newNode.left = recursive_copy(node.left)
    newNode.right = recursive_copy(node.right)

    return newNode

# This took me less than 10 minutes. 

def tree_to_list(node):
    if node is None:
        return []

    result = []

    left_values = tree_to_list(node.left)
    result += left_values

    result.append(node.value)

    right_values = tree_to_list(node.right)
    result += right_values

    return result

def main():
    # Build tree:
    #       5
    #     4   7
    #    /   / \
    #   3   6   8
    root = Node(5)
    root.left = Node(4)
    root.right = Node(7)
    root.left.left = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(8)

    copy = recursive_copy(root)

    print("Original:", tree_to_list(root))  
    print("Copy:    ", tree_to_list(copy))  

    print("Empty:   ", recursive_copy(None)) 


main()

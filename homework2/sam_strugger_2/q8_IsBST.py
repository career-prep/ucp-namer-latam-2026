class Node:
    def __init__(self,value):
        self.right = None
        self.left = None
        self.value = value


# everything to the left of the root is less than the root
# everything to the right is greater than the root


# Struggled to turn concept into code, below is what I had at 40 minutes 
def isBst(node, min, max):
    
    if node is None:
        return True

    valid_left_tree = isBst(node.left)
    
    valid_right_tree = isBst(node.right)

    if node.left.value < node.value < node.right.value and valid_left_tree and valid_right_tree:
        return True
    else:
        return False
        

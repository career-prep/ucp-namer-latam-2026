# Technique: Depth-first traversal (Post-order)
# Time Complexity: O(n)
# Space Complexity: O(h)

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def deepcopy(node):
    if node is None:
        return None

    new_node = Node(node.data)
    new_node.left = deepcopy(node.left)
    new_node.right = deepcopy(node.right)

    return new_node

# Time Taken: 7mins 39secs

# Test Cases
t1 = Node(1)
t1.left = Node(2)
t1.right = Node(3)
t1.left.left = Node(4)
t1.left.right = Node(5)

copy1 = deepcopy(t1)
print(copy1.data, copy1.left.data, copy1.right.data)

# Edge cases
t2 = None
print(deepcopy(t2))
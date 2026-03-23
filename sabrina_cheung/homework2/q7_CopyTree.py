'''
Method: DFS
Time: 10 mins
Time Complexity: O(n)
Space Complexity: O(h)

Intuition: 

Given Tree:
            5
        /       \
        3       7
            /       \
            6       10

Copy: 5 -->     5       -->     5        -->         5
                    \       /       \           /           \
                    7       3       7           3            7
                                            /       \      /    \
                                            None    None    6   10
                                                        /   \   /   \
                                                        None None None None

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def CopyTree(root):
    if not root:
        return None
    new = Node(root.data)
    new.right = CopyTree(new.right)
    new.left = CopyTree(new.left)
    return new
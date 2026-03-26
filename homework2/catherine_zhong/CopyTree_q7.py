#technique: dfs
#time complexity: O(n)
#space complexity: O(n)

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right 

def copyTree(root):
    nodes = {}

    def dfs(node):
        if not node:
            return None

        if node in nodes:
            return nodes[node]

        copy = Node(node.val)
        nodes[node] = copy
        copy.left = dfs(node.left)
        copy.right = dfs(node.right)

        return copy

    return dfs(root)

def printTree(root, level=0):
    if root is None:
        print("     " * level + "- " + str(None))
        return

    printTree(root.right, level + 1)
    print("     " * level + "- " + str(root.val))
    printTree(root.left, level + 1)



print('base case: root node is None')
root = None
printTree(copyTree(root))

print('\nbasic tree test: ')
LLchild = Node(4, None, None)
LRchild = Node(5, None, None)
RLchild = Node(6, None, None)
RRchild = Node(7, None, None)
Lchild = Node(2, LLchild, LRchild)
Rchild = Node(3, RLchild, RRchild)
root = Node(1, Lchild, Rchild)
printTree(copyTree(root))

print('\nonly left nodes: ')
LLchild = Node(4, None, None)
Lchild = Node(2, LLchild, None)
root = Node(1, Lchild, None)
printTree(copyTree(root))


print('\nonly right nodes: ')
RRchild = Node(7, None, None)
Rchild = Node(3, None, RRchild)
root = Node(1, None, Rchild)
printTree(copyTree(root))


#time spent: 30 min
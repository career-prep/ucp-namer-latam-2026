#technique: dfs
#time complexity: O(n)
#space complexity: O(1)
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right 

def IsBST(root):
    if root is None:
        return True

    def dfs(node, minval, maxval):
        if node is None:
            return True 

        if not (minval < node.val < maxval):
            return False

        return dfs(node.left, minval, node.val) and dfs(node.right, node.val, maxval)

    return dfs(root, float('-inf'), float('inf'))

def printTree(root, level=0):
    if root is None:
        print("     " * level + "- " + str(None))
        return

    printTree(root.right, level + 1)
    print("     " * level + "- " + str(root.val))
    printTree(root.left, level + 1)



print('base case: root node is None')
root = None
print(IsBST(root))

print('\nbasic tree test: ')
LLchild = Node(4, None, None)
LRchild = Node(5, None, None)
RLchild = Node(6, None, None)
RRchild = Node(7, None, None)
Lchild = Node(2, LLchild, LRchild)
Rchild = Node(3, RLchild, RRchild)
root = Node(1, Lchild, Rchild)
print(IsBST(root))

print('\nbasic BST test: ')
LLchild = Node(1, None, None)
LRchild = Node(3, None, None)
RLchild = Node(5, None, None)
RRchild = Node(7, None, None)
Lchild = Node(2, LLchild, LRchild)
Rchild = Node(6, RLchild, RRchild)
root = Node(4, Lchild, Rchild)
print(IsBST(root))

#time spent: 20 min
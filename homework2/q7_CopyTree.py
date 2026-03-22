# Tree Traversal: Depth-first traversal: Pre-Order Traversal.
# O(n) Time complexity. We visit all nodes once.
# O(n) Space Complexity. A deep copy of 'n' nodes is made. (Recursion stack is O(h), h being height of tree. Skewed: O(n), Balanced: O(logn))
# Given a binary tree, create a deep copy. Return the root of the new tree.

# Binary Tree class
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Test Cases

# 1: Empty Tree
root1 = None

# 2: Tree with 1 node
root2 = Node(5)

# 3: Unbalanced Tree
root3 = Node(1)
root3.left = Node(2)
root3.left.right = Node(3)

# 4: Balanced BST
root4 = Node(6)
root4.left = Node(5)
root4.right = Node(7)
root4.left.left = Node(4)
root4.right.right = Node(8)


# Deep Copy Function, returns a different root
def copyTree(root):

    if root == None:
        return None
    
    # Create a new root using the data of the given root
    copyRoot = Node(root.data)

    # Use recursion to fill in the left and right children
    copyRoot.left = copyTree(root.left)

    copyRoot.right = copyTree(root.right)


    return copyRoot


# 15 Minutes 



# Testing the Test Cases

res1 = copyTree(root1)
res2 = copyTree(root2)
res3 = copyTree(root3)
res4 = copyTree(root4)

print("Test Case 1:")
print(res1)
print(res1 == root1) # In this case its true because None == None
print()

print("Test Case 2:")
print(f"res2 data is {res2.data}, root2 data is {root2.data}")
print(f"Does res2 and root2 have the same reference? {res2==root2}")
print()

print("Test Case 3:")
print(f"res3 data is {res3.data}, root3 data is {root3.data}")
print(f"Does res3 and root3 have the same reference? {res3==root3}")
print(f"res3.left data is {res3.left.data}, root3.left data is {root3.left.data}")
print(f"Does res3.left and root3.left have the same reference? {res3.left==root3.left}")
print(f"res3.left.right data is {res3.left.right.data}, root3 data is {root3.left.right.data}")
print(f"Does res3.left.right and root3.left.right have the same reference? {res3.left.right==root3.left.right}")
print()

print("Test Case 4:")
print(f"res4 data is {res4.data}, root4 data is {root4.data}")
print(f"Does res4 and root4 have the same reference? {res4==root4}")
print(f"res4.left data is {res4.left.data}, root4.left data is {root4.left.data}")
print(f"Does res4.left and root4.left have the same reference? {res4.left==root4.left}")
print(f"res4.left.left data is {res4.left.left.data}, root4.left.left data is {root4.left.left.data}")
print(f"Does res4.left.left and root4.left.left have the same reference? {res4.left.left==root4.left.left}")
print(f"res4.right data is {res4.right.data}, root4.right data is {root4.right.data}")
print(f"Does res4.right and root4.right have the same reference? {res4.right==root4.right}")
print(f"res4.right.right data is {res4.right.right.data}, root4.right.right data is {root4.right.right.data}")
print(f"Does res4.right.right and root4.right.right have the same reference? {res4.right.right==root4.right.right}")
print()



# Additional Test
print("Additional Test of Proof of Deep copy:")
print(f"Before modification, res2.data is {res2.data}, and root2.data is {root2.data}")
res2.data = 100
print(f"Now, after chaning res2.data to 100, res2.data is {res2.data}, while root2.data remains to be {root2.data}")
print()

print("Deep Copy Test on Larger Tree:")
print(f"Before: res4.left.data = {res4.left.data}, root4.left.data = {root4.left.data}")
res4.left.data = 44
print(f"After: res4.left.data = {res4.left.data}, root4.left.data = {root4.left.data}")




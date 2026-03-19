# Question 3: Binary Search Tree

# Implement a BST class with min, max, contains, insert, and delete operations.
# The Node struct has left and right references (no duplicates allowed).

# Examples:

# insert(5), insert(3), insert(7), insert(1), insert(4) -> BST
# min() -> 1
# max() -> 7
# contains(3) -> True
# contains(6) -> False
# delete(3) -> removes 3, restructures BST
# contains(3) -> False


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def min(self):
        # Walk all the way left
        if not self.root:
            return None
        cur = self.root
        while cur.left:
            cur = cur.left
        return cur.data
    # Time Complexity = O(log n), Space Complexity = O(1)

    def max(self):
        # Walk all the way right
        if not self.root:
            return None
        cur = self.root
        while cur.right:
            cur = cur.right
        return cur.data
    # Time Complexity = O(log n), Space Complexity = O(1)

    def contains(self, val):
        cur = self.root
        while cur:
            if val == cur.data:
                return True
            elif val < cur.data:
                cur = cur.left
            else:
                cur = cur.right
        return False
    # Time Complexity = O(log n), Space Complexity = O(1)

    def insert(self, val):
        new_node = Node(val)
        if not self.root:
            self.root = new_node
            return
        cur = self.root
        while True:
            if val == cur.data:
                return  # no duplicates
            elif val < cur.data:
                if not cur.left:
                    cur.left = new_node
                    return
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = new_node
                    return
                cur = cur.right
    # Time Complexity = O(log n), Space Complexity = O(1)

    def delete(self, val):
        self.root = self._delete_helper(self.root, val)
    # Time Complexity = O(log n), Space Complexity = O(log n) call stack

    def _delete_helper(self, node, val):
        if not node:
            return None
        if val < node.data:
            node.left = self._delete_helper(node.left, val)
        elif val > node.data:
            node.right = self._delete_helper(node.right, val)
        else:
            # Node to delete found
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            # Node has two children: replace with in-order successor (min of right subtree)
            successor = node.right
            while successor.left:
                successor = successor.left
            node.data = successor.data
            node.right = self._delete_helper(node.right, successor.data)
        return node

    def inorder(self):
        result = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            result.append(node.data)
            traverse(node.right)
        traverse(self.root)
        return result


# --- Tests ---

bst = BinarySearchTree()
for val in [5, 3, 7, 1, 4, 6, 9]:
    bst.insert(val)

print("Inorder (should be sorted):", bst.inorder())   # [1, 3, 4, 5, 6, 7, 9]
print("min:", bst.min())                               # 1
print("max:", bst.max())                               # 9
print("contains(3):", bst.contains(3))                 # True
print("contains(8):", bst.contains(8))                 # False

bst.insert(5)  # duplicate, no-op
print("Inorder after insert(5) duplicate:", bst.inorder())  # unchanged

bst.delete(3)  # node with two children
print("Inorder after delete(3):", bst.inorder())       # [1, 4, 5, 6, 7, 9]
print("contains(3) after delete:", bst.contains(3))    # False

bst.delete(1)  # leaf node
print("Inorder after delete(1):", bst.inorder())       # [4, 5, 6, 7, 9]

bst.delete(7)  # node with one child
print("Inorder after delete(7):", bst.inorder())       # [4, 5, 6, 9]

# Spent a total of 40 mins on this question

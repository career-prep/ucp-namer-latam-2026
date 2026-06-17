"""
BINARY SEARCH TREE METHODS

min()
    Time: O(log n)
    Space: O(1)

max()
    Time: O(log n)
    Space: O(1)

contains(val)
    Time: O(log n)
    Space: O(1)

insert(val)
    Time: O(log n)
    Space: O(log n) recursion

delete(val)
    Time: O(log n)
    Space: O(log n)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def min(self):
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.data

    def max(self):
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.data

    def contains(self, val):
        curr = self.root

        while curr:
            if val == curr.data:
                return True
            elif val < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        return False

    def insert(self, val):

        def helper(node, val):
            if node is None:
                return Node(val)

            if val < node.data:
                node.left = helper(node.left, val)
            elif val > node.data:
                node.right = helper(node.right, val)

            return node

        self.root = helper(self.root, val)

    def delete(self, val):

        def findMin(node):
            while node.left:
                node = node.left
            return node

        def helper(node, val):
            if node is None:
                return None

            if val < node.data:
                node.left = helper(node.left, val)
            elif val > node.data:
                node.right = helper(node.right, val)
            else:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left

                temp = findMin(node.right)
                node.data = temp.data
                node.right = helper(node.right, temp.data)

            return node

        self.root = helper(self.root, val)

def run_tests():
    bst = BinarySearchTree()

    # Test Insert
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    # Test Contains
    assert bst.contains(50) == True
    assert bst.contains(100) == False
    assert bst.contains(20) == True
    print("insert/contains passed")

    # Test Min/Max
    assert bst.min() == 20
    assert bst.max() == 80
    print("min/max passed")

    # Test Delete Leaf
    bst.delete(20)
    assert bst.contains(20) == False
    assert bst.min() == 30
    print("delete leaf passed")

    # Test Delete Node with one child
    bst.delete(30)
    assert bst.contains(30) == False
    assert bst.contains(40) == True
    print("delete one-child node passed")

    # Test Delete Node with two children
    bst.delete(70)
    assert bst.contains(70) == False
    assert bst.contains(60) == True
    assert bst.contains(80) == True
    print("delete two-child node passed")


run_tests()

# Time spent: 40:00
# Needed help on delete.

# Given a binary tree, create an array of the left view (leftmost elements in each level) of the tree.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # def insert(self, val):
    #     self.root = Node(val)

    # input : binary tree
    # output: array of left view

    # traverse through the entire BT and keep track of level
    
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self):
        self.root = None


    # Returns minimun value in BST. O(logn) time.
    def min(self):

        if self.root == None:
            return None

        root = self.root

        while root.left:
            root = root.left

        return root.data
    

    # Returns the maximum value in the BST. O(logn) time.
    def max(self):

        if self.root == None:
            return None
        
        root = self.root

        while root.right:
            root = root.right

        return root.data
    

    # Returns a boolean indicating whether val is present in the bst. O(logn) time.
    def contains(self, val):

        if self.root == None:
            return False
        
        root = self.root

        while root:

            if root.data == val:
                return True
            elif root.data < val:
                root = root.right
            else:
                # root.data > val
                root = root.left

        return False
    



    # Creates a new node with data val in the appropriate location. No duplicates allowed. O(logn) time
    def insert(self, val):

        if self.contains(val):
            return

        if self.root is None:
            self.root = Node(val)
            return

        def insertHelper(node):

            if val < node.data:
                if node.left is None:
                    node.left = Node(val)
                else:
                    insertHelper(node.left)

            else:  # val > node.data
                if node.right is None:
                    node.right = Node(val)
                else:
                    insertHelper(node.right)

        insertHelper(self.root)





    # Deletes Node with the data 'val', if it exists. O(logn) time.
    def delete(self, val):
        
        # 3 cases. Deleting a leaf, deleting a node with only 1 child, deleting a node with two children

        # Helper function to find a node. O(logn) time.
        def findNode(root, val):
            if root:
                if root.data == val:
                    return root
                elif val < root.data:
                    return findNode(root.left, val)
                else:
                    # val > root.data
                    return findNode(root.right, val)
            else:
                return None
            
        # Helper function to find the parent of a node. O(logn) time.
        def findParent(root, delNode):

            if root == None or root == delNode:
                return None
            
            # Root is direct parent of node
            if root.left == delNode or root.right == delNode:
                return root
            
            # Continue to search for delNode's parent node
            if root.data > delNode.data:
                # Search left
                return findParent(root.left, delNode)
            else:
                # Search right
                return findParent(root.right, delNode)


        delNode = findNode(self.root, val)

        if delNode == None:
            # val is not inside the BST
            return

        parentNode = findParent(self.root, delNode)




        # CASE 1: delNode is a leaf node
        if delNode.left == None and delNode.right == None:

            # delNode is the only node
            if parentNode == None:
                self.root = None
                return
            
            # delNode is a left child leaf node
            if val < parentNode.data:
                parentNode.left = None
                return
            
            # delNode is a right child leaf node
            if val > parentNode.data:
                parentNode.right = None
                return
            
        
        # CASE 2.1: delNode has only a left child
        if delNode.left != None and delNode.right == None:

            # delNode is the root
            if parentNode == None:
                self.root = delNode.left
                delNode.left = None
                return
            
            # delNode is a left child
            if val < parentNode.data:
                parentNode.left = delNode.left
                delNode.left = None
                return
            
            # delNode is a right child
            if val > parentNode.data:
                parentNode.right = delNode.left
                delNode.left = None
                return


        # CASE 2.2: delNode has only a right child
        if delNode.left == None and delNode.right != None:

            # delNode is the root
            if parentNode == None:
                self.root = delNode.right
                delNode.right = None
                return
            
            # delNode is a left child
            if val < parentNode.data:
                parentNode.left = delNode.right
                delNode.right = None
                return
            
            # delNode is a right child
            if val > parentNode.data:
                parentNode.right = delNode.right
                delNode.right = None
                return


        # CASE 3: delNode has two children

        # We can either replace delNode with the largest value from left subtree or smallest from right substree.
        # The current min() function does not find the smallest value in a subtree so I must make a helper function that runs O(logn) time.
        def findMinNode(root): # Returns a node
            if root == None:
                return None
            
            if root.left == None:
                return root
            else:
                return findMinNode(root.left)
            
        
        newDelNode = findMinNode(delNode.right) # We will physically delete the node in this location
        # newDelNode must fall under Case 1 or Case 2

        saveVal = newDelNode.data

        # This recursive call will handle newDelNode as it falls under either case 1 or case 2
        self.delete(saveVal)

        delNode.data = saveVal



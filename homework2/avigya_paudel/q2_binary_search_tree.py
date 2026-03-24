class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self._root = None

    def min(self):
        # returns the minimum value in the BST.  O(logn) time.
        if not self._root: return -1 

        self.runner = self._root 
        while self.runner.left:
            self.runner = self.runner.left

        return self.runner.data

    def max(self):
        # returns the maximum value in the BST.  O(logn) time.
        if not self._root: return -1 

        self.runner = self._root 
        while self.runner.right:
            self.runner = self.runner.right

        return self.runner.data

    def contains(self, val):
        # returns a boolean indicating whether val is present in the BST.  O(logn) time.
        if not self._root: return False

        self.runner = self._root

        while self.runner:
            if self.runner == None:
                return False
            if self.runner.data == val:
                return True 
            
            if self.runner.data > val:
                self.runner = self.runner.left
            else:
                self.runner = self.runner.right
        return False

    def insert(self, val):
        # creates a new Node with data val in the appropriate location.   
        # For simplicity, do not allow duplicates. If val is already 
        # present, insert is a no-op. O(logn) time.
        
        def insert_helper(node, val):
            node_val = node.data
            if node.left == None and node.right == None:
                if node_val > val:
                    node.left = Node(val)
                else:
                    node.right = Node(val)
            elif node.right == None:
                if node_val < val:
                    node.right = Node(val)
                else:
                    return insert_helper(node.left, val)
            elif node.left == None:
                if node_val > val:
                    node.left = Node(val)
                else:
                    return insert_helper(node.right, val)
            else:
                if node.data > val:
                    return insert_helper(node.left, val)
                else:
                    return insert_helper(node.right, val)
        
        if not self._root:
            self._root = Node(val)
        else:
            insert_helper(self._root, val)
                
    def delete(self, val):
        #  deletes the Node with data val, if it exists. O(logn) time.
        def delete_helper(node, val):
            if node.data > val:
                node.left = delete_helper(node.left, val)
            elif node.data < val:
                node.right = delete_helper(node.right, val)
            else:
                if not node.left and not node.right:
                    return None
                elif not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    min_val = find_min(node.right)
                    node.data = min_val
                    node.right = delete_helper(node.right, min_val)
            return node

        def find_min(node):
            while node.left:
                node = node.left
            return node.data

        self._root = delete_helper(self._root, val)

if __name__ == "__main__":
    bst = BinarySearchTree()

    # Insert values to build a tree:
    #        10
    #       /  \
    #      5    15
    #     / \     \
    #    3   7    20
    for val in [10, 5, 15, 3, 7, 20]:
        bst.insert(val)

    print("Min:", bst.min())           # expected: 3
    print("Max:", bst.max())           # expected: 20
    print("Contains 7:", bst.contains(7))   # expected: True
    print("Contains 9:", bst.contains(9))   # expected: False

    bst.delete(5)

    print("Contains 5 after delete:", bst.contains(5))  # expected: False
    print("Contains 7 after delete 5:", bst.contains(7))  # expected: True

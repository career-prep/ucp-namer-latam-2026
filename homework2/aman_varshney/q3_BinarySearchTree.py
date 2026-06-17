# spent 40 minutes

class Node:
    """Node struct in python"""
    def __init__(self, data: int, left: Node = None, right: Node = None) -> None:
        self.data = data
        self.left = left 
        self.right = right
        
        
class BinarySearchTree:
    def __init__(self, root) -> None:
        self.root = root
        
        
    def min(self):
        """Returns the min value in tree. O(h)"""
        if not self.root: # empty case
            return None
        
        curr = self.root
        while curr.left:
            curr = curr.left       
        return curr.data
    
    
    def max(self):
        """Returns the max value in tree. O(h)"""
        if not self.root: # empty case
            return None
        
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.data
    
    
    def contains(self, val):
        """Searches for a node with data `val` and returns true if found. O(h)"""
        if not self.root: # empty case
            return False
        
        curr = self.root
        
        # helper
        def finder(node, val):
            if not node: # empty case
                return False
            if node.data > val: 
                return finder(node.left, val)
            elif node.data < val:
                return finder(node.right, val) 
            else:
                return True
            
        return finder(curr, val)
    
    
    def insert(self, val):
        """Creates a new node with data `val` and inserts it into the tree. If a node with `val`
        is already in the tree, no-op. O(h)"""
        if not self.root:
            self.root = Node(val, None, None)
            return
            
        curr = self.root
            
        # helper
        def helper(node, val):
            if node.data > val:
                if not node.left: # min value
                    node.left = Node(val, None, None)
                else:
                    helper(node.left, val)
            elif node.data < val:
                if not node.right: # max value
                    node.right = Node(val, None, None)
                else:
                    helper(node.right, val)
            else: # no op
                return
            
        helper(curr, val)
        
        
    def delete(self, val):
        """Deletes the node with data `val` if it exists. O(h)"""
        curr = self.root
        
        # helper
        def helper(node, val):
            if not node: # empty case
                return None
            
            if node.data > val:
                node.left = helper(node.left, val) 
            elif node.data < val:
                node.right = helper(node.right, val)
            else: # node found
                # no children case
                if not node.left and not node.right:
                    return None
                
                # one child
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                
                # two children
                # find min in right subtree
                min_in_right = node.right
                while min_in_right.left:
                    min_in_right = min_in_right.left
                # 
                node.data = min_in_right.data
                node.right = helper(node.right, min_in_right.data)
            
            return node
        
        self.root = helper(curr, val)


if __name__ == "__main__":
    # helper for inorder traversal
    def inorder_values(node, acc):
        if not node:
            return
        inorder_values(node.left, acc)
        acc.append(node.data)
        inorder_values(node.right, acc)


    # 1
    # test min, max, contains on empty tree
    empty = BinarySearchTree(None)
    assert empty.min() is None, "empty min error"
    assert empty.max() is None, "empty max error"
    assert empty.contains(1) is False, "empty contains error"


    # 2
    # test insert into empty tree; min, max, contains on single node
    bst = BinarySearchTree(None)
    bst.insert(42)
    assert bst.min() == 42, "single min error"
    assert bst.max() == 42, "single max error"
    assert bst.contains(42) is True, "single contains error"
    acc2 = []
    inorder_values(bst.root, acc2)
    assert acc2 == [42], "single inorder error"


    # 3
    # test insert duplicate is no-op when tree is only root
    dup_root = BinarySearchTree(None)
    dup_root.insert(5)
    dup_root.insert(5)
    assert dup_root.min() == 5, "dup root min error"
    assert dup_root.max() == 5, "dup root max error"
    assert dup_root.contains(5) is True, "dup root contains error"
    acc3 = []
    inorder_values(dup_root.root, acc3)
    assert acc3 == [5], "dup root inorder error"


    # 4
    # test min/max after building a tree
    bst2 = BinarySearchTree(None)
    for v in [10, 5, 15, 3, 7, 12, 18]:
        bst2.insert(v)
    assert bst2.min() == 3, "min error"
    assert bst2.max() == 18, "max error"


    # 5
    # test contains
    assert bst2.contains(7) is True, "contains true error"
    assert bst2.contains(12) is True, "contains true2 error"
    assert bst2.contains(99) is False, "contains false error"


    # 6
    # test insert duplicate is no-op (value already in larger tree)
    bst2.insert(7)
    acc6 = []
    inorder_values(bst2.root, acc6)
    assert acc6 == [3, 5, 7, 10, 12, 15, 18], "duplicate insert error"


    # 7
    # test delete leaf
    bst2.delete(3)
    acc7 = []
    inorder_values(bst2.root, acc7)
    assert acc7 == [5, 7, 10, 12, 15, 18], "delete leaf error"
    assert bst2.contains(3) is False, "delete leaf contains error"


    # 8
    # test delete node with one child
    bst3 = BinarySearchTree(None)
    bst3.insert(10)
    bst3.insert(5)
    bst3.insert(3)
    bst3.delete(5)
    acc8 = []
    inorder_values(bst3.root, acc8)
    assert acc8 == [3, 10], "delete one child error"


    # 9
    # test delete node with two children (root)
    bst4 = BinarySearchTree(None)
    for v in [10, 5, 15, 3, 7, 12, 20]:
        bst4.insert(v)
    bst4.delete(10)
    acc9 = []
    inorder_values(bst4.root, acc9)
    assert acc9 == [3, 5, 7, 12, 15, 20], "delete two children error"
    assert bst4.contains(10) is False, "delete root contains error"


    # 10
    # test delete on missing value leaves tree unchanged
    bst4.delete(999)
    acc10 = []
    inorder_values(bst4.root, acc10)
    assert acc10 == [3, 5, 7, 12, 15, 20], "delete missing error"


    print("All tests passed")

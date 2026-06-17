class Node:
    def __init__(self,value):
        self.value = value
        self.left =  None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def min(self): # O(logn) time, O(1) space
        cur = self.root

        if cur is None:
            return None

        while cur.left:
            cur = cur.left

        return cur.value    

    def max(self): # O(logn) time, O(1) space
        cur = self.root

        if cur is None:
            return None
        while cur.right:
            cur = cur.right

        return cur.value

    def contains(self, target): # O(logn) time, O(1) sapce
        cur = self.root
        if cur is None:
            return False
        
        while cur:

            if cur is None:
                return False
            
            elif target > cur:
                cur = cur.right

            elif target < cur:
                cur = cur.left

            else:
                return True
        return False

    def insert(self, val): # O(logn) time, O(1) space
        newNode = Node(val)
        cur =  self.root

        if cur is None:
            self.root = newNode
            return 

        while cur:
            if val < cur.value:
                if cur.left is None:
                    cur.left = newNode
                    return
                cur = cur.left
            elif val > cur.value:
                if cur.right is None:
                    cur.right = newNode
                    return
                cur = cur.right
            else:
                return # if they are equal do nothing

    
    def remove(self,val): # O(logn) time,  O(1) space
        cur = self.root
        if cur is None:
            return

        while cur:
            if val < cur.value:
                if cur.left.value == val:
                    grandchild = cur.left
                    cur.left = grandchild.left
                    cur.right = grandchild.right
                    return
                cur = cur.left
            elif val > cur.value:
                if cur.right.value == val:
                    grandchild = cur.right
                    cur.left = grandchild.left
                    cur.right = grandchild.right
                    return
                cur = cur.right

        return

# This took me 40 minutes and still has some bugs that need fixing. Especially with remove().


def main():
    bst = BinarySearchTree()

    # Test insert
    for v in [5, 3, 7, 1, 4, 6, 8]:
        bst.insert(v)
    #       5
    #      / \
    #     3   7
    #    / \ / \
    #   1  4 6  8

    print("Min:     ", bst.min())       # expect 1
    print("Max:     ", bst.max())       # expect 8
    print("Contains 4:", bst.contains(4))  # expect True
    print("Contains 9:", bst.contains(9))  # expect False

    bst.remove(1)
    print("After remove 1, min:", bst.min())  # expect 3

    bst.remove(7)
    print("After remove 7, max:", bst.max())  # expect 8

if __name__ == "__main__":
    main()


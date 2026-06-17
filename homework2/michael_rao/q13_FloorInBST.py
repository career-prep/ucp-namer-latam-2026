class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def floorInBST(root, target):
    floor_val = None
    curr = root
    while curr != None:
        if curr.val == target:
            return curr.val
        if curr.val < target:
            floor_val = curr.val
            curr = curr.right
        else:
            curr = curr.left
    return floor_val
# time: O(h)

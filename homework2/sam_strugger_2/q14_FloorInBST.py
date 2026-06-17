class TreeNode:
    def __init__(self,value):
        self.right = None
        self.left = None
        self.value = value


def floorInBST(root, target): # O(logn) time, O(1) space

    cur = root
    greatest = -1

    while cur:
        current_value = cur.value
        if greatest < current_value < target:
            greatest = current_value

        if current_value == target:
            return current_value

        elif current_value < target:
            cur = cur.right

        else:
            cur = cur.left

        
    return greatest

# This took me 25 minutes to complete 
def main():
    #       5
    #      / \
    #     3   7
    #    / \ / \
    #   1  4 6  8
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)


    print("floor(5):", floorInBST(root, 5))  # expect 5

    print("floor(6.5):", floorInBST(root, 6.5))  # expect 6

    print("floor(10):", floorInBST(root, 10))  # expect 8

    print("floor(2):", floorInBST(root, 2))  # expect 1

    print("floor(0):", floorInBST(root, 0))  # expect -1


    print("floor(4):", floorInBST(root, 4))  # expect 4

if __name__ == "__main__":
    main()


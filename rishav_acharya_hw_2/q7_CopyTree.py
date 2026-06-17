# 29 minutes
# Generic tree traversal technique
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def copyTree(root):
    if root is None:
        return None

    newroot = Node(root.data)

    newroot.left = copyTree(root.left)
    newroot.right = copyTree(root.right)

    return newroot

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    copied = copyTree(root)
    print(root is copied)
    print(root.left is copied.left)
    print(root.data, copied.data)

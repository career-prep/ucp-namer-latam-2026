class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def minValue(root):
    if not root:
        return None

    curr = root
    while curr.left:
        curr = curr.left

    return curr.data


def maxValue(root):
    if not root:
        return None

    curr = root
    while curr.right:
        curr = curr.right

    return curr.data


def contains(root, val):
    curr = root

    while curr:
        if val == curr.data:
            return True
        elif val < curr.data:
            curr = curr.left
        else:
            curr = curr.right

    return False


def insert(root, val):
    if not root:
        return Node(val)

    if val < root.data:
        root.left = insert(root.left, val)
    elif val > root.data:
        root.right = insert(root.right, val)

    return root


def delete(root, val):
    if not root:
        return None

    if val < root.data:
        root.left = delete(root.left, val)
    elif val > root.data:
        root.right = delete(root.right, val)
    else:
        if not root.left and not root.right:
            return None

        if not root.left:
            return root.right

        if not root.right:
            return root.left

        successor = root.right
        while successor.left:
            successor = successor.left

        root.data = successor.data
        root.right = delete(root.right, successor.data)

    return root
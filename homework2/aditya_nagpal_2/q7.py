def deep_copy(root):
    if root is None:
        return None

    new_node = Node(root.data)
    new_node.left = deep_copy(root.left)
    new_node.right = deep_copy(root.right)

    return new_node



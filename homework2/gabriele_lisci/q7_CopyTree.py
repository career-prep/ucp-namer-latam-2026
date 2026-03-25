# Runtime: O(n)
# Space complexity: O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def deepCopyTree(root):
    if root is None:
        return None
    newNode = Node(root.data)

    newNode.left = deepCopyTree(root.left)
    newNode.right = deepCopyTree(root.right)

    return newNode

def isDeepCopy(original, copy):
    if not original and not copy:
        return True
    if not original or not copy:
        return False

    return (original.data == copy.data and
            original is not copy and
            isDeepCopy(original.left, copy.left) and
            isDeepCopy(original.right, copy.right))

def run_tests():
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    copy1 = deepCopyTree(root1)
    assert isDeepCopy(root1, copy1) == True
    print("Standard tree test passed")

    # 2. Test Single Node
    root2 = Node(10)
    copy2 = deepCopyTree(root2)
    assert isDeepCopy(root2, copy2) == True
    assert root2 is not copy2
    print("Single node test passed")

    # 3. Test Empty Tree
    assert deepCopyTree(None) is None
    print("Empty tree test passed")

    # 4. Test Unbalanced (Left-skewed) Tree
    root4 = Node(5)
    root4.left = Node(4)
    root4.left.left = Node(3)
    copy4 = deepCopyTree(root4)
    assert isDeepCopy(root4, copy4) == True
    print("Unbalanced tree test passed")

if __name__ == "__main__":
    run_tests()

# Time spent: 35:15

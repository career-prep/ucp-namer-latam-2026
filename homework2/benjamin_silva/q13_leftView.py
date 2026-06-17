# Technique: BFS
# Time Complexity: O(n)
# Space Complexity: O(w) width of the tree
# Time spent: 40 minutes
 
from q3_binarySearchTree import Node
 
 
def left_view(root):
    if not root:
        return []
    
    result = []
    queue = [root]

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.pop(0)

            if i == 0:
                result.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result
    
 
 
def build_tree(val, left=None, right=None):
    node = Node(val)
    node.left = left
    node.right = right
    return node
 
tree1 = build_tree(7, build_tree(8), build_tree(3, build_tree(9, build_tree(20), build_tree(14, None, build_tree(15))), build_tree(13)))
print(left_view(tree1))  # expected [7, 8, 9, 20, 15]
 
tree2 = build_tree(7, build_tree(20, build_tree(15), build_tree(6)), build_tree(4, build_tree(8), build_tree(11)))
print(left_view(tree2))  # expected [7, 20, 15]
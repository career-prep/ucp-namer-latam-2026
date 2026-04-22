from collections import deque

class TreeNode:
    def __init__(self,value):
        self.right = None
        self.left = None
        self.value = value
#   5
#  3  7
# 1 4   8


def leftView(root): # I'm pretty sure this is still O(n) time complexity 
                    # even though my solution is a bit convoluted. Space is O(n).
    queue = deque()
    ans = []

    if root:
        queue.append(root)

    while len(queue) > 0:
        to_add = []

        for i in range(len(queue)):
            cur = queue.popleft()
            to_add.append(cur.value)

            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

        ans.append(to_add)

    ans2 = []
    for j in ans:
        ans2.append(j[0])

    return ans2

# 

def main():
    #       5
    #      / \
    #     3   7
    #    / \    \
    #   1   4    8
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(8)
    print("Left view:", leftView(root))  # expect [5, 3, 1]

    root = TreeNode(1)
    print("Single:   ", leftView(root))  # expect [1]


    print("Empty:    ", leftView(None))  # expect []

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    print("Left skew:", leftView(root))  # expect [1, 2, 3]

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    print("Right skew:", leftView(root))  # expect [1, 2, 3]

if __name__ == "__main__":
    main()

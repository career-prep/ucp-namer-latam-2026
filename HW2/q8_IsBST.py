#Run time: O(n)
#Space: O(h), h=height of the tree

"""
Question:
    Given a binary tree, determine if it is a BST

IDEAS:
    + Binary tree: at most 2 child, left child < parent and right child> parent. NO NODE WITH SAME VALUE

    edge case 6>5 but 6 in left subtree.
         5
        / \
       4   8
      / \
     3   6

    use Depth First and Pre Order Traversal, recursion.
    we will use helper to track the node, the min possible value of that node and max possible value of that node in order to handle the edge case above
    in the root, there would be no limit => the min_val =float('-inf'), max_val=float('inf')
    we keep traverse and check if it fails any requirement of the bst above:
        when traverse to the left, we only have max limit
        when traverse to the right, we only have min limit 


"""

class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right


def is_bst_helper(node, min_val, max_val):
    #base case
    if node ==None:
        return True
    
    if node.data<=min_val or node.data>=max_val:
        return False
    
    left_check= is_bst_helper(node.left,min_val,node.data)
    right_check=is_bst_helper(node.right,node.data, max_val)

    return left_check and right_check

def is_bst(root):
    return is_bst_helper(root, float('-inf'), float('inf'))



def test1(): #empty bst
    node=None
    assert is_bst(node) == True


def test2(): #valid bst
    node1=Node(3)
    node2=Node(9)
    node3=Node(10,node2)
    node4=Node(8,node1,node3)

    assert is_bst(node4)==True

def test3(): #invalid bst
    node1=Node(3)
    node2=Node(7)
    node3=Node(10,node2)
    node4=Node(8,node1,node3)

    assert is_bst(node4)==False

if __name__ == "__main__":
    test1()
    test2()
    test3()
    print("all passed")







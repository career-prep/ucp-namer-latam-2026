# Run time: O(n) due to visiting all node and copy
# Space: O(h) since recurion use call stack => Worst case: O(n) if all node is always go to right or left side
#Technique: Deft first Pre-order traversal 


"""
Question:
given a binary tree, create a copy and return root of new tree
binary tree: have max of 2 children


ideas:
   using recursion to traverse through every node of the tree and copy:
    base case: if node =None => return None
    traverse all the way to left, then all the way to right => Pre-order traverse
"""

class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    
    

def copy_bt(root):
    curr=root

    if curr ==None:
        return None
    
    copy_node= Node(curr.data)
    copy_node.left=copy_bt(curr.left)
    copy_node.right=copy_bt(curr.right)

    return copy_node



#TEST CASE
def test1():

    node1= Node(1)
    node2= Node(2)
    node3=Node(3,node1,node2)
    node4=Node(4,node3)

    copy_root=copy_bt(node4)
    assert copy_root is not None
    assert copy_root.data==node4.data

    assert copy_root.left is not None
    assert copy_root.left.data==node3.data

    assert copy_root.right is None

    assert copy_root.left.left is not None
    assert copy_root.left.left.data==node1.data

    assert copy_root.left.right is not None
    assert copy_root.left.right.data==node2.data


def test2(): #None

    node= None
    copy_root=copy_bt(node)

    assert copy_root is None


def test3():
    node1= Node(1)
    node2= Node(2)
    node3=Node(3,node1,node2)
    node5=Node(5)
    node4=Node(4,node3,node5)
    

    copy_root=copy_bt(node4)
    assert copy_root is not None
    assert copy_root.data==node4.data

    assert copy_root.left is not None
    assert copy_root.left.data==node3.data

    assert copy_root.left.left is not None
    assert copy_root.left.left.data==node1.data

    assert copy_root.left.right is not None
    assert copy_root.left.right.data==node2.data

    assert copy_root.right is not None
    assert copy_root.right.data==node5.data

if __name__ == "__main__":
    test1()
    test2()
    test3()
    print("ALL PASSED!!!")








    


        

        
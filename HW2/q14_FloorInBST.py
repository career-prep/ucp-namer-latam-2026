#Run time: O(h) with h= height
#Space: O(1)
#Technique: Search Binary Tree

"""
question:
given an num and a bst, return the greatest elem that >=num in BST

travere in the tree:
    if node.val= target => return 
    if node.val>target => move left
    if node.val<target, track the max possible value and move to right to find a bigger possible sol

"""
class Node: 
    def __init__(self, data=None,left=None,right=None): 
        self.data=data 
        self.left=left
        self.right=right

def floor_in_bst(head,target):
    if head ==None:
        return head
    
    max_valid_result= float("-inf")
    curr=head

    while curr:
        if curr.data==target:
            return curr.data
        elif target<curr.data:
            curr=curr.left
        else:
            max_valid_result=max(max_valid_result, curr.data)
            curr=curr.right
    
    return max_valid_result


def test1():

    node1= Node(1)
    node2= Node(2)
    node3=Node(3,node1,node2)
    node5=Node(5)
    node4=Node(4,node3,node5)

    assert floor_in_bst(node4,10) == node5.data
    assert floor_in_bst(node4,4) == node4.data


if __name__=="__main__":
    test1()
    print("passed all")

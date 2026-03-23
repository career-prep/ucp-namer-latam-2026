#Run time: O(n)
#Space: O(1)
#Technique: reset/catch up 2 ptr 


"""
Question;
    given a sorted linked list, remove duplicate

    ideas:
        + use 2 ptr
        + we use slow pointer to track the current node, fast to track the next valid node
        + if the next node is dup, we move the right ptr to the next unique node
"""
class Node:
    def __init__(self, data=None,next=None):
        self.data=data
        self.next=next


# fast slow 2 ptr
def dedup_sorted_ll(head):
    if head==None:
        return None
    
    slow=head
    fast=head.next

    while fast:
        if slow.data==fast.data:
            fast=fast.next
        else:
            slow.next=fast
            slow=fast
            fast=fast.next

    slow.next=None #handle the case when there is duplicate at the end, the slow.next point to None (since it is the last node)
    
    return head


# one ptr
"""
idea: 
traverse, check the condition:
    if there is no duplicate, keep moving the ptr => curr=curr.next
    if there is a dup, move the curr.next to the curr.next.next position in order to find the next valid node for curr

"""
def dedup_sorted_ll_optimized(head):
    curr=head
    while curr and curr.next:
        if curr.data==curr.next.data:
            curr.next=curr.next.next
        else:
            curr=curr.next
    return head



def test1():
    node1=Node(10)
    node2=Node(10,node1)
    node3=Node(5,node2)
    node4=Node(4,node3)
    node5=Node(4,node4)

    new_head=dedup_sorted_ll(node5)

    assert new_head is not None
    assert new_head.data== node5.data

    assert new_head.next is not None
    assert new_head.next.data== node3.data

    assert new_head.next.next is not None
    assert new_head.next.next.data== node2.data

    assert new_head.next.next.next is None



def test2():
    node1=Node(8)
    node2=Node(8,node1)
    node3=Node(8,node2)

    new_head=dedup_sorted_ll(node3)

    assert new_head is not None
    assert new_head.data== node3.data

    assert new_head.next is None


def test1_1():
    node1=Node(10)
    node2=Node(10,node1)
    node3=Node(5,node2)
    node4=Node(4,node3)
    node5=Node(4,node4)

    new_head=dedup_sorted_ll_optimized(node5)

    assert new_head is not None
    assert new_head.data== node5.data

    assert new_head.next is not None
    assert new_head.next.data== node3.data

    assert new_head.next.next is not None
    assert new_head.next.next.data== node2.data

    assert new_head.next.next.next is None



def test2_1():
    node1=Node(8)
    node2=Node(8,node1)
    node3=Node(8,node2)

    new_head=dedup_sorted_ll_optimized(node3)

    assert new_head is not None
    assert new_head.data== node3.data

    assert new_head.next is None

if __name__ == "__main__":
    test1()
    test2()
    test1_1()
    test2_1()
    print("all passed")






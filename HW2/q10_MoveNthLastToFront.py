#Run time: O(N)
#Space: O(1)
#Technique: fixed distance 2 ptr


"""
Question:
    have a singly linkedlist, move nth node from back to front

IDEAS:
    #use fixed distance 2 ptr technique
    we create a dummy node and point the slow ptr to it
    fast will be place at node kth from the start (make sure to handle the case when k=length of ll => return head )
    
    we gonna slide the window until reach the end, we will see that :
        slow ptr will be at the prev node of the updated node
        fast ptr will be at the None 
    
    since slow at the prev node of updated node, we update the ptr of that node to skip the updated node. and the updated node will point to head 
    

"""
class Node: 
    def __init__(self, data=None,next=None): 
        self.data=data 
        self.next=next 
    
    
def move_nth_last_to_front(head,k): 
    if head==None or k<=0: 
        return head 

    dummy=Node(None,head) 

    slow=dummy 
    fast=head 

    for i in range(k): 
        if fast==None: 
            return head 
        fast=fast.next 

    #handle the case when k=length of ll
    if fast==None:
        return head

    while fast: #idk why we need to include slow, but if we dont, there is gonna be an error 
        slow=slow.next 
        fast=fast.next 
    
        
    nth_node=slow.next
    slow.next=nth_node.next
    nth_node.next=head
    dummy.next=nth_node

    return dummy.next


def test1():
    node1=Node(19)
    node2=Node(6,node1)
    node3=Node(11,node2)
    node4=Node(9,node3)

    new_head=move_nth_last_to_front(node4,2)

    assert new_head.data == node2.data
    assert new_head.next.data == node4.data
    assert new_head.next.next.data == node3.data
    assert new_head.next.next.next.data == node1.data

def test2():
    node1=Node(19)
    node2=Node(6,node1)
    node3=Node(11,node2)
    node4=Node(9,node3)

    new_head=move_nth_last_to_front(node4,4)

    assert new_head.data == node4.data
    assert new_head.next.data == node3.data
    assert new_head.next.next.data == node2.data
    assert new_head.next.next.next.data == node1.data


if __name__=="__main__":
    test1()
    test2()
    print("passed all")



    
    





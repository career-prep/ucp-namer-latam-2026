#Run time: O(N)
#Space: O(n)
#Technique: Hash Linkedlist node

"""
question: disconnect the cycle if exist

ideas:
    use set to check if the node apprear before or not:
        if not, keep looping until end
        else: set the next ptr of node to None
"""
class Node: 
    def __init__(self, data=None,next=None): 
        self.data=data 
        self.next=next 
        
def disconnect_cycle(head):
    if head==None:
        return head

    seen=set()
    curr=head
    while curr:
        if curr.next in seen:
            curr.next=None
            return head
        else:
            seen.add(curr)
            curr=curr.next
    
    return head


def test1():
    node1=Node(4)
    node2=Node(11,node1)
    node3=Node(9,node2)
    node4=Node(12,node3)
    node1.next=node3

    new_head=disconnect_cycle(node4)

    assert new_head.data == node4.data
    assert new_head.next.data == node3.data
    assert new_head.next.next.data == node2.data
    assert new_head.next.next.next.data == node1.data
    assert new_head.next.next.next.next == None



if __name__=="__main__":
    test1()
    print("passed all")




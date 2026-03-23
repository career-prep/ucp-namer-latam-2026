#Run time: O(N)
#Space: O(1)
#Technique: Doubly Linkedlist forward backward 2 ptr

"""
question:
    given doubly linklist, check if its palindrome

idea:
    using 2 ptr
    1 ptr go from the front, 1 ptr go from the back
    after finding the front and back ptr, we keep comparing the value that 2 of them point to:
        if not equals => false

"""
class Node: 
    def __init__(self, data=None,next=None,prev=None): 
        self.data=data 
        self.next=next 
        self.prev=prev
    

def is_palindrome(head):
    if head==None:
        return True
    
    l= head
    r=head 

    #find the last elem
    while r.next:
        r=r.next

    while l!=r and l.prev!=r: #first condition handle odd length, second handle even length
        if l.data!=r.data:
            return False
        l=l.next
        r=r.prev
    
    return True


def test1():
    node1=Node(9)
    node2=Node(2)
    node3=Node(4)
    node4=Node(2)
    node5=Node(9)
    node1.next=node2
    node2.prev=node1
    node2.next=node3
    node3.prev=node2
    node3.next=node4
    node4.prev=node3
    node4.next=node5
    node5.prev=node4

    assert is_palindrome(node1) ==True

def test2():

    node1=Node(9)
    node2=Node(12)
    node3=Node(4)
    node4=Node(2)
    node5=Node(9)
    node1.next=node2
    node2.prev=node1
    node2.next=node3
    node3.prev=node2
    node3.next=node4
    node4.prev=node3
    node4.next=node5
    node5.prev=node4

    assert is_palindrome(node1) ==False   


if __name__=="__main__":
    test1()
    test2()
    print("passed all")


    
    
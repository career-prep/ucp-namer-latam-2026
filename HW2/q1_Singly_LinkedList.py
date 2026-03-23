class Node:
    def __init__(self, data=None,next=None):
        self.data=data
        self.next=next

    
def insertAtFront(head, val): #head is Node, val is int
    node= Node(val)

    if head==None:
        return node
    
    node.next=head
    return node

def insertAtBack(head,val): #append
    node = Node(val)

    if head ==None:
        return node
    
    curr=head
    while curr.next:
        curr=curr.next
    
    curr.next=node
    return head

def insertAfter(head, val, loc):   #create new node with data val after Node loc (insert in the middle)
    if loc ==None:
        return head

    node= Node(val)
    node.next= loc.next
    loc.next=node
    return head

def insertBefore(head, val, loc): # insert before node loc
    if loc ==None or head==None:
        return head
    
    #insert before the head
    node=Node(val)
    if loc==head:
        node.next=head
        return node

    curr=head
    while curr.next and curr.next!=loc:
        curr=curr.next
    
    #if loc not found
    if curr.next==None:
        return head

    #insert in the middle 
    node.next=curr.next
    curr.next=node
    return head


def deleteFront(head): #remove first node
    if head==None:
        return head
    
    if head.next==None:
        return None
    
    head=head.next
    return head

def deleteBack(head):
    #empty LL
    if head==None:
        return head
    
    #1 node in LL
    if head.next==None:
        return None
    
    #normal case
    curr=head
    while curr.next and curr.next.next:
        curr=curr.next
    
    curr.next=None
    return head

def deleteNode(head,loc): #delete node loc
    if loc==None or head==None:
        return head

    #if loc is head
    if loc==head:
        head=head.next
        return head

    #if loc is in middle 
    curr=head
    while curr.next and curr.next!=loc:
        curr=curr.next
    
    #could not find loc
    if curr.next==None:
        return head
    
    #if found
    curr.next=loc.next
    return head

def length(head):
    if head==None:
        return 0

    curr=head
    count=1

    while curr.next:
        count+=1
        curr=curr.next
    
    return count

def reverseIterative(head):
    if head==None or head.next==None:
        return head

    prev=None
    curr=head

    while curr:
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp
    
    return prev



    
def recursive_helper(curr,prev):
    #base case (return the sol without the need to recursion or it could be a condition that make recursion stop)
    if curr==None:
        return prev
    
    #change the direction of the pointer and move to next node to call the recursison
    next_node=curr.next
    curr.next=prev

    return recursive_helper(next_node,curr)


def reverseRecursive(head):    
    return recursive_helper(head,None)





        

        
        

        



        

        
    








        
        
        
        
        
        
        
        
        
        
        

        


        



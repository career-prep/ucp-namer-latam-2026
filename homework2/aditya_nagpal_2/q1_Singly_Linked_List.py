class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def insertAtFront(head, val):
    newNode =  Node(head)
        
    if not head:
        return newNode
        
    newNode.next = head

    return newNode

def insertAtBack(head, val):
    newNode = Node(val)

    if not head:
        return newNode
        
    curr =  head
    while curr.next:
        curr = curr.next
    curr.next = newNode

    return head
    

def insertAfter(head, val, loc):
    if loc is None:
        return head  

    newNode = Node(val)
    newNode.next = loc.next
    loc.next = newNode

    return head
    
def insertBefore(head, val, loc): 
        ## in this case we have considered that loc will always be present in the
        ##linked list, if this is not the case we need to change the while loop
        ## to check for none and that is potentially the reason for red lines
        ## .next.
    newNode = Node(val)
    if not head:
        return newNode
        
    if loc is head:
        newNode.next = head
        return newNode
        
    curr = head 
    while curr.next is not loc:
        curr = curr.next

    newNode.next = curr.next
    curr.next = newNode

    return head
    
def deleteFront(head):
    if not head:
        return None
        
    if head.next is None:
        return None
        
    head = head.next

    return head
    
def deleteBack(head):
    if head is None:
        return None
        
    if head.next is None:
        return None
        
    curr = head
    while curr.next and curr.next.next:
        curr =  curr.next
    curr.next = None

    return head
    
def deleteNode(head, loc):
    if head is None or loc is head:
        return None
          
    curr =  head
    while curr.next and curr.next is not loc:
        curr = curr.next

    temp = curr.next.next
    curr.next = temp

    return head
    
def length(head):
    curr = head
    count = 1
    while curr:
        count += 1
        curr = curr.next

    return count
    
def reverseIterative(head):
    prev = None
        
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return head
    

    

# def reverseRecursive(head):
#     if head is None or head.next is None:
#         return head
        
#     newHead = reverseRecursive(head.next)
        
#     head.next.next = head
#     head.next = None
        
#     return newHead
    


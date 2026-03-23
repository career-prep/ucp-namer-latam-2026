class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
        self.prev = None

def insertAtFront(head, val):
    newNode =  Node(head)
        
    if not head:
        return newNode
        
    newNode.next = head
    head.prev = newNode

    return newNode

def insertAtBack(head, val):
    newNode = Node(val)

    if not head:
        return newNode
        
    curr =  head
    while curr.next:
        curr = curr.next

    curr.next = newNode
    newNode.prev = curr

    return head
    
# assumption: a head definately exists
def insertAfter(head, val, loc):
    if loc is None:
        return head 

    newNode = Node(val)
    if loc.next is None:
        loc.next = newNode
        newNode.prev = loc
    else:
        temp = loc.next         
        newNode.next = temp
        newNode.prev = loc
        loc.next = newNode
        temp.prev = newNode


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
        head.prev = newNode
        return newNode
        

    temp = loc.prev
    newNode.next = loc
    newNode.prev = temp
    temp.next = newNode
    loc.prev = newNode

    return head
    
def deleteFront(head):
    if not head:
        return None
        
    if head.next is None:
        return None
        
    head = head.next
    head.prev = None

    return head
    
def deleteBack(head):
    if head is None:
        return None
        
    if head.next is None:
        return None
        
    curr = head
    while curr.next and curr.next.next:
        curr =  curr.next

    temp = curr.next
    curr.next = None
    temp.prev = None

    return head
    
#assumption: the location is never none
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
        
    curr = head
    while curr:
        temp = curr.next
        curr.next = curr.prev
        curr.prev = temp
        newHead = curr
        # curr.prev = temp
        # last = curr
        curr = curr.prev

    return newHead
    

    

def reverseRecursive(head):
    if head is None or head.next is None:
        return head
        
    newHead = reverseRecursive(head.next)
        
    head.next.next = head
    head.next = None
        
    return newHead


    


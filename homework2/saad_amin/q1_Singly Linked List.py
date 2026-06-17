class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtFront(head, val):
    new_node = Node(val)
    new_node.next = head
    return new_node

def insertAtBack(head, val):
    new_node = Node(val)
    
    if not head:
        new_node.next = head
        return new_node
     
    curr = head
    
    while curr.next:
        curr = curr.next

    curr.next = new_node
    return head

def insertAfter(head, val, loc):
    new_node = Node(val)
    new_node.next = loc.next  
    loc.next = new_node 
    return head    

def inserBefore(head, val, loc):
    new_node = Node(val)
    
    if head == loc:
        new_node.next = head
        return new_node

    curr = head
    
    while curr.next and curr.next != loc:
        curr = curr.next
        
    new_node.next = curr.next
    curr.next = new_node
    
    return head

def deleteFront(head):
    if not head:
        return head
    
    temp = head.next
    head.next = None
    return temp

def deleteBack(head):
    curr = head
    if not head or not head.next:
        return None
    
    while curr.next.next != None:
        curr = curr.next
        
    curr.next = None
    return head
    
def deleteNode(head, loc):
    curr = head
    if not head:
        return None
    
    if head == loc:
        temp = head.next
        loc.next = None
        return temp

    
    while curr.next and curr.next != loc:
        curr = curr.next
    
    if curr.next:
        curr.next = curr.next.next
        loc.next = None
    return head

def length(head):
    if not head:
        return 0
    count = 0
    
    curr = head
    while curr:
        curr = curr.next
        count +=1 
        
    return count   

def reverseIterative(head):
    if not head:
        return None
    
    curr = head
    prev = None
    
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        
    return prev

def reverseRecursive(head):
    if not head or not head.next:
        return head

    new_head = reverseRecursive(head.next)

    head.next.next = head 
    head.next = None        
    return new_head
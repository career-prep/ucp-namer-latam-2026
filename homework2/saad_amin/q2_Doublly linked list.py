class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
def insertAtFront(head, val):
    new_node = Node(val)
    if not head:
        return new_node

    new_node.next = head
    head.prev = new_node
    
    return new_node

def insertAtBack(head, tail,  val):
    new_node = Node(val)
    
    if not head:
        return new_node
    
    tail.next = new_node
    new_node.prev = tail
    
    return head

def insertAfter(head, val, loc):
    new_node = Node(val)
    new_node.next = loc.next  
    loc.next = new_node 
    new_node.prev = loc
    
    if new_node.next:
        new_node.next.prev = new_node
        
    return head    

def inserBefore(head, val, loc):
    new_node = Node(val)
    prevv = loc.prev
    
    if loc.prev is None:
        new_node.next = loc
        loc.prev = new_node
        return new_node
    
    loc.prev = new_node
    new_node.next = loc
    prevv.next = new_node
    new_node.prev = prevv
    
    return head

def deleteFront(head):
    if not head:
        return None
    if not head.next:
        return None
    
    temp = head.next
    temp.prev = None
    head.next = None
    return temp

def deleteBack(head, tail):
    if not head:
        return None
    
    prevv = tail.prev
    prevv.next = None
    tail.prev = None
    
    return head
    
def deleteNode(head, loc):
    if not head:
        return None
    
    if loc == head:
        new_head = head.next
        if new_head:
            new_head.prev = None
        return new_head
    
    if loc.next is None:
        prevv = loc.prev
        prevv.next = None
        loc.prev = None   
        return head
    
    temp = loc.next
    prevv = loc.prev
    prevv.next = temp
    temp.prev = prevv
    
    loc.prev = None
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
        curr.prev, curr.next = curr.next, curr.prev
        prev = curr
        curr = curr.prev
        
    return prev

def reverseRecursive(head):
    def helper(node):
        if not node:
            return None

        node.prev, node.next = node.next, node.prev
        
        if not node.prev:
            return node

        return helper(node.prev)
    return helper(head)
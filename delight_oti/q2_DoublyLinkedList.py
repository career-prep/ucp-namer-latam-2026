class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def insertAtFront(head, val):
    new_node = Node(val)

    if head:
        head.prev = new_node
        new_node.next = head
        
    return new_node

def insertAtBack(head, tail, val):
    new_node = Node(val)
    
    if head is None:
        return new_node
    
    tail.next = new_node
    new_node.prev = tail

    return head
    

def insertAfter(head, val, loc):
    new_node = Node(val)

    new_node.next = loc.next
    new_node.prev = loc

    if loc.next:
        loc.next.prev = new_node
    
    loc.next = new_node

    return head

def insertBefore(head, val, loc):
    new_node = Node(val)

    new_node.prev = loc.prev
    new_node.next = loc

    if loc.prev:
        loc.prev.next = new_node
    else:
        head = new_node

    loc.prev = new_node

    return head

def deleteFront(head):

    if head is None:
        return None
    
    new_head = head.next
    
    if new_head:
        new_head.prev = None

    return new_head

def deleteBack(head, tail):
    
    if head is None:
        return None
    if tail.prev is None:
        return None
    
    tail.prev.next = None
    
    return head

def deleteNode(head, loc):

    if head is None:
        return None
    
    if head == loc:
        new_head = head.next
        if new_head:
            new_head.prev = None
        return new_head
    

    loc.prev.next = loc.next
    
    if loc.next:
        loc.next.prev = loc.prev
    
    return head

def length(head):
    
    if head is None:
        return 0
    
    curr = head

    length = 0

    while curr:
        length += 1
        curr = curr.next
    
    return length

def reverseIterative(head):

    curr = head
    temp = None

    while curr != None:
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        curr = curr.prev
    
    head = temp.prev

    return head

def reverseRecursive(head):

    return helper(head, None)


def helper(curr, prev):

    if curr is None:
        return prev

    next_node = curr.next

    curr.next = prev
    curr.prev = next_node

    return helper(next_node, curr)
    
#34 mins

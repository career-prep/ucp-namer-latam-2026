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
    
    if head is None:
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

def insertBefore(head, val, loc):
    new_node = Node(val)

    if head is None:
        return new_node
    
    curr = head
    while curr.next != loc:
        curr = curr.next
    
    new_node.next = loc
    curr.next = new_node

    return head

def deleteFront(head):

    if head is None:
        return None
    
    return head.next

def deleteBack(head):
    
    if head is None:
        return None
    
    curr = head

    while curr.next.next:
        curr = curr.next
    
    curr.next = None

    return head

def deleteNode(head, loc):

    if head is None:
        return None
    
    if head == loc:
        return head.next
    
    while curr.next != loc:
        curr = curr.next
    
    curr.next = loc.next
    
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

    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr= next_node
    
    return prev

def reverseRecursive(head):

    return helper(head, None)


def helper(curr, prev):

    if curr is None:
        return prev

    next_node = curr.next
    curr.next = prev

    return helper(next_node, curr)
    
#34 mins

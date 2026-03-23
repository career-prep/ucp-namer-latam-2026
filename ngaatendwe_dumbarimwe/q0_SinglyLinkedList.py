class Node:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

def insertAtFront(head,val):
    if not head:
        return Node(val)
    
    new_head = Node(val)
    new_head.next = head 

    return new_head


def insertAtBack(head, val):
    if not head:
        return Node(val)

    curr = head 
    while curr.next:
        curr = curr.next
    curr.next = Node(val)

    return head

def insertAfter(head, val, loc):
    curr = head

    while curr:
        if curr is loc:
            new_node = Node(val, curr.next)
            curr.next = new_node
            break
        curr = curr.next

    return head


def insertBefore(head, val, loc):
    if head is loc:
        return Node(val, head)

    curr = head
    while curr.next:
        if curr.next is loc:
            curr.next = Node(val, curr.next)
            break
        curr = curr.next

    return head

def deleteFront(head):
    if not head:
        return None
    return head.next

def deleteBack(head):
    if not head:
        return None

    if not head.next:
        return None

    curr = head
    while curr.next.next:
        curr = curr.next

    curr.next = None
    return head 

def deleteNode(head, loc):
    if head is loc:
        return head.next

    curr = head
    while curr.next:
        if curr.next is loc:
            curr.next = curr.next.next
            break
        curr = curr.next

    return head

def length(head):
    count = 0
    curr = head 

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
    return prev

def reverseRecursive(head):
    if not head or not head.next:
        return head

    new_head = reverseRecursive(head.next)

    head.next.next = head 
    head.next = None       

    return new_head
    




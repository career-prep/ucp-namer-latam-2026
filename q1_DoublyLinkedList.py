class Node:
    def __init__(self,val,next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev 

def insertAtFront(head, val):
    new_head = Node(val)
    if head:
        head.prev = new_head
        new_head.next = head
    return new_head

def insertAtBack(head, tail, val):
    new_node = Node(val)

    if not head:
        return new_node, new_node  # new head, tail

    tail.next = new_node
    new_node.prev = tail
    return head, new_node 

def insertAfter(head, val, loc):
    curr = head

    while curr:
        if curr is loc:
            new_node = Node(val)
            new_node.next = curr.next
            new_node.prev = curr

            if curr.next:
                curr.next.prev = new_node

            curr.next = new_node
            break

        curr = curr.next

    return head

def insertBefore(head, val, loc):
    if head is loc:
        new_head = Node(val, head)
        head.prev = new_head
        return new_head

    curr = head
    while curr:
        if curr is loc:
            new_node = Node(val)
            prev_node = curr.prev

            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = curr
            curr.prev = new_node
            break

        curr = curr.next

    return head

def deleteFront(head):
    if not head:
        return None

    new_head = head.next
    if new_head:
        new_head.prev = None

    return new_head

def deleteBack(head):
    if not head:
        return None

    if not head.next:
        return None

    curr = head
    while curr.next:
        curr = curr.next

    curr.prev.next = None
    return head 


def deleteNode(head, loc):
    if not head:
        return None

    if head is loc:
        new_head = head.next
        if new_head:
            new_head.prev = None
        return new_head

    curr = head
    while curr:
        if curr is loc:
            if curr.prev:
                curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev
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
    curr = head
    new_head = None

    while curr:
        curr.prev, curr.next = curr.next, curr.prev
        new_head = curr
        curr = curr.prev  

    return new_head

def reverseRecursive(head):
    if not head:
        return None

    head.prev, head.next = head.next, head.prev

    if not head.prev:
        return head

    return reverseRecursive(head.prev)


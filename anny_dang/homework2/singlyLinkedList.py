class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtFront(head, val):
    new_head = Node(val)
    new_head.next = head
    return new_head

def insertAtBack(head, val):
    if not head:
        return Node(val)
    
    cur = head 
    while cur.next:
        cur = cur.next
    cur.next = Node(val)

    return head

def insertAfter(head, val, loc):
    """
    assume that loc always exists in head
    """
    new_node = Node(val)
    temp = loc.next
    loc.next = new_node
    new_node.next = temp
    return head

def insertBefore(head, val, loc):
    """
    assume that loc always exists in head
    """
    if loc == head:
        return insertAtFront(head, val)
    
    prev = None
    cur = head
    while cur and cur != loc:
        prev = cur
        cur = cur.next

    new_node = Node(val)
    prev.next = new_node
    new_node.next = loc
    return head

def deleteFront(head):
    if not head:
        return head
    
    head = head.next
    return head 

def deleteBack(head):
    if not head:
        return head
    if not head.next:
        return None
    
    prev = None
    cur = head
    while cur and cur.next:
        prev = cur
        cur = cur.next
    
    prev.next = None
    return head

def deleteNode(head, loc):
    """
    assume head exists and loc always exists in head
    """
    if head == loc:
        return deleteFront(head)
    
    prev = None
    cur = head
    while cur and cur != loc:
        prev = cur
        cur = cur.next

    temp = loc.next
    prev.next = temp
    return head

def length(head):
    l = 0
    cur = head
    while cur:
        cur = cur.next
        l += 1

    return l 

def reverseIterative(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    
    return prev

def reverseRecursive(head):
    def recursion(prev, cur):
        if not cur:
            return prev
        
        nxt = cur.next
        cur.next = prev
        return recursion(cur, nxt)

    return recursion(None, head) 
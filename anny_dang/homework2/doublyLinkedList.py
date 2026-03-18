class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def insertAtFront(head, val):
    """Create a new Node with data val at the front; return head. O(1)."""
    if not head:
        return Node(val)
    
    new_head = Node(val)
    new_head.next = head
    head.prev = new_head
    return new_head

def insertAtBack(head, tail, val):
    """Create a new Node with data val at the end; return head. O(1)."""
    if not head:
        return Node(val)
    
    new_tail = Node(val)
    tail.next = new_tail
    new_tail.prev = tail
    return head

def insertAfter(head, val, loc):
    """Create a new Node with data val after loc; return head. O(1)."""
    new_node = Node(val)
    if not loc.next:
        loc.next = new_node
        new_node.prev = loc
    else:
        nxt_node = loc.next
        loc.next = new_node
        new_node.prev = loc
        new_node.next = nxt_node
        nxt_node.prev = new_node
    return head

def insertBefore(head, val, loc):
    """Create a new Node with data val before loc; return head. O(1)."""
    new_node = Node(val)
    if head == loc:
        new_node.next = loc
        loc.prev = new_node
        return new_node
    else:
        prev_node = loc.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = loc
        loc.prev = new_node
        return head

def deleteFront(head):
    """Remove the first node; return head. O(1)."""
    if not head:
        return head
    if not head.next:
        return None
    
    new_head = head.next
    new_head.prev = None
    return new_head


def deleteBack(head, tail):
    """Remove the last node; return head. O(1)."""
    if head == tail:
        return None

    new_tail = tail.prev
    new_tail.next = None
    tail.prev = None
    return head

def deleteNode(head, loc):
    """Delete loc; return head. O(1)."""
    """ assume that loc always exists """
    if head == loc:
        return deleteFront(head)
    
    prev = loc.prev
    nxt = None
    if loc.next:
        nxt = loc.next
        prev.next = nxt
        nxt.prev = prev
    else:
        prev.next = None
        loc.prev = None
    return head

def length(head):
    """Return the length of the list. O(n)."""
    cur = head
    l = 0
    while cur:
        cur = cur.next
        l += 1
    
    return l

def reverseIterative(head):
    """Reverse the linked list iteratively. O(n)."""
    prev = None
    cur = head
    while cur:
        cur.prev, cur.next = cur.next, cur.prev
        prev = cur
        cur = cur.prev
    
    return prev

def reverseRecursive(head):
    """Reverse the linked list recursively. O(n)."""
    def recursion(prev, cur):
        if not cur:
            return prev
        
        cur.prev, cur.next = cur.next, cur.prev

        return recursion(cur, cur.prev)

    return recursion(None, head)
        

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # extra pointer going backwards
 
 
# Time: O(1)
def dll_insertAtFront(head, val):
    new_node = DoublyNode(val)
    if head is not None:
        head.prev = new_node
    new_node.next = head
    return new_node
 
 
# now we need tail so we can just stick the new node right at the end
# Time: O(1) - this is why doubly LL is nice vs singly
def dll_insertAtBack(head, tail, val):
    new_node = DoublyNode(val)
    if tail is None:
        return new_node, new_node  # empty list
    tail.next = new_node
    new_node.prev = tail
    return head, new_node  # new tail is the new node
 
 
# Time: O(1) - we have loc so just rewire neighbors
def dll_insertAfter(head, val, loc):
    new_node = DoublyNode(val)
    new_node.next = loc.next
    new_node.prev = loc
    if loc.next is not None:
        loc.next.prev = new_node
    loc.next = new_node
    return head
 
 
# Time: O(1) - prev pointer lets us get to loc's predecessor instantly
def dll_insertBefore(head, val, loc):
    new_node = DoublyNode(val)
    new_node.next = loc
    new_node.prev = loc.prev
    if loc.prev is not None:
        loc.prev.next = new_node
    else:
        head = new_node  # loc was the head
    loc.prev = new_node
    return head
 
 
# Time: O(1)
def dll_deleteFront(head):
    if head is None:
        return None
    head = head.next
    if head is not None:
        head.prev = None
    return head
 
 
# Time: O(1) - tail pointer makes this instant unlike singly LL
def dll_deleteBack(head, tail):
    if tail is None:
        return None, None
    tail = tail.prev
    if tail is not None:
        tail.next = None
    else:
        head = None  # list is now empty
    return head, tail
 
 
# Time: O(1) - just rewire the two neighbors around loc
def dll_deleteNode(head, loc):
    if loc.prev is not None:
        loc.prev.next = loc.next
    else:
        head = loc.next  # loc was the head
    if loc.next is not None:
        loc.next.prev = loc.prev
    return head
 
 
# Time: O(n)
def dll_length(head):
    count = 0
    curr = head
    while curr is not None:
        count += 1
        curr = curr.next
    return count
 
 
# swap next and prev for every node, then return what used to be the tail
# Time: O(n)
def dll_reverseIterative(head):
    curr = head
    new_head = None
    while curr is not None:
        # swap next and prev
        curr.prev, curr.next = curr.next, curr.prev
        new_head = curr
        curr = curr.prev  # after the swap, prev is the "old next"
    return new_head
 
 
# same idea recursively
# Time: O(n)
def dll_reverseRecursive(head):
    if head is None or head.next is None:
        if head is not None:
            head.prev, head.next = head.next, head.prev
        return head
    new_head = dll_reverseRecursive(head.next)
    head.next.next = head   # point back to us
    head.prev = head.next   # update our prev
    head.next = None        # we're the new tail
    return new_head

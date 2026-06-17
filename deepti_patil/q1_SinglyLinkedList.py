class SinglyNode:
    def __init__(self, data):
        self.data = data
        self.next = None  # just points forward, thats it
 
 
# adds a new node at the very beginning - super simple since we just
# point the new node to wherever head currently is
# Time: O(1)
def insertAtFront(head, val):
    new_node = SinglyNode(val)
    new_node.next = head
    return new_node  # new node is the new head now
 
 
# have to walk all the way to the end to stick the new node on
# Time: O(n)
def insertAtBack(head, val):
    new_node = SinglyNode(val)
    if head is None:
        return new_node  # empty list edge case
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = new_node
    return head
 
 
# loc is the node we insert AFTER - we already have a pointer to it
# so no traversal needed, just rewire two pointers
# Time: O(1)
def insertAfter(head, val, loc):
    new_node = SinglyNode(val)
    new_node.next = loc.next
    loc.next = new_node
    return head
 
 
# inserting BEFORE loc means we need to find the node that comes before loc
# since we can't go backwards in a singly LL we have to walk from the front
# Time: O(n)
def insertBefore(head, val, loc):
    new_node = SinglyNode(val)
    # special case: inserting before the head itself
    if head == loc:
        new_node.next = head
        return new_node
    curr = head
    while curr is not None and curr.next != loc:
        curr = curr.next
    if curr is None:
        return head  # loc wasn't in the list, do nothing
    new_node.next = loc
    curr.next = new_node
    return head
 
 
# just skip over the first node
# Time: O(1)
def deleteFront(head):
    if head is None:
        return None
    return head.next
 
 
# walk until we find the second-to-last node, then cut off the last one
# Time: O(n)
def deleteBack(head):
    if head is None:
        return None
    if head.next is None:
        return None  # only one element
    curr = head
    while curr.next.next is not None:
        curr = curr.next
    curr.next = None  # snip off the last node
    return head
 
 
# find the node just before loc, then rewire around loc
# Time: O(n)
def deleteNode(head, loc):
    if head is None:
        return None
    if head == loc:
        return head.next  # deleting the head
    curr = head
    while curr is not None and curr.next != loc:
        curr = curr.next
    if curr is None:
        return head  # loc wasnt found
    curr.next = loc.next
    return head
 
 
# just count as we walk - nothing fancy
# Time: O(n)
def length(head):
    count = 0
    curr = head
    while curr is not None:
        count += 1
        curr = curr.next
    return count
 
 
# 3-pointer reversal prev, curr, next_node
# at each step we flip the arrow then advance
# Time: O(n)
def reverseIterative(head):
    prev = None
    curr = head
    while curr is not None:
        next_node = curr.next  # save next before we break the link
        curr.next = prev       # flip the arrow
        prev = curr            # advance prev
        curr = next_node       # advance curr
    return prev  # prev is the new head
 
 
# recursive reversalafter reversing the rest of the list
# we need to make the node after us point back at us
# Time: O(n)
def reverseRecursive(head):
    # base case: empty or single node, already reversed
    if head is None or head.next is None:
        return head

# Technique: Linked list fixed-distance two-pointer
# Time: O(n) - single pass
# Space: O(1)
 
# classic fixed-distance two pointer trick:
# send fast pointer k steps ahead, then move both until fast hits the end
# at that point slow is right at the (k)th from last node
 
def moveNthLastToFront(head, k):
    if head is None:
        return head
 
    # send fast k steps ahead
    fast = head
    for _ in range(k):
        if fast is None:
            return head  # k is larger than list length, do nothing
        fast = fast.next
 
    # edge case: k == length of list, so nth from last IS the head - nothing to do
    if fast is None:
        return head
 
    # now move both until fast.next is None
    # we need slow to be one BEFORE the target so we can rewire around it
    slow = head
    while fast.next is not None:
        fast = fast.next
        slow = slow.next
 
    # slow.next is now the node we want to move to front
    target = slow.next
    slow.next = target.next  # cut target out of its current position
    target.next = head       # stick it at the front
    return target            # target is the new head
 

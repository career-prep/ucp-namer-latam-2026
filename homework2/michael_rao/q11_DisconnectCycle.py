class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def disconnectCycle(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head
    has_cycle = False
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return head

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    cycle_start = slow

    curr = cycle_start
    while curr.next != cycle_start:
        curr = curr.next
    curr.next = None

    return head
# time: O(n)

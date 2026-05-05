class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def moveNthLastToFirst(head, n):
    if not head or n <= 0:
        return head

    fast = head
    for _ in range(n - 1):
        if fast.next == None:
            return head
        fast = fast.next

    prev = None
    slow = head
    while fast.next != None:
        fast = fast.next
        prev = slow
        slow = slow.next

    if prev == None:
        return head

    prev.next = slow.next
    slow.next = head
    return slow
# time: O(n)

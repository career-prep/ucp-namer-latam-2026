class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def dedupSortedList(head):
    curr = head
    while curr != None and curr.next != None:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
# time: O(n)

# Technique: Linked list fixed-distance two-pointer
# time complexity: O(n)
# space complexity: O(1)
# 20 minutes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def moveNthLastToFront(head, k):
    if not head:
        return None

    dummy = Node(0)
    dummy.next = head

    fast = dummy
    slow = dummy

    # advance fast k steps ahead of slow
    for _ in range(k):
        if not fast.next:
            return head  # k > length of list, do nothing
        fast = fast.next

    # advance both until fast reaches the last node
    while fast.next:
        slow = slow.next
        fast = fast.next

    # slow.next is the nth from last node
    target = slow.next
    slow.next = target.next
    target.next = dummy.next
    dummy.next = target

    return dummy.next

# helpers
def to_list(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result

def from_list(lst):
    if not lst:
        return None
    head = Node(lst[0])
    curr = head
    for val in lst[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head

# test cases
# k=2: 2nd from last is 6, move to front
head1 = from_list([15, 2, 8, 7, 20, 9, 11, 6, 19])
assert to_list(moveNthLastToFront(head1, 2)) == [6, 15, 2, 8, 7, 20, 9, 11, 19]

# k=7: 7th from last is 8, move to front
head2 = from_list([15, 2, 8, 7, 20, 9, 11, 6, 19])
assert to_list(moveNthLastToFront(head2, 7)) == [8, 15, 2, 7, 20, 9, 11, 6, 19]

# k=1: move last element to front
head3 = from_list([1, 2, 3, 4, 5])
assert to_list(moveNthLastToFront(head3, 1)) == [5, 1, 2, 3, 4]

# k equals length: move head to front (no-op effectively)
head4 = from_list([1, 2, 3])
assert to_list(moveNthLastToFront(head4, 3)) == [1, 2, 3]

print("yay!!")

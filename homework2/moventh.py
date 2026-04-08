# Technique: Linked list fixed-distance two-pointer
# Time Complexity: O(n)
# Space Complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

def moveNthLastToFront(head, n):
    dummy      = ListNode(0)
    dummy.next = head
    fast       = dummy
    slow       = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    target     = slow.next
    slow.next  = target.next   
    target.next = dummy.next   
    dummy.next = target        

    return dummy.next

def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def build(vals):
    dummy = ListNode(0)
    curr  = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

vals = [15,2,8,7,20,9,11,6,19]

# Test 1: k=2 → 6 moves to front
print(to_list(moveNthLastToFront(build(vals), 2)))
# [6, 15, 2, 8, 7, 20, 9, 11, 19]

# Test 2: k=7 → 8 moves to front
print(to_list(moveNthLastToFront(build(vals), 7)))
# [8, 15, 2, 7, 20, 9, 11, 6, 19]

# Test 3: k=1 → last element moves to front
print(to_list(moveNthLastToFront(build(vals), 1)))
# [19, 15, 2, 8, 7, 20, 9, 11, 6]

# Time spent: ~35 minutes

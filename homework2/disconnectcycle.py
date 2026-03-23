# Technique: Linked list fast-slow two-pointer
# Time Complexity: O(n)
# Space Complexity: O(1)


class ListNode:
    def __init__(self, val=0):
        self.val  = val
        self.next = None

def disconnectCycle(head):
    if not head:
        return head

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return head  # no cycle

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    cycle_tail = fast
    while cycle_tail.next != fast:
        cycle_tail = cycle_tail.next

    cycle_tail.next = None   
    return head

def to_list(head):
    result, seen = [], set()
    while head and head not in seen:
        result.append(head.val)
        seen.add(head)
        head = head.next
    return result

# Test 1: cycle from 4 back to 12
n1,n2,n3,n4,n5,n6 = ListNode(10),ListNode(18),ListNode(12),ListNode(9),ListNode(11),ListNode(4)
n1.next=n2; n2.next=n3; n3.next=n4; n4.next=n5; n5.next=n6
n6.next=n3  # cycle: 4 → 12
disconnectCycle(n1)
print(to_list(n1))   # [10, 18, 12, 9, 11, 4]

# Test 2: no cycle
p1,p2,p3 = ListNode(1),ListNode(2),ListNode(3)
p1.next=p2; p2.next=p3
disconnectCycle(p1)
print(to_list(p1))   # [1, 2, 3]

# Time spent: ~40 minutes


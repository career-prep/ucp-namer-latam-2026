# Technique: Linked list fast-slow two-pointer
# Time Complexity: O(n)
# Space Complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

def dedupSortedList(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next  
        else:
            curr = curr.next            
    return head

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

# Test 1: [1,2,2,4,5,5,5,10,10] → [1,2,4,5,10]
head1 = build([1,2,2,4,5,5,5,10,10])
print(to_list(dedupSortedList(head1)))  # [1, 2, 4, 5, 10]

# Test 2: [8,8,8,8] → [8]
head2 = build([8,8,8,8])
print(to_list(dedupSortedList(head2)))  # [8]

# Test 3: no duplicates
head3 = build([1,2,3])
print(to_list(dedupSortedList(head3)))  # [1, 2, 3]

# Time spent: ~40 minutes

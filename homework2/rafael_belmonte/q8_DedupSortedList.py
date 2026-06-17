# Technique: Linked list fast-slow two-pointer
# time complexity: O(n)
# space complexity: O(1)
# 10 minutes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def dedupSortedList(head):
    if not head:
        return None
    slow = head
    fast = head.next
    while fast:
        if fast.data != slow.data:
            slow.next = fast
            slow = fast
        fast = fast.next
    slow.next = None  # cut off any remaining duplicates at the tail end
    return head

# helpers for testing
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
head1 = from_list([1, 2, 2, 4, 5, 5, 5, 10, 10])
assert to_list(dedupSortedList(head1)) == [1, 2, 4, 5, 10]

head2 = from_list([8, 8, 8, 8])
assert to_list(dedupSortedList(head2)) == [8]

head3 = from_list([1, 2, 3])
assert to_list(dedupSortedList(head3)) == [1, 2, 3]

head4 = from_list([1])
assert to_list(dedupSortedList(head4)) == [1]

assert dedupSortedList(None) is None

print("yay!!")

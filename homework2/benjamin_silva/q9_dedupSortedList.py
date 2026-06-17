# Technique: Fast and slow pointer
# Time Complexity: O(n)
# Space Complexity: O(1)
# Time spent: 15 minutes

from q1_singlyLinkedList import Node, insertAtBack


def dedup_sorted_list(head):
    curr = head
    while curr:
        while curr.next and curr.next.data == curr.data:
            curr.next = curr.next.next
        curr = curr.next
    return head

def build_list(values):
    head = None
    for v in values:
        head = insertAtBack(head, v)
    return head


def to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.data)
        curr = curr.next
    return result


head = build_list([1, 2, 2, 4, 5, 5, 5, 10, 10])
print(to_list(dedup_sorted_list(head)))  # expected [1, 2, 4, 5, 10]

head = build_list([8, 8, 8, 8])
print(to_list(dedup_sorted_list(head)))  # expected [8]
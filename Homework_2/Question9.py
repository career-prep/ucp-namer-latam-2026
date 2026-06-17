# Given a sorted singly linked list, remove any duplicates so that no
# value appears more than once.

# Examples:

# Input: 1 -> 2 -> 2 -> 3 -> 3 -> 3 -> 4
# Output: 1 -> 2 -> 3 -> 4

# Input: 1 -> 1 -> 1 -> 1
# Output: 1

# Technique: Linked list reset/catch-up two-pointer

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def dedup_sorted_list(head):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head


def to_list(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    return result


def from_list(lst):
    if not lst:
        return None
    head = Node(lst[0])
    current = head
    for val in lst[1:]:
        current.next = Node(val)
        current = current.next
    return head


head = from_list([1, 2, 2, 3, 3, 3, 4])
print(to_list(dedup_sorted_list(head)))

head = from_list([1, 1, 1, 1])
print(to_list(dedup_sorted_list(head)))

head = from_list([1, 2, 3])
print(to_list(dedup_sorted_list(head)))

head = from_list([])
print(to_list(dedup_sorted_list(head)))

head = from_list([1, 1, 2, 3, 3, 4, 5, 5, 5])
print(to_list(dedup_sorted_list(head)))

# Time Complexity: O(n)
# Space Complexity: O(1)
# Spent 38 mins

# Given a singly linked list, move the nth from the last element to the
# front of the list.

# Examples:

# Input: k=2, 15 -> 2 -> 8 -> 7 -> 20 -> 9 -> 11 -> 6 -> 19
# Output: 6 -> 15 -> 2 -> 8 -> 7 -> 20 -> 9 -> 11 -> 19

# Input: k=7, 15 -> 2 -> 8 -> 7 -> 20 -> 9 -> 11 -> 6 -> 19
# Output: 8 -> 15 -> 2 -> 7 -> 20 -> 9 -> 11 -> 6 -> 19

# Technique: Linked list fixed-distance two-pointer

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def move_nth_last_to_front(head, n):
    if head is None or n <= 0:
        return head
    front = head
    back = head
    for _ in range(n):
        if front is None:
            return head
        front = front.next
    if front is None:
        return head
    prev = None
    while front:
        prev = back
        back = back.next
        front = front.next
    if prev is None:
        return head
    prev.next = back.next
    back.next = head
    return back


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


head = from_list([15, 2, 8, 7, 20, 9, 11, 6, 19])
print(to_list(move_nth_last_to_front(head, 2)))

head = from_list([15, 2, 8, 7, 20, 9, 11, 6, 19])
print(to_list(move_nth_last_to_front(head, 7)))

head = from_list([1, 2, 3])
print(to_list(move_nth_last_to_front(head, 1)))

head = from_list([1, 2, 3])
print(to_list(move_nth_last_to_front(head, 3)))

head = from_list([1, 2])
print(to_list(move_nth_last_to_front(head, 1)))

# Time Complexity: O(n)
# Space Complexity: O(1)
# Spent 25 mins

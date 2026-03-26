# Given a singly linked list, disconnect the cycle, if one exists.

# Examples:

# Input: 10 -> 18 -> 12 -> 9 -> 11 -> 4 -> (back to 12)
# Output: 10 -> 18 -> 12 -> 9 -> 11 -> 4

# Input: 10 -> 18 -> 12 -> 9 -> 11 -> 4 -> (back to 10)
# Output: 10 -> 18 -> 12 -> 9 -> 11 -> 4

# Technique: Linked list fast-slow two-pointer

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def disconnect_cycle(head):
    if head is None:
        return head
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return head
    slow = head
    prev = None
    while slow is not fast:
        slow = slow.next
        prev = fast
        fast = fast.next
    if slow is fast and prev is None:
        current = slow
        while current.next is not slow:
            current = current.next
        current.next = None
    else:
        prev.next = None
    return head


def to_list(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    return result


def from_list_with_cycle(lst, cycle_index):
    if not lst:
        return None
    nodes = []
    head = Node(lst[0])
    nodes.append(head)
    current = head
    for val in lst[1:]:
        new_node = Node(val)
        current.next = new_node
        nodes.append(new_node)
        current = new_node
    if cycle_index >= 0:
        current.next = nodes[cycle_index]
    return head


head = from_list_with_cycle([10, 18, 12, 9, 11, 4], 2)
print(to_list(disconnect_cycle(head)))

head = from_list_with_cycle([10, 18, 12, 9, 11, 4], 0)
print(to_list(disconnect_cycle(head)))

head = from_list_with_cycle([1, 2, 3, 4, 5], -1)
print(to_list(disconnect_cycle(head)))

head = from_list_with_cycle([1, 2], 0)
print(to_list(disconnect_cycle(head)))

head = from_list_with_cycle([1, 2, 3], 1)
print(to_list(disconnect_cycle(head)))

# Time Complexity: O(n)
# Space Complexity: O(1)
# Spent 35 mins

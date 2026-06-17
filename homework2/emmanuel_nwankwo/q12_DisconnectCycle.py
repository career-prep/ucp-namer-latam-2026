# Technique: Linked list fast-slow two-pointer
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def disconnect_cycle(head):
    if not head or not head.next:
        return head

    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast: break
    else:
        return head

    slow = head
    if slow == fast:  # Cycle starts at head
        while fast.next != slow: fast = fast.next
    else:
        while slow.next != fast.next: slow, fast = slow.next, fast.next

    fast.next = None
    return head

def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> " if curr.next else "\n")
        curr = curr.next

# Time Taken: 18mins 26secs

# Test Cases
h1 = Node(10)
h1.next = Node(18)
h1.next.next = Node(12)
h1.next.next.next = Node(9)
h1.next.next.next.next = Node(11)
h1.next.next.next.next.next = Node(4)

h1.next.next.next.next.next.next = h1.next.next
disconnect_cycle(h1)
print_list(h1)

h2 = Node(10)
h2.next = Node(18)
h2.next.next = Node(12)
h2.next.next.next = Node(9)
h2.next.next.next.next = Node(11)
h2.next.next.next.next.next = Node(4)

h2.next.next.next.next.next.next = h2.next.next.next.next.next
disconnect_cycle(h2)
print_list(h2)

# Edge cases
h3 = Node(1)
h3.next = Node(2)
h3.next.next = Node(3)

disconnect_cycle(h3)
print_list(h3)

h4 = Node(7)
h4.next = h4

disconnect_cycle(h4)
print_list(h4)
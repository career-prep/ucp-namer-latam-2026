# Technique: Linked list fixed-distance two-pointer
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def move_nth_last_to_front(head, k):
    if not head or not head.next or k <= 0:
        return head

    slow = head
    fast = head

    for i in range(k):
        if fast is None: # k is larger than list length
            return head
        fast = fast.next

    if fast is None:
        return head

    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    target = slow.next
    slow.next = target.next
    target.next = head
    return target

def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> " if curr.next else "\n")
        curr = curr.next

# Time Taken: 14mins 8secs

# Test Cases
h1 = Node(15)
h1.next = Node(2)
h1.next.next = Node(8)
h1.next.next.next = Node(7)
h1.next.next.next.next = Node(20)
h1.next.next.next.next.next = Node(9)
h1.next.next.next.next.next.next = Node(11)
h1.next.next.next.next.next.next.next = Node(6)
h1.next.next.next.next.next.next.next.next = Node(19)

print_list(move_nth_last_to_front(h1, 2))

h2 = Node(15)
h2.next = Node(2)
h2.next.next = Node(8)
h2.next.next.next = Node(7)
h2.next.next.next.next = Node(20)
h2.next.next.next.next.next = Node(9)
h2.next.next.next.next.next.next = Node(11)
h2.next.next.next.next.next.next.next = Node(6)
h2.next.next.next.next.next.next.next.next = Node(19)

print_list(move_nth_last_to_front(h2, 7))

# Edge cases
h3 = Node(1)
h3.next = Node(2)
h3.next.next = Node(3)
print_list(move_nth_last_to_front(h3, 3))

h4 = Node(1)
h4.next = Node(2)
print_list(move_nth_last_to_front(h4, 5))
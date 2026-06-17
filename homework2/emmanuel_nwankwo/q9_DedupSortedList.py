# Technique: Linked list recursion
# Time Complexity: O(n)
# Space Complexity: O(n)

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def dedup_sorted_list(head):
    if not head or not head.next:
        return head

    if head.data == head.next.data:
        head.next = head.next.next
        return dedup_sorted_list(head)
    else:
        head.next = dedup_sorted_list(head.next)
        return head


def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> " if curr.next else "\n")
        curr = curr.next

# Time Taken: 4mins 23secs

# Test Cases
h1 = Node(1)
h1.next = Node(2)
h1.next.next = Node(2)
h1.next.next.next = Node(4)
h1.next.next.next.next = Node(5)
h1.next.next.next.next.next = Node(5)
h1.next.next.next.next.next.next = Node(5)
h1.next.next.next.next.next.next.next = Node(10)
h1.next.next.next.next.next.next.next.next = Node(10)

print_list(dedup_sorted_list(h1))

h2 = Node(8)
h2.next = Node(8)
h2.next.next = Node(8)
h2.next.next.next = Node(8)

print_list(dedup_sorted_list(h2))

# Edge Case
h3 = None
print(dedup_sorted_list(h3))

h4 = Node(42)
print_list(dedup_sorted_list(h4))
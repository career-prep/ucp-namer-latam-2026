# Technique: Doubly linked list forward-backward two-pointer
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

def is_palindrome(head):
    if not head or not head.next:
        return True

    tail = head
    while tail.next:
        tail = tail.next

    left, right = head, tail
    while left != right and left.prev != right:
        if left.data != right.data:
            return False
        left, right = left.next, right.prev
    return True

def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> " if curr.next else "\n")
        curr = curr.next

# Time Taken: 6mins 11secs

# Test Cases
h1 = Node(9)
h1.next = Node(2)
h1.next.prev = h1
h1.next.next = Node(4)
h1.next.next.prev = h1.next
h1.next.next.next = Node(2)
h1.next.next.next.prev = h1.next.next
h1.next.next.next.next = Node(9)
h1.next.next.next.next.prev = h1.next.next.next

print(is_palindrome(h1))

h2 = Node(9)
h2.next = Node(12)
h2.next.prev = h2
h2.next.next = Node(4)
h2.next.next.prev = h2.next
h2.next.next.next = Node(2)
h2.next.next.next.prev = h2.next.next
h2.next.next.next.next = Node(9)
h2.next.next.next.next.prev = h2.next.next.next

print(is_palindrome(h2))

# Edge cases

h3 = None
print(is_palindrome(h3))

h4 = Node(7)
print(is_palindrome(h4))
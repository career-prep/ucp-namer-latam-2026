# Given a doubly linked list, determine if it is a palindrome.

# Examples:

# Input: 9 <-> 2 <-> 4 <-> 2 <-> 9
# Output: True

# Input: 9 <-> 2 <-> 4 <-> 4 <-> 2 <-> 9
# Output: True

# Input: 1 <-> 2 <-> 3
# Output: False

# Technique: Doubly linked list forward-backward two-pointer

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def is_palindrome(head):
    if head is None:
        return True
    tail = head
    while tail.next:
        tail = tail.next
    left = head
    right = tail
    while left is not right and left.prev is not right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.prev
    return True


def from_list(lst):
    if not lst:
        return None
    head = Node(lst[0])
    current = head
    for val in lst[1:]:
        new_node = Node(val)
        new_node.prev = current
        current.next = new_node
        current = new_node
    return head


print(is_palindrome(from_list([9, 2, 4, 2, 9])))
print(is_palindrome(from_list([9, 2, 4, 4, 2, 9])))
print(is_palindrome(from_list([1, 2, 3])))
print(is_palindrome(from_list([1])))
print(is_palindrome(None))
print(is_palindrome(from_list([1, 1])))
print(is_palindrome(from_list([1, 2])))

# Time Complexity: O(n)
# Space Complexity: O(1)
# Spent 20 mins
